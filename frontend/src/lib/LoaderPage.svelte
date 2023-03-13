<script>
  import { goToTabById, Headers } from "../stores/header";
  import { setFiles } from "../stores/request";

  let filesCount = 0;
  let uploadedFiles = [];
  let invalidFileDragged = false;

  function onDragEnter(evt) {
    evt.stopPropagation();
    evt.preventDefault();
  }

  function onDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
  }

  function onFileDropped(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    invalidFileDragged = false;

    const dtFiles = evt.dataTransfer.files;
    for (let i = 0; i < dtFiles.length; i++) {
      const fileName = dtFiles[i].name;

      const fileNameParts = fileName.split(".");
      if (
        fileNameParts.length > 1 &&
        fileNameParts[fileNameParts.length - 1] === "java"
      ) {
        uploadedFiles.push(dtFiles[i]);
        filesCount++;
      } else {
        invalidFileDragged = true;
        uploadedFiles = [];
        break;
      }
    }

    if (!invalidFileDragged) {
      setFiles(uploadedFiles);
    }
  }

  function onNextButtonPressed(evt) {
    evt.preventDefault();
    goToTabById(Headers.EvaluationCriteria);
  }

  function onAlertCloseButtonPress(evt) {
    evt.preventDefault();
    invalidFileDragged = false;
  }
</script>

<div class="container">
  <div class="columns">
    <div class="column col-6">
      <div
        class="empty"
        on:dragenter={onDragEnter}
        on:drop={onFileDropped}
        on:dragover={onDragOver}
      >
        {#if uploadedFiles.length === 0}
          <div class="empty-icon">
            <i class="icon icon-link" />
          </div>
          <p class="empty-title h5">Aún no has seleccionado archivos</p>
          <p class="empty-subtitle">
            Arroja archivos en esta área para subirlos.
          </p>
        {:else}
          {#each uploadedFiles as uploadedFile}
            <div>{uploadedFile.name}</div>
          {/each}
        {/if}
      </div>

      {#if invalidFileDragged}
        <div class="toast toast-error">
          <button
            on:click={onAlertCloseButtonPress}
            class="btn btn-clear float-right"
          />
          Recuerda subir únicamente archivos con extensión <b>.java</b>!
        </div>
      {/if}
    </div>

    <div class="divider-vert" />

    <div class="column col-5">
      <h4>Primero, debes subir algunos archivos.</h4>
      <p class="text-justify text-muted">
        Asegurate de subir unicamente archivos sueltos con extension <span
          class="text-bold">.java</span
        >. Para una mejor visualización de los resultados, te sugerimos poner
        nombres signifivativos a los archivos; por ejemplo el correo (sin el
        dominio) del estudiante que desarrolló el código fuente.
      </p>
      <button
        on:click={onNextButtonPressed}
        disabled={filesCount === 0}
        class="btn {filesCount > 0 ? 'btn-success' : ''}  btn-block"
        >Siguiente <i class="icon icon-arrow-right" /></button
      >
    </div>
  </div>
</div>
