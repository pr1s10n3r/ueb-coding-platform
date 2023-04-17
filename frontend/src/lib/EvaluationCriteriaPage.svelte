<script>
  import { goToTabById, Headers } from "../stores/header";
  import { setEvaluationCriteria } from "../stores/request";

  let expectedTimeField = 0,
    inputFormField = "",
    expectedOutputField = "",
    funcName = "",
    funcExpectedComplexity = "";

  function onSubmitEvaluationCriteria(evt) {
    evt.preventDefault();

    setEvaluationCriteria(
      inputFormField,
      expectedOutputField.trim(),
      funcExpectedComplexity,
      expectedTimeField,
      funcName
    );

    goToTabById(Headers.Results);
  }
</script>

<div class="container">
  <div class="columns">
    <div class="column col-6">
      <form>
        <div class="form-group">
          <label class="form-label" for="input-expected-runtime"
            >Tiempo de Ejecución Máximo <span
              class="form-hint tooltip"
              data-tooltip="Unidad en segundos.">(?)</span
            ></label
          >
          <input
            bind:value={expectedTimeField}
            class="form-input"
            type="number"
            id="input-expected-runtime"
            placeholder="En segundos"
            min="0"
          />
          <p class="text-muted">
            Si es cero, no se evaluará el tiempo de ejecución.
          </p>
        </div>

        <div class="form-group">
          <label class="form-label" for="input-stdin-input"
            >Entradas del Programa <span
              class="form-hint tooltip"
              data-tooltip="Serán enviadas al stdin del sistema.">(?)</span
            ></label
          >
          <textarea
            bind:value={inputFormField}
            class="form-input"
            id="input-stdin-input"
            placeholder="10 8 5 54 1 2 7 87"
            rows="2"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-expected-output"
            >Salida Deseada del Programa</label
          >
          <textarea
            bind:value={expectedOutputField}
            class="form-input"
            id="input-expected-output"
            placeholder="1 2 5 7 8 10 54 87"
            rows="2"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-func-name"
            >Nombre de Función a Evaluar <span
              class="form-hint tooltip"
              data-tooltip="Únicamente el nombre, no la firma.">(?)</span
            ></label
          >
          <input
            bind:value={funcName}
            class="form-input"
            type="text"
            id="input-func-name"
            placeholder="quickSort"
          />
        </div>

        <div class="form-group">
          <label class="form-label" for="input-expected-complexity"
            >Complejidad Algorítmica Deseada para la Función a Evaluar</label
          >
          <select
            id="input-expected-complexity"
            class="form-select"
            bind:value={funcExpectedComplexity}
            disabled={funcName === ""}
          >
            <option value="constant">O(1)</option>
            <option value="linear">O(n)</option>
            <option value="quadratic">O(n^2)</option>
            <option value="linearithmic">O(n log n)</option>
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

      <p>
        Si un parámetro no es establecido, no se tomará en cuenta durante el
        proceso de evaluación.
      </p>

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
