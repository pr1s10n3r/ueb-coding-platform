<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { reqFormData, reqSourceFiles } from "../stores/request";

  let reqFd = null;
  reqFormData.subscribe((value) => {
    reqFd = value;
  });

  let reqSources = null;
  reqSourceFiles.subscribe((value) => {
    reqSources = value;
  });

  let done = false;
  let results = [];

  onMount(async () => {
    reqSources.forEach(async (file) => {
      reqFd.set("file", file);

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

      let result = data;
      result.filename = file.name;
      result.input = reqFd.get("input");
      results.push(result);
    });

    done = true;
  });

  function onExportButtonPress(evt) {
    // TODO: Export results to Excel
  }
</script>

<div class="container">
  <h1>Tus Resultados</h1>

  {#if !done}
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
        {#each results as r}
          <tr class="active">
            <td>{r.filename}</td>
            <td>{r.time.actual}</td>
            <td>{r.input}</td>
            <td>{r.output.expected}</td>
            <td>{r.output.actual}</td>
            <td>{r.complexity.expected}</td>
            <td>{r.complexity.actual}</td>
          </tr>
        {/each}
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
