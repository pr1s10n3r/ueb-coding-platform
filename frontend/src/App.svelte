<script>
  import Header from "./lib/Header.svelte";
  import LoaderPage from "./lib/LoaderPage.svelte";
  import EvaluationCriteriaPage from "./lib/EvaluationCriteriaPage.svelte";
  import ResultsPage from "./lib/ResultsPage.svelte";
  import Footer from "./lib/Footer.svelte";
  import ErrorPage from "./lib/ErrorPage.svelte";
  import { activeTab, Headers } from "./stores/header";

  let headerActiveTab = Headers.Loader;
  activeTab.subscribe((value) => {
    headerActiveTab = value;
  });
</script>

<main>
  <Header />

  <div class="tab-wrapper">
    <div class="tab-item">
      {#if headerActiveTab == Headers.Loader}
        <LoaderPage />
      {:else if headerActiveTab == Headers.EvaluationCriteria}
        <EvaluationCriteriaPage />
      {:else if headerActiveTab == Headers.Results}
        <ResultsPage />
      {:else if headerActiveTab == Headers.Error}
        <ErrorPage />
      {/if}
    </div>
  </div>

  <Footer />
</main>

<style>
  .tab-wrapper {
    width: 100%;
    height: calc(100vh - 110px);

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
