"""Extract the related-work animation, ending before the board fades out."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/faccp/FacCp.mp4'
OUTPUT = ROOT / 'src/pages/projects/faccp/related-work.mp4'
STILL = ROOT / 'src/pages/projects/faccp/related-work-final.jpg'
# Manim opening_banner: .8 + .8 + 1.5 + .6 + .15 seconds.
START = 3.85
# related_work: .8 + 4 * (3 * .8) + 1.5 seconds, before FadeOut.
END = 15.75
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
    '-ss', str(START), '-i', str(SOURCE), '-t', str(END - START),
    '-map', '0:v:0', '-an', '-c:v', 'libx264', '-crf', '18',
    '-preset', 'fast', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(OUTPUT),
], check=True)
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
    '-sseof', str(-1 / 60), '-i', str(OUTPUT),
    '-frames:v', '1', '-q:v', '2', str(STILL),
], check=True)
print('Created related-work.mp4 and related-work-final.jpg')
