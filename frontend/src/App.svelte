<script>
  import Header from "./lib/Header.svelte";
  import LoaderPage from "./lib/LoaderPage.svelte";
</script>

<main>
  <Header />

  <div class="tab">
    <LoaderPage />
  </div>
</main>

<style>
  .tab {
    border: 1px solid red;
  }
</style>
