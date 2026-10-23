"""Frame the adaptive conformal prediction animation for the publication thumbnail (requires ffmpeg)."""
from pathlib import Path
import hashlib
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/adaptive-conformal-prediction/FacCp.mp4'
OUTPUT = ROOT / 'public/projects/adaptive-conformal-prediction/assets/thumbnail.mp4'

# Reachable-set prediction through Local Guarantees; exclude the experiments.
START_SECONDS = 16
END_SECONDS = 82

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
    '-ss', str(START_SECONDS), '-i', str(SOURCE),
    '-t', str(END_SECONDS - START_SECONDS),
    '-filter_complex',
    # Fit the foreground to the frame; blur is visible only in unused space.
    '[0:v]setsar=1,split=2[front][back];'
    '[front]scale=3840:2400:force_original_aspect_ratio=decrease,setsar=1[fg];'
    '[back]scale=640:400:force_original_aspect_ratio=increase,crop=640:400,'
    'gblur=sigma=55:steps=3,eq=brightness=-0.12:saturation=0.6,'
    'colorchannelmixer=rr=0.55:gg=0.55:bb=0.55,scale=3840:2400[bg];'
    '[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[out]',
    '-map', '[out]', '-an', '-c:v', 'libx264', '-crf', '18', '-preset', 'slow',
    '-movflags', '+faststart', str(OUTPUT),
], check=True)
digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()[:12]
publications = ROOT / 'src/data/publications.ts'
data = publications.read_text()
data, count = re.subn(
    r"const facCpThumbnailUrl = '[^']*';",
    f"const facCpThumbnailUrl = '/projects/adaptive-conformal-prediction/assets/thumbnail.mp4?v={digest}';",
    data,
)
if count != 1:
    raise RuntimeError('Expected one FacCP thumbnail URL in src/data/publications.ts')
publications.write_text(data)
print(f'Created {OUTPUT.relative_to(ROOT)}')
