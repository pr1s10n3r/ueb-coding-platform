<script>
  import { goToTabById, Headers } from "../stores/header";

  function onSubmitEvaluationCriteria(evt) {
    evt.preventDefault();

    // TODO: Send evaluation criteria to server

    goToTabById(Headers.Results);
  }
</script>

<div class="container">
  <div class="columns">
    <div class="column col-6">
      <form>
        <div class="form-group">
          <label class="form-label" for="input-example-1"
            >Tiempo de Ejecución Máximo <span
              class="form-hint tooltip"
              data-tooltip="Unidad en segundos.">(?)</span
            ></label
          >
          <input
            class="form-input"
            type="number"
            id="input-example-1"
            placeholder="En segundos"
            min="1"
            value="1"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-example-3"
            >Entradas del Programa <span
              class="form-hint tooltip"
              data-tooltip="Serán enviadas al stdin del sistema.">(?)</span
            ></label
          >
          <textarea
            class="form-input"
            id="input-example-3"
            placeholder="10 8 5 54 1 2 7 87"
            rows="2"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-example-3"
            >Salida Deseada del Programa</label
          >
          <textarea
            class="form-input"
            id="input-example-3"
            placeholder="1 2 5 7 8 10 54 87"
            rows="2"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-example-1"
            >Nombre de Función a Evaluar <span
              class="form-hint tooltip"
              data-tooltip="Únicamente el nombre, no la firma.">(?)</span
            ></label
          >
          <input
            class="form-input"
            type="text"
            id="input-example-1"
            placeholder="quickSort"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-example-1"
            >Complejidad Algorítmica Deseada para la Función a Evaluar</label
          >
          <select class="form-select">
            <option>O(1)</option>
            <option>O(n)</option>
            <option>O(n^2)</option>
            <option>O(log n)</option>
            <option>O(n log n)</option>
          </select>
        </div>
      </form>
    </div>

    <div class="divider-vert" />

    <div class="column col-5">
      <h4>Segundo, Define los Criterios de Evaluación</h4>
      <p>
        Ahora debes definir los criterios de evaluación que se aplicarán sobre
        los archivos cargados. En estos criterios puedes calificar aspectos
        como:
      </p>

      <ul>
        <li>
          Tiempo de ejecución máximo permitido <span class="text-bold"
            >en segundos</span
          >.
        </li>
        <li>Salidas deseadas de un programa dado unas entradas.</li>
        <li>Complejidad algorítimica de una función dada su firma.</li>
      </ul>

      <button
        on:click={onSubmitEvaluationCriteria}
        class="btn btn-success btn-block"
        >Siguiente <i class="icon icon-arrow-right" /></button
      >
    </div>
  </div>
</div>

<style>
  .form-hint {
    font-weight: bold;
    cursor: pointer;
  }
</style>
