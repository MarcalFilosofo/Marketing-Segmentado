<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6>Análise de produtos</h6>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Produto</th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Preço atual</th>
              <th
                class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2"
              >Número de pedidos</th>
              <th
                class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2"
              >Taxa de recompra</th>
              <th
                class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >NPS</th>
              <th
                class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >Situção do estoque</th>
              <th
                class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >Classificação inteligente</th>
              <th
                class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >Rating</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in products" :key="p.id">
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
                <p class="text-xs font-weight-bold mb-0">{{ p.current_price }}</p>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">{{ p.qt_orders }}</p>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">{{ p.repurchase }}%</p>
              </td>
              <td class="align-middle text-center text-sm">
                <span class="badge badge-sm " :class="p.nps >= 4 ? 'bg-gradient-success' : 'bg-gradient-danger' ">{{ p.nps }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold badge badge-sm" :class="p.stock_status == 1 ? 'bg-gradient-success' : 'bg-gradient-danger' ">
                  {{ p.stock_status == 1 ? 'Disponível' : 'Indisponível' }} <small>({{ p.stock_quantity }})</small>
                </span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ p.K_classes }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ p.rating }}</span>
              </td>
            
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "tabela-produtos",
  data() {
    return {
      products: []
    }
  },

  async mounted(){
    var myHeaders = new Headers();
    myHeaders.append("Accept", "application/json");

    let requestOptions = {
      method: 'GET',
      headers: myHeaders,
    }

    let response = await fetch('http://localhost:5000/products-kpis', requestOptions)
    let products = await response.json()
    console.log("Produtos KPI", products)
     
    products = products.map((p) => {
      if(p.repurchase < 30){
        p.repurchase_class = 'bg-gradient-danger'
      } else if(p.repurchase >= 30 && p.repurchase < 60){
        p.repurchase_class = 'bg-gradient-orange'
      } else if(p.repurchase >= 60 && p.repurchase < 70){
        p.repurchase_class = 'bg-gradient-warning'
      } else if(p.repurchase >= 70){
        p.repurchase_class = 'bg-gradient-success'
      }

      return p
    })
    this.products = products


  },

};
</script>
