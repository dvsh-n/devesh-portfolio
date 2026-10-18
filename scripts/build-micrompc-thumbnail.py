"""Frame the experiments clip for the publication thumbnail (requires ffmpeg)."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/micrompc/experiments.mp4'
OUTPUT = ROOT / 'public/projects/micrompc/assets/thumbnail.mp4'

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(SOURCE),
    '-filter_complex',
    # Preserve native foreground resolution inside the shared 8:5 frame.
    '[0:v]setsar=1,split=2[fg][back];'
    '[back]scale=640:400:force_original_aspect_ratio=increase,crop=640:400,'
    'gblur=sigma=55:steps=3,eq=brightness=-0.12:saturation=0.6,'
    'colorchannelmixer=rr=0.55:gg=0.55:bb=0.55,scale=3232:2020[bg];'
    '[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p,tpad=stop_mode=clone:stop_duration=1[out]',
    '-map', '[out]', '-an', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
    '-movflags', '+faststart', str(OUTPUT),
], check=True)
print(f'Created {OUTPUT.relative_to(ROOT)}')
