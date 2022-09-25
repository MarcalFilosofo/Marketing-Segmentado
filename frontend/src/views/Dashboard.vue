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
            ></card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.cac.title"
              :value="stats.cac.value"
              :percentage="stats.cac.percentage"
              :iconClass="stats.cac.iconClass"
              :iconBackground="stats.cac.iconBackground"
              :detail="stats.cac.detail"
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
        <div class="row">
          <div class="col-lg-12 mb-lg">
            <!-- line chart -->
            <div class="card z-index-2">
              <gradient-line-chart />
            </div>
          </div>
        </div>
        <div class="row mt-4">
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
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Card from "@/examples/Cards/Card.vue";
import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
// import Carousel from "./components/Carousel.vue";
import CategoriesCard from "./components/CategoriesCard.vue";

import US from "@/assets/img/icons/flags/US.png";
import DE from "@/assets/img/icons/flags/DE.png";
import GB from "@/assets/img/icons/flags/GB.png";
import BR from "@/assets/img/icons/flags/BR.png";

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
        this.stats.cac.value = `R$ ${kpis_json.cac}`
        this.stats.nps.value = `${kpis_json.nps}`
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
          detail: "Lifetime value",
          iconBackground: "bg-gradient-primary",
        },
        cac: {
          title: "CAC",
          value: "R$ 0.0",
          percentage: "",
          iconClass: "ni ni-single-02",
          detail: "Cost of Acquisition Customer",
          iconBackground: "bg-gradient-primary",
        },
        mau: {
          title: "MAU",
          value: "0",
          percentage: "",
          iconClass: "ni ni-circle-08",
          detail: "Monthly Active Users",
          iconBackground: "bg-gradient-primary",
        },
        nps: {
          title: "NPS",
          value: "0",
          percentage: "",
          iconClass: "ni ni-satisfied",
          detail: "Net Promoter Score",
          iconBackground: "bg-gradient-primary",
        },
      },
      sales: {
        us: {
          country: "United States",
          sales: 2500,
          value: "$230,900",
          bounce: "29.9%",
          flag: US,
        },
        germany: {
          country: "Germany",
          sales: "3.900",
          value: "$440,000",
          bounce: "40.22%",
          flag: DE,
        },
        britain: {
          country: "Great Britain",
          sales: "1.400",
          value: "$190,700",
          bounce: "23.44%",
          flag: GB,
        },
        brasil: {
          country: "Brasil",
          sales: "562",
          value: "$143,960",
          bounce: "32.14%",
          flag: BR,
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
    // Carousel,
    CategoriesCard,
  },
};
</script>
