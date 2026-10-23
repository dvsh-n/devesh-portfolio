"""Extract FacCP method cards at Manim section and concept-hold boundaries."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/faccp/FacCp.mp4'
OUTPUT = SOURCE.parent / 'method_videos'
# Seconds from representation.py's play/wait durations at TIME_SCALE = 1.
# Stop card 1 before its .6s fade. Card 3 ends after the retrieval-ring hold.
CLIPS = [
    ('01-reachable-set-prediction', 16.50, 27.35),
    ('02-representation-learning', 27.95, 41.10),
    ('03-local-residual-retrieval', 41.10, 50.95),
    ('04-local-residual-weights', 50.95, 58.00),
    ('05-local-geometry-retrieval', 58.00, 70.10),
    ('06-conformalized-local-geometry', 70.10, 76.60),
    ('07-local-guarantees', 76.60, 82.30),
]
OUTPUT.mkdir(parents=True, exist_ok=True)
for name, start, end in CLIPS:
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
        '-ss', str(start), '-i', str(SOURCE), '-t', f'{end-start:.2f}',
        '-map', '0:v:0', '-an', '-c:v', 'libx264', '-crf', '18',
        '-preset', 'fast', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
        str(OUTPUT / f'{name}.mp4'),
    ], check=True)
    print(f'Created {name}: {start:.2f}–{end:.2f}s', flush=True)
