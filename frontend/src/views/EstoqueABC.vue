<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-4 col-12">
            
              <card
                title="Classe A"
                :value="stats.a.value"
                :percentage="stats.a.percentage"
                :iconClass="stats.a.iconClass"
                iconBackground="bg-gradient-primary"
                detail="Movimenta 80% do estoque"
                directionReverse
                data-container="body" 
                data-toggle="popover" 
                data-placement="bottom" 
                data-content="TEsTE."
              ></card>

          </div>
          <div class="col-lg-4 col-md-6 col-12">
            <card
              title="Classe B"
              :value="stats.b.value"
              :percentage="stats.b.percentage"
              :iconClass="stats.b.iconClass"
              iconBackground="bg-gradient-primary"
              detail="Movimenta 15% do estoque"
              directionReverse
            ></card>
          </div>
          <div class="col-lg-4 col-md-6 col-12">
            <card
              title="Classe C"
              :value="stats.c.value"
              :percentage="stats.c.percentage"
              :iconClass="stats.c.iconClass"
              iconBackground="bg-gradient-primary"
              detail="Movimenta 5% do estoque"
              directionReverse
            ></card>
          </div>
        </div>
        
        <div class="row mb-3">
          <div class="col-12 mb-lg">
            <!-- line chart -->
            <div class="card z-index-2">
              <gradient-line-chart-abc title="Quantidade de pedidos por classe de produto"/>
            </div>
          </div>
        </div>
      
      </div>
    </div>
    <div class="card">
      <div class="card-header pb-0">
        <h6>Lista de produtos</h6>
      </div>
      <div class="card-body px-0 pt-0 pb-2">
        <div class="table-responsive p-0">
          <table class="table align-items-center mb-0">
            <thead>
              <tr>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Produto</th>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Número de pedidos</th>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Classe</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="p in this.products" :key="p.id">
                <td>
                  <div class="d-flex px-2 py-1">
                    <div>
                    </div>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">{{ p.post_title }}</h6>
                    </div>
                  </div>
                </td>
                <td>
                  <p class="text-xs font-weight-bold mb-0">{{ p.qt }}</p>
                </td>
                <td>
                  <p class="text-xs font-weight-bold mb-0">{{ p.classe }}</p>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
import Card from "@/examples/Cards/Card.vue";
// import ConsumptionRoomChart from "@/examples/Charts/ConsumptionRoomChart.vue";
import GradientLineChartAbc from "@/examples/Charts/GradientLineChartAbc.vue";

export default {
  name: "estoque-abc",
  methods: {
    async getKpis(){
      var myHeaders = new Headers();
      myHeaders.append("Accept", "application/json");

      var requestOptions = {
        method: 'GET',
        headers: myHeaders,
      };

      try {
        let kpis_request = await fetch("http://localhost:5000/estoque-abc", requestOptions)
        let kpis_json = await kpis_request.json()
        this.stats.a.value = `${kpis_json.total_prod_a} produtos`
        this.stats.b.value = `${kpis_json.total_prod_b} produtos`
        this.stats.c.value = `${kpis_json.total_prod_c} produtos`
        this.products = kpis_json.produtos
        console.log(kpis_json)
      } catch (error) {
        console.log(error)
      }
    }
  },  
  data() {
    
    return {
      products: [],
      stats: {
        a: {
          title: "LTV",
          value: "0",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "Quanto vale o seu cliente",
          iconBackground: "bg-gradient-primary",
        },
        b: {
          title: "CHURN",
          value: "0",
          percentage: "",
          iconClass: "ni ni-single-02",
          detail: "Perda de clientes",
          iconBackground: "bg-gradient-primary",
        },
        c: {
          title: "MAU",
          value: "0",
          percentage: "",
          iconClass: "ni ni-circle-08",
          detail: "Clientes ativos mensalmente",
          iconBackground: "bg-gradient-primary",
        },
      },
      
    };
  },
  mounted(){
    this.getKpis()
  },
  components: {
    Card,
    GradientLineChartAbc,
  },
};
</script>
