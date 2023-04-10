<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { reqFormData, clearRequestData } from "../stores/request";
  import { setError } from "../stores/error";
  import { goToTabById, Headers } from "../stores/header";

  let loading = true;
  let success = [];
  let error = [];

  let reqFd = null;
  reqFormData.subscribe((value) => {
    reqFd = value;
  });

  function onQualifyOtherBatch(evt) {
    evt.preventDefault();

    // NOTE (@astagg): IMPORTANT TO CLEAR ALL VARIABLES
    clearRequestData();

    goToTabById(Headers.Loader);
  }

  async function sendToServer(formData, file) {
    const fd = formData.valueOf();
    fd.set("file", file);

    try {
      const { status, data } = await axios.post(
        `${import.meta.env.VITE_BACKEND_BASE_URL}/api/dummy/`,
        fd,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      if (status !== 200) {
        // TODO: Handle error
        console.error(`bad response from server: ${status}: ${data}`);
      } else {
        data.name = file.name;
        success.push(data);
      }
    } catch (err) {
      setError(err.message);
      goToTabById(Headers.Error);
    }
  }

  onMount(async () => {
    const reqFiles = reqFd.getAll("file");
    for (const rFile of reqFiles) {
      await sendToServer(reqFd, rFile);
    }

    loading = false;
  });
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
          <th>Salidas Esperadas</th>
          <th>Salidas Obtenidas</th>
          <th>Complejidad Esperada</th>
          <th>Complejidad Obtenida</th>
        </tr>
      </thead>
      <tbody>
        {#each success as s}
          <tr class="active">
            <td>{s.name}</td>
            <td
              class={s.time.expected === s.time.actual
                ? "text-success"
                : "text-error"}>{s.time.actual}</td
            >
            <td>{s.output.expected}</td>
            <td
              class={s.output.expected === s.output.actual
                ? "text-success"
                : "text-error"}>{s.output.actual}</td
            >
            <td>{s.complexity.expected}</td>
            <td
              class={s.complexity.expected === s.complexity.actual
                ? "text-success"
                : "text-error"}>{s.complexity.actual}</td
            >
          </tr>
        {/each}
      </tbody>
    </table>

    <div class="controls mt-2 float-right">
      <button on:click={onQualifyOtherBatch} class="btn"
        >Calificar otro lote <i class="icon icon-refresh" /></button
      >
    </div>
  {/if}
</div>
