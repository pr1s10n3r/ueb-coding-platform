<script>
  function onExportButtonPress(evt) {
    // TODO: Export results to Excel
  }
</script>

<div class="container">
  <h1>Tus Resultados</h1>
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
</div>
