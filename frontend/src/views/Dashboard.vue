<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            
              <card
                :title="stats.ltv.title"
                :value="stats.ltv.value"
                :percentage="stats.ltv.percentage"
                :iconClass="stats.ltv.iconClass"
                :iconBackground="stats.ltv.iconBackground"
                :detail="stats.ltv.detail"
                directionReverse
                data-container="body" 
                data-toggle="popover" 
                data-placement="bottom" 
                data-content="TEsTE."
              ></card>

          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.churn.title"
              :value="stats.churn.value"
              :percentage="stats.churn.percentage"
              :iconClass="stats.churn.iconClass"
              :iconBackground="stats.churn.iconBackground"
              :detail="stats.churn.detail"
              directionReverse
            ></card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.nps.title"
              :value="stats.nps.value"
              :percentage="stats.nps.percentage"
              :iconClass="stats.nps.iconClass"
              :iconBackground="stats.nps.iconBackground"
              :detail="stats.nps.detail"
              directionReverse
            ></card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.mau.title"
              :value="stats.mau.value"
              :percentage="stats.mau.percentage"
              :iconClass="stats.mau.iconClass"
              :iconBackground="stats.mau.iconBackground"
              :detail="stats.mau.detail"
              directionReverse
            ></card>
          </div>
        </div>
        
        <div class="row mb-3">
          <div class="col-lg-6 mb-lg">
            <!-- line chart -->
            <div class="card z-index-2">
              <consumption-day-chart title="Horários com mais compras"/>
            </div>
          </div>

          <div class="col-lg-6 mb-lg">
            <!-- line chart -->
            <div class="card z-index-2">
              <gradient-line-chart title="Histórico do ticket médio"/>
            </div>
          </div>
        </div>

        <!-- <div class="row mb-3">
          <div class="col-lg-12 mb-lg">
            <div class="card z-index-2">
              <gradient-line-chart title="Horários com mais compras"/>
            </div>
          </div>
        </div> -->

        <!-- <div class="row">
          <div class="col-lg-12 mb-lg">
            <div class="card z-index-2">
              <active-users-chart />
            </div>
          </div>
        </div> -->

        <div class="row mb-3">
          <div class="col-lg-12 mb-lg">
            <div class="card z-index-2">
              <div class="card-title px-4 pt-2">
                <strong>
                  Mapa de vendas
                </strong>
              </div>
                <heat-map-chart />
            </div>
          </div>
        </div>

        <!-- <div class="row mt-4">
          <div class="col-lg-7 mb-lg-0 mb-4">
            <div class="card">
              <div class="p-3 pb-0 card-header">
                <div class="d-flex justify-content-between">
                  <h6 class="mb-2">Sales by Country</h6>
                </div>
              </div>
              <div class="table-responsive">
                <table class="table align-items-center">
                  <tbody>
                    <tr v-for="(sale, index) in sales" :key="index">
                      <td class="w-30">
                        <div class="px-2 py-1 d-flex align-items-center">
                          <div>
                            <img :src="sale.flag" alt="Country flag" />
                          </div>
                          <div class="ms-4">
                            <p class="mb-0 text-xs font-weight-bold">Country:</p>
                            <h6 class="mb-0 text-sm">{{ sale.country }}</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Sales:</p>
                          <h6 class="mb-0 text-sm">{{ sale.sales }}</h6>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Value:</p>
                          <h6 class="mb-0 text-sm">{{ sale.value }}</h6>
                        </div>
                      </td>
                      <td class="text-sm align-middle">
                        <div class="text-center col">
                          <p class="mb-0 text-xs font-weight-bold">Bounce:</p>
                          <h6 class="mb-0 text-sm">{{ sale.bounce }}</h6>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="col-lg-5">
            <categories-card />
          </div>
        </div> -->
      </div>
    </div>
  </div>
</template>
<script>
import Card from "@/examples/Cards/Card.vue";
import ConsumptionDayChart from "@/examples/Charts/ConsumptionDayChart.vue";
// import ConsumptionRoomChart from "@/examples/Charts/ConsumptionRoomChart.vue";
import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
import HeatMapChart from "@/examples/Charts/HeatMapChart.vue";

export default {
  name: "dashboard-default",
  methods: {
    async getKpis(){
      var myHeaders = new Headers();
      myHeaders.append("Accept", "application/json");

      var requestOptions = {
        method: 'GET',
        headers: myHeaders,
      };

      try {
        let kpis_request = await fetch("http://localhost:5000/report", requestOptions)
        let kpis_json = await kpis_request.json()

        this.stats.ltv.value = `R$ ${kpis_json.ltv}`
        this.stats.churn.value = `${kpis_json.churn}`
        this.stats.nps.value = `${kpis_json.nps}/5`
        this.stats.mau.value = `${kpis_json.mau}`
        console.log(kpis_json)
      } catch (error) {
        console.log(error)
      }
    }
  },  
  data() {
    
    return {
      stats: {
        ltv: {
          title: "LTV",
          value: "R$ 0.0",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "Quanto vale o seu cliente",
          iconBackground: "bg-gradient-primary",
        },
        churn: {
          title: "CHURN",
          value: "0",
          percentage: "",
          iconClass: "ni ni-single-02",
          detail: "Perda de clientes",
          iconBackground: "bg-gradient-primary",
        },
        mau: {
          title: "MAU",
          value: "0",
          percentage: "",
          iconClass: "ni ni-circle-08",
          detail: "Clientes ativos mensalmente",
          iconBackground: "bg-gradient-primary",
        },
        nps: {
          title: "NPS",
          value: "0",
          percentage: "",
          iconClass: "ni ni-satisfied",
          detail: "Satisfação do cliente",
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
    GradientLineChart,
    // ActiveUsersChart,
    ConsumptionDayChart,
    HeatMapChart,
    // ConsumptionRoomChart,  
    // Carousel,
    // CategoriesCard,
  },
};
</script>
