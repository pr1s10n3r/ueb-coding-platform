<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { reqFormData, clearRequestData } from "../stores/request";
  import { setError } from "../stores/error";
  import { goToTabById, Headers } from "../stores/header";

  let loading = true;
  let success = [];
  let error = [];
  let isComplexityExpected = true,
    isOutputExpected = true;

  let reqFd = null;
  reqFormData.subscribe((value) => {
    console.log("Request Form:", value);
    console.log("Request Form Files:", value.getAll("files"));
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
        if (isComplexityExpected && data.complexity.expected === "") {
          isComplexityExpected = false;
        }
        if (isOutputExpected && data.output.expected === "") {
          isOutputExpected = false;
        }

        data.name = file.name;
        data.output.actual = data.output.actual.trim();
        success = [...success, data];
      }
    } catch (err) {
      error = [...error, err];
      console.error(err);
      setError(err.message);
      goToTabById(Headers.Error);
    }
  }

  onMount(async () => {
    const reqFiles = reqFd.getAll("file");
    console.log(`Request Files: ${reqFiles.length}`);
    for (const rFile of reqFiles) {
      console.log("Sending to server...");
      await sendToServer(reqFd, rFile);
    }
    loading = false;
  });
</script>

<div class="container">
  <h1>Tus Resultados</h1>

  {#if success.length === 0}
    <p>Estamos cargando...</p>
  {:else}
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>Código Evaluado</th>
          <th>Tiempo de Ejecución</th>
          {#if isOutputExpected}
            <th>Salidas Esperadas</th>
          {/if}
          <th>Salidas Obtenidas</th>
          {#if isComplexityExpected}
            <th>Complejidad Esperada</th>
            <th>Complejidad Obtenida</th>
          {/if}
        </tr>
      </thead>
      <tbody>
        {#each success as s}
          <tr class="active">
            <td>{s.name}</td>
            <td
              class={s.time.expected > 0 &&
              s.time.actual / 1000 > s.time.expected
                ? "text-error"
                : "text-success"}>{s.time.actual / 1000}s</td
            >
            {#if isOutputExpected}
              <td>{s.output.expected}</td>
            {/if}
            <td
              class={isOutputExpected &&
              s.output.expected !== "" &&
              s.output.expected === s.output.actual
                ? "text-success"
                : "text-error"}>{s.output.actual}</td
            >
            {#if isComplexityExpected}
              <td>{s.complexity.expected}</td>
              <td
                class={s.complexity.expected !== "" &&
                s.complexity.expected === s.complexity.actual
                  ? "text-success"
                  : "text-error"}>{s.complexity.actual}</td
              >
            {/if}
          </tr>
        {/each}
      </tbody>
    </table>

    {#if loading}
      <div class="loading loading-lg" />
    {/if}

    <div class="controls mt-2 float-right">
      <button on:click={onQualifyOtherBatch} class="btn"
        >Calificar otro lote <i class="icon icon-refresh" /></button
      >
    </div>
  {/if}
</div>
