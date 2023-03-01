<script>
  import Header from "./lib/Header.svelte";
  import LoaderPage from "./lib/LoaderPage.svelte";
</script>

<main>
  <Header />

  <div class="tab-wrapper">
    <div class="tab-item">
      <LoaderPage />
    </div>
  </div>
</main>

<style>
  .tab-wrapper {
    width: 100%;
    height: calc(100vh - 61px);

    display: flex;
    align-items: center;
    justify-content: center;
  }

  .tab-item {
    max-width: 60%;
  }

  @media screen and (max-width: 1000px) {
    .tab-item {
      max-width: 90%;
    }
  }

  @media screen and (max-width: 740px) {
    .tab-item {
      max-width: 100%;
    }
  }
</style>
