<script>
  import { reqError } from "../stores/error";
  import { clearRequestData } from "../stores/request";
  import { goToTabById, Headers } from "../stores/header";

  let displayError = "";
  reqError.subscribe((value) => {
    displayError = value.trim();
  });

  function onBackToStart(evt) {
    evt.preventDefault();
    clearRequestData(); // Just in case
    goToTabById(Headers.Loader);
  }
</script>

<div class="container">
  <h3>¡Oh no!</h3>
  <h5>Algo ha salido mal, ¿Tal vez el sistema está caído?</h5>

  <textarea readonly class="error-display-area">
    // Envía esto a tu administrador del sistema.
    {displayError}
  </textarea>

  <button on:click={onBackToStart} class="mt-2 btn btn-primary btn-block"
    >Volver al Inicio</button
  >
</div>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap");

  .error-display-area {
    width: 100%;
    height: 200px;
    font-family: "Source Code Pro", monospace;

    resize: none;
    border: none;
    outline: none;
  }
</style>
