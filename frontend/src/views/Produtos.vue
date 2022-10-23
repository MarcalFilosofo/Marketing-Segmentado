<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-12">
       </div>
    </div>

    <div class=" row">
      <div class="col-12">
        <tabela-produtos />
      </div>
    </div>
    <!-- <div class="mt-4 row">
      <div class="col-12">
        <projects-table />
      </div>
    </div> -->
  </div>
</template>

<script>
import TabelaProdutos from "./components/TabelaProdutos.vue";
// import ProjectsTable from "./components/ProjectsTable.vue";

export default {
  name: "tables",
  components: {
    TabelaProdutos,
    // ProjectsTable
  },
  data() {
    return {
    };
  },
};
</script>
