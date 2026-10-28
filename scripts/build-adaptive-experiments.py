"""Extract cropped, once-played experiment panels from the FacCP presentation."""
from pathlib import Path
import argparse
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/faccp/FacCp.mp4'
OUTPUT = SOURCE.parent / 'experiment_videos'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source', type=Path, default=SOURCE)
parser.add_argument('--clips', nargs='+', help='Only regenerate these clip names.')
args = parser.parse_args()
# Manim's quad2d_animation.py, quad3d_animation.py, and driving_animation.py
# define the panels. Frame boundaries come from the production render's partial
# movie manifest (60 fps), including its 145-frame geometry transforms.
# Driving uses responsive SVGs converted from the original PDFs in experiment_plots
# with pdftocairo -svg input.pdf output.svg.
# Begin after outgoing panels/header animations and stop before the next fade.
# Crops retain plots, labels, and legends, removing the heading and bottom box.
CLIPS = [
    ('01-multiple-geometries', 5032, 469, '2560:990:0:200'),
    ('02-data-and-capacity', 5537, 469, '2560:990:0:200'),
    ('03-3d-reachability', 6042, 469, '2560:990:0:200'),
]

OUTPUT.mkdir(parents=True, exist_ok=True)
for name, start_frame, frames, crop in CLIPS:
    if args.clips and name not in args.clips:
        continue
    target = OUTPUT / f'{name}.mp4'
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
        '-ss', f'{start_frame / 60:.9f}', '-i', str(args.source),
        '-frames:v', str(frames), '-vf', f'crop={crop}',
        '-map', '0:v:0', '-an', '-c:v', 'libx264', '-crf', '18',
        '-preset', 'fast', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
        str(target),
    ], check=True)
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
        '-sseof', '-0.05', '-i', str(target), '-frames:v', '1',
        '-q:v', '2', str(OUTPUT / f'{name}.jpg'),
    ], check=True)
    print(f'Created {name}: {start_frame / 60:.3f}s, {frames} frames', flush=True)
