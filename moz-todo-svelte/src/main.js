import App from "./routes/App.svelte";

const app = new App({
  target: document.body,
  hydrate: true
});

export default app;