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

- `src/pages/index.astro`: introduction, About, Education, and page styles. The profile photo is intentionally blank.
- `src/data/publications.ts`: publication metadata, paper/video URLs, and optional image/video media. Replace `paperUrl` and `videoUrl` values of `#` when links are ready. Set `media` to `{ src: '/media/example.mp4', type: 'video' }` or `{ src: '/media/example.jpg', type: 'image' }`, with assets in `public/media/`.
- `src/pages/projects/`: five separate, intentionally blank dark project pages, linked from the Website buttons.
- `public/Resume.pdf`: downloadable résumé.
