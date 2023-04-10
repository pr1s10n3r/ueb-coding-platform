import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: '0.0.0.0',
    port: '80',
    hot: true
  },
  plugins: [svelte()],
  build: {
    outDir: path.join(path.dirname(__dirname), "backend/uebcodingplatform_app/home/static"),
    lib: {
      // Could also be a dictionary or array of multiple entry points
      entry: path.resolve(__dirname, 'src/main.js'),
      name: 'libmain',
    },  
    rollupOptions: {
      output: {
        assetFileNames: (assetInfo) => {
          var info = assetInfo.name.split(".");
          var extType = info[info.length - 1];
          if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
            extType = "imgs";
          } else if (/woff|woff2/.test(extType)) {
            extType = "css";
          }
          return `${extType}/[name][extname]`;
        },
        chunkFileNames: '[name].js',
        entryFileNames: 'js/[name].js',
      },
    },
  },
})
