<script>
  import { activeTab } from "../stores/header";

  let headerActiveTab = 0;

  activeTab.subscribe((value) => {
    headerActiveTab = value;
  });
</script>

<header>
  <ul class="step">
    <li class="step-item {headerActiveTab === 0 ? 'active' : ''}">
      <a class="tooltip tooltip-bottom" data-tooltip="Paso 1"
        >Paso 1: Subir Archivos</a
      >
    </li>
    <li class="step-item {headerActiveTab === 1 ? 'active' : ''}">
      <a class="tooltip tooltip-bottom" data-tooltip="Paso 2"
        >Paso 2: Definir Criterios de Evaluación</a
      >
    </li>
    <li class="step-item {headerActiveTab === 2 ? 'active' : ''}">
      <a class="tooltip tooltip-bottom" data-tooltip="Paso 3"
        >Paso 3: Resultados</a
      >
    </li>
  </ul>
</header>

<style>
  header {
    width: 100%;
  }
</style>
