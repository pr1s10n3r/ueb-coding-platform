<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { reqFormData } from "../stores/request";
  import { setError } from "../stores/error";
  import { goToTabById, Headers } from "../stores/header";

  let loading = true;

  let reqFd = null;
  reqFormData.subscribe((value) => {
    reqFd = value;
  });

  onMount(async () => {
    try {
      const { status, data } = await axios.post(
        `${import.meta.env.VITE_BACKEND_BASE_URL}/api/dummy/`,
        reqFd,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      if (status !== 200) {
        // TODO: Handle error
        console.error(`bad response from server: ${status}: ${data}`);
      }
    } catch (err) {
      setError(err.message);
      goToTabById(Headers.Error);
    }
  });

  function onExportButtonPress(evt) {
    // TODO: Export results to Excel
  }
</script>

<div class="container">
  <h1>Tus Resultados</h1>

  {#if loading}
    <p>Estamos cargando...</p>
  {:else}
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>Código Evaluado</th>
          <th>Tiempo de Ejecución</th>
          <th>Entradas</th>
          <th>Salidas Esperadas</th>
          <th>Salidas Obtenidas</th>
          <th>Complejidad Esperada</th>
          <th>Complejidad Obtenida</th>
        </tr>
      </thead>
      <tbody>
        <tr class="active">
          <td>Quicksort.java</td>
          <td>0.02s</td>
          <td>10 8 5 54 1 2 7 87</td>
          <td>1 2 5 7 8 10 54 87</td>
          <td>1 2 5 7 8 10 54 87</td>
          <td>O(log n)</td>
          <td>O(log n)</td>
        </tr>
      </tbody>
    </table>

    <div class="controls mt-2 float-right">
      <button on:click={onExportButtonPress} class="btn"
        >Calificar otro lote <i class="icon icon-refresh" /></button
      >

      <button on:click={onExportButtonPress} class="btn btn-success"
        >Exportar a Excel <i class="icon icon-download" /></button
      >
    </div>
  {/if}
</div>
