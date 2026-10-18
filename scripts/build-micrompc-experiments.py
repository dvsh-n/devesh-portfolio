"""Edit the original experiments section, enlarge comparisons, and play at 2x."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'src/pages/projects/micrompc'
OUTPUT = PROJECT / 'experiments.mp4'
TEMP = PROJECT / 'experiments-building.mp4'

# Times are relative to the section beginning at 2:06 in the original.
rope = 'between(t,50.733333,60.066667)'
cube = 'gte(t,60.266667)'
filters = (
    '[0:v]setpts=PTS-STARTPTS,split=3[base][rope][cube];'
    '[base]crop=3232:1740:304:360,setsar=1,'
    f"drawbox=x=0:y=0:w=iw:h=1490:color=black:t=fill:enable='{rope}',"
    f"drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill:enable='{cube}'[canvas];"
    '[rope]crop=1792:896:1024:600,scale=2800:1400:flags=lanczos[ropebig];'
    '[cube]crop=1920:960:960:568,scale=2800:1400:flags=lanczos[cubebig];'
    f"[canvas][ropebig]overlay=216:10:enable='{rope}'[r];"
    f"[r][cubebig]overlay=216:10:enable='{cube}'[c];"
    '[1:v]crop=1920:220:64:252,scale=2120:-2:flags=lanczos[caption];'
    f"[c][caption]overlay=(W-w)/2:1490:enable='{cube}',"
    'setpts=0.5*PTS,setsar=1,format=yuv420p[out]'
)
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
    '-ss', '126', '-t', '66', '-i', str(PROJECT / 'muMPC_orig.mp4'),
    '-i', str(PROJECT / 'assets/hardware-cube-caption.png'),
    '-filter_complex', filters, '-map', '[out]', '-map', '0:a:0',
    '-r', '60', '-c:v', 'libx264', '-crf', '14', '-preset', 'medium',
    '-af', 'atempo=2', '-c:a', 'aac', '-b:a', '192k',
    '-movflags', '+faststart', str(TEMP),
], check=True)
TEMP.replace(OUTPUT)
print(f'Created {OUTPUT.relative_to(ROOT)}')
