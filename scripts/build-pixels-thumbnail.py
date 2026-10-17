"""Rebuild the looping publication thumbnail (requires ffmpeg on PATH)."""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/pixels-to-proofs'
OUTPUT = ROOT / 'public/projects/pixels-to-proofs/assets/thumbnail.mp4'
# Nominal demos first, robust comparisons next, then PushT and hardware rope.
CLIPS = [
    'reacher.mp4',
    'cube.mp4',
    'rope.mp4',
    'reacher_robust.mp4',
    'cube_robust.mp4',
    'rope_robust.mp4',
    'pusht.mp4',
    'hardware.mp4',
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='pixels-thumbnail-') as directory:
    work = Path(directory)
    for index, name in enumerate(CLIPS):
        print(f'{index + 1}/{len(CLIPS)}: {name}', flush=True)
        subprocess.run([
            'ffmpeg', '-hide_banner', '-loglevel', 'error',
            '-i', str(SOURCE / name),
            '-filter_complex',
            '[0:v]fps=24,setsar=1,split=2[front][back];'
            '[back]scale=640:400:force_original_aspect_ratio=increase,'
            'crop=640:400,gblur=sigma=55:steps=3,eq=brightness=-0.12:saturation=0.6,colorchannelmixer=rr=0.55:gg=0.55:bb=0.55[bg];'
            '[front]scale=640:400:force_original_aspect_ratio=decrease:force_divisible_by=2[fg];'
            '[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[out]',
            '-map', '[out]', '-an', '-c:v', 'libx264', '-crf', '22', '-preset', 'medium',
            '-video_track_timescale', '12288', str(work / f'{index}.mp4'),
        ], check=True)
    (work / 'clips.txt').write_text(''.join(f"file '{i}.mp4'\n" for i in range(len(CLIPS))))
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
        '-f', 'concat', '-safe', '0', '-i', str(work / 'clips.txt'),
        '-c', 'copy', '-movflags', '+faststart', str(OUTPUT),
    ], check=True)
print(f'Created {OUTPUT.relative_to(ROOT)}')
