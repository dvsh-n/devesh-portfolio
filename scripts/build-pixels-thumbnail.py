"""Rebuild the looping publication thumbnail (requires ffmpeg on PATH)."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/pixels-to-proofs'
OUTPUT = ROOT / 'public/projects/pixels-to-proofs/assets/thumbnails'
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

OUTPUT.mkdir(parents=True, exist_ok=True)
for index, name in enumerate(CLIPS):
    print(f'{index + 1}/{len(CLIPS)}: {name}', flush=True)
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
        '-i', str(SOURCE / name),
        '-vf', 'scale=640:-2,setsar=1,fps=24',
        '-an', '-c:v', 'libx264', '-crf', '23', '-preset', 'medium',
        '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
        str(OUTPUT / name),
    ], check=True)
print(f'Created unpadded clips in {OUTPUT.relative_to(ROOT)}')
