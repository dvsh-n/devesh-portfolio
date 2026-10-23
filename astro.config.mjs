// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.deveshnath.com',
  devToolbar: { enabled: false },
  redirects: {
    '/projects/adaptive-conformal-prediction/': '/projects/faccp/',
  },
});
