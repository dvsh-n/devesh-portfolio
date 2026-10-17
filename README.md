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
