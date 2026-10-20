"""Join the method chapters and remove the second chapter's opening hold."""
from pathlib import Path
import subprocess
import tempfile
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / 'ghost-linear/presentation/manim/grouped_videos'
OUTPUT = ROOT / 'src/pages/projects/micrompc/method_videos'
GROUPS = [
    ('01-latent-rollout', ['2.1_latent_dynamics', '2.2_given_control_sequence', '2.3_condensed_rollout', '2.4_state_and_output_maps', '2.5_precomputed_linear_map_visual']),
    ('02-condensed-program', ['2.6_full_quadratic_program', '2.7_condensed_cost', '2.8_h_and_g_pulse', '2.9_condensed_constraint']),
    ('03-primal-dual-solver', ['2.10_primal_dual_equations', '2.11_frozen_inverse', '2.12_primal_dual_iterations']),
]

OUTPUT.mkdir(parents=True, exist_ok=True)
for name, clips in GROUPS:
    with tempfile.TemporaryDirectory() as temporary:
        manifest = Path(temporary) / 'clips.txt'
        paths = [SOURCE / f'{clip}.mp4' for clip in clips]
        for path in paths:
            if not path.is_file():
                raise FileNotFoundError(path)
        manifest.write_text(''.join(f"file '{path}'\n" for path in paths))
        # The second group holds the previous diagram for 90 frames before
        # the output equation starts moving. Cut precisely at that boundary.
        encoding = ([
            '-vf', 'trim=start_frame=90,setpts=PTS-STARTPTS',
            '-c:v', 'libx264', '-crf', '18', '-preset', 'fast',
        ] if name == '02-condensed-program' else ['-c:v', 'copy'])
        subprocess.run([
            'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
            '-f', 'concat', '-safe', '0', '-i', str(manifest),
            '-map', '0:v:0', *encoding, '-an', '-movflags', '+faststart',
            str(OUTPUT / f'{name}.mp4'),
        ], check=True)
    print(f'Created {name}.mp4')
