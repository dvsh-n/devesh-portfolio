"""Build CFM/diffusion, FRS, and Robotarium into one publication loop."""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/pages/projects/generative-planner-safety'
OUTPUT = ROOT / 'public/projects/generative-planner-safety/assets/thumbnail.mp4'
# Match the site's fixed 8:5 frame, with a high-resolution 60 fps web encode.
FRAME = (
    'split=2[fg][back];'
    '[back]scale=640:400:force_original_aspect_ratio=increase,crop=640:400,'
    'gblur=sigma=55:steps=3,eq=brightness=-0.12:saturation=0.6,'
    'colorchannelmixer=rr=0.55:gg=0.55:bb=0.55,scale=3600:2250[bg];'
    '[fg]scale=3600:2250:force_original_aspect_ratio=decrease:force_divisible_by=2[front];'
    '[bg][front]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[out]'
)

def encode(inputs, graph, output):
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *inputs,
        '-filter_complex', graph, '-map', '[out]', '-an',
        '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
        '-video_track_timescale', '15360', str(output),
    ], check=True)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='generative-thumbnail-') as directory:
    work = Path(directory)
    print('1/3: CFM above diffusion', flush=True)
    encode([
        '-i', str(SOURCE / 'cfm_anim.mp4'),
        '-i', str(SOURCE / 'diffusion_anim.mp4'),
    ],
        '[0:v]setpts=(PTS-STARTPTS)/2,fps=60,scale=3600:1050,setsar=1[top];'
        '[1:v]setpts=(PTS-STARTPTS)/2,fps=60,setsar=1[bottom];'
        '[top][bottom]vstack=inputs=2:shortest=1,' + FRAME,
        work / '0.mp4',
    )
    print('2/3: FRS', flush=True)
    encode(['-i', str(SOURCE / 'frs__anim.mp4')],
           '[0:v]setpts=PTS-STARTPTS,fps=60,setsar=1,' + FRAME, work / '1.mp4')
    print('3/3: Robotarium (25–37 seconds)', flush=True)
    encode(['-ss', '25', '-t', '12', '-i', str(SOURCE / 'robotarium_video.mp4')],
           '[0:v]setpts=(PTS-STARTPTS)/1.5,fps=60,setsar=1,' + FRAME, work / '2.mp4')
    (work / 'clips.txt').write_text(''.join(f"file '{i}.mp4'\n" for i in range(3)))
    subprocess.run([
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
        '-f', 'concat', '-safe', '0', '-i', str(work / 'clips.txt'),
        '-c', 'copy', '-movflags', '+faststart', str(OUTPUT),
    ], check=True)
print(f'Created {OUTPUT.relative_to(ROOT)}')
