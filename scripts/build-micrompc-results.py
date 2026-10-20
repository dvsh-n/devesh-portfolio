"""Export the original timing figure in its final, dark, static state."""
from pathlib import Path
import importlib.util
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path.home() / 'ghost-linear/presentation/manim/experiments/numbers/video_barchart.py'
spec = importlib.util.spec_from_file_location('micrompc_barchart', SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
figure = module.load_source_module().build_figure()
module.apply_dark_theme(figure)
figure.set_facecolor('#101214')
for artist in figure.artists:
    if isinstance(artist, matplotlib.patches.PathPatch):
        artist.set_facecolor('none')
for text in figure.texts:
    # Preserve the three main group headers; simplify the smaller card titles.
    if text.get_fontsize() < 8:
        box = text.get_bbox_patch()
        if box is not None:
            text.set_color(box.get_facecolor())
            text.set_bbox(None)
# Keep the original data, logarithmic axes, and uncertainty whiskers intact.
matplotlib.rcParams['svg.fonttype'] = 'path'
output = ROOT / 'public/projects/micrompc/assets/results.svg'
output.parent.mkdir(parents=True, exist_ok=True)
figure.savefig(output, format='svg', facecolor=figure.get_facecolor(),
               metadata={'Title': 'μMPC benchmark results', 'Date': None})
plt.close(figure)
print(f'Created {output.relative_to(ROOT)}')
