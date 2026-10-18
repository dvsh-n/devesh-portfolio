# Devesh Nath

Dark academic portfolio built with Astro. Layout inspired by https://www.rpunamiya.dev/.

## Development

```sh
npm install
npm run astro -- dev --background
```

Open http://localhost:4321. Manage the background server with:

```sh
npm run astro -- dev status
npm run astro -- dev logs
npm run astro -- dev stop
```

## Build

```sh
npm run build
```

## Content

- `src/pages/index.astro`: introduction, About, Education, and page styles. The profile photo is stored at `public/images/me.jpeg`, with its face crop set in the page styles.
- `src/data/publications.ts`: publication metadata, paper/video URLs, and optional image/video media. Replace `paperUrl` and `videoUrl` values of `#` when links are ready. Set `media` to `{ src: '/media/example.mp4', type: 'video' }` or `{ src: '/media/example.jpg', type: 'image' }`, with assets in `public/media/`.
- `src/pages/projects/<slug>/index.astro`: each project’s page in its own folder.
- `public/projects/<slug>/assets/`: each project’s videos, images, and PDFs. A file such as `public/projects/micrompc/assets/demo.mp4` is served at `/projects/micrompc/assets/demo.mp4`. Use that URL in a `<video src="...">` or in a publication’s `media.src`.
- `public/Resume.pdf`: downloadable résumé.

## Pixels to Proofs thumbnail

Source clips live in `src/pages/projects/pixels-to-proofs/`. The three `*_robust.mp4` clips are cropped to the top 512 pixels, retaining their colored borders and excluding the reachable-set plots.

Run `python3 scripts/build-pixels-thumbnail.py` (requires ffmpeg) to rebuild `public/projects/pixels-to-proofs/assets/thumbnail.mp4`. The loop plays nominal Reacher/Cube/Rope, robust Reacher/Cube/Rope, PushT, and finally hardware rope. The thumbnail is encoded at 2080 × 1300, 60 fps, H.264 CRF 16 to retain source resolution and frame rates. It is a single looping video in a fixed 8:5 frame, with a dim, blurred version of each clip filling the unused space while preserving the full video. Clip transitions are encoded into the file, so playback never swaps sources.

## Koopman Reachability thumbnail

The original animation is `src/pages/projects/koopman-reachability/thumbnail.mp4`. Run `python3 scripts/build-koopman-thumbnail.py` to rebuild the public thumbnail. It removes unused black margins with a fixed crop that retains all animation elements, preserves native foreground resolution at 60 fps, and fills the 8:5 frame with the same dim, heavily blurred backdrop used for Pixels to Proofs.

## μMPC thumbnail

Run `python3 scripts/build-micrompc-thumbnail.py` to frame `src/pages/projects/micrompc/experiments.mp4` as `public/projects/micrompc/assets/thumbnail.mp4`. The experiments clip covers 2:06–3:12 of the original (skipping the first 11 seconds of the experiments section), cropped to 3232 × 1740. The clip plays at normal speed (about 66 seconds, 30 fps), retaining every original video frame. The thumbnail adds a one-second hold on the final frame before looping. The silent loop preserves the cropped clip at native resolution, with the shared dim blurred background filling the fixed 8:5 frame.

To rebuild the edited experiments clip from the temporary original, run `python3 scripts/build-micrompc-experiments.py` before rebuilding the thumbnail. The rope and hardware cube comparisons are enlarged; the cube caption is replaced with the generated asset in `src/pages/projects/micrompc/assets/`. Its generation prompt is saved beside it.

## Generative Planner Safety thumbnail

Run `python3 scripts/build-generative-thumbnail.py` to rebuild the publication loop: CFM stacked above diffusion at 2× speed (5 seconds), FRS at normal speed (5.05 seconds), then Robotarium’s 25–37 second excerpt at 1.5× speed (8 seconds). The fixed 8:5 video uses the shared blurred fill, H.264 CRF 16, 3600 × 2250 at 60 fps. The 6000-pixel FRS source is fitted to this web frame; diffusion is sampled from 100 to 60 fps. Original source files are preserved.

## Adaptive Conformal Prediction thumbnail

Run `python3 scripts/build-adaptive-thumbnail.py` to frame `src/pages/projects/adaptive-conformal-prediction/FacCp.mp4` as the publication thumbnail. The full animation retains its native 3840 × 2160 foreground and 60 fps in the shared 8:5 frame with blurred fill.
