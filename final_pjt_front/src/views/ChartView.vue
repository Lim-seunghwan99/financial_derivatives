<template>
  <!-- <div class="chart-container"> -->
  <div class="div-chart">
    <Bar v-if="loaded" :data="chartData" :style="{position: 'relative', height: '800px', width: '80%' }"/>
    <button @click="goBack" class="goBackbutton">뒤로가기</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
import { useCounterStore } from "@/stores/counter";
import { useProductStore } from "@/stores/product";
import { useRoute, useRouter  } from "vue-router";

const router = useRouter();
const goBack = () => {
  router.back();
};

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);
const store1 = useCounterStore();
const store2 = useProductStore();

const loaded = ref(false);
const chartData = ref({
  labels: [],
  datasets: [
    {
      label: "기본 금리",
      backgroundColor: "skyblue",
      data: [],
    },
    {
      label: "우대 금리",
      backgroundColor: "lightgreen",
      data: [],
    },
  ],
});

const fetchData = async () => {
  loaded.value = false;

  try {
    const apiUrl = `${store1.API_URL}/api/profile/${store1.userInfo.username}/`;
    const response = await fetch(apiUrl);
    const profileData = await response.json();
    const dataValues = profileData.financial_products.split(',');

    // Remove empty strings from dataValues
    const filteredDataValues = dataValues.filter(value => value.trim() !== '');

    const basicValues = filteredDataValues.map((product) => {
      const matchingProduct = store2.finlifes.find((item) => item.fin_prdt_nm === product);
      if (matchingProduct) {
        const maxInterest = Math.max(...matchingProduct.depositoptions_set.map((option) => option.intr_rate));
        const maxInterest4 = Math.max(...matchingProduct.depositoptions_set.map((option) => option.intr_rate2));
        console.log(maxInterest)
        console.log(maxInterest4)
        return [maxInterest, maxInterest4];
      } else {
        const matchingProduct4 = store2.finlifes2.find((item) => item.fin_prdt_nm === product);
        if (matchingProduct4) {
          const maxInterest = Math.max(...matchingProduct4.savingoptions_set.map((option) => option.intr_rate));
          const maxInterest4 = Math.max(...matchingProduct4.savingoptions_set.map((option) => option.intr_rate2));
          console.log(maxInterest)
          console.log(maxInterest4)
          return [maxInterest, maxInterest4];
        }
      }
      return [0, 0];
    });
    console.log(filteredDataValues)
    console.log(basicValues)

    chartData.value.labels = filteredDataValues;

    // Extracting basic and upper values separately
    const basicDataSet = basicValues.map(([basicValue]) => basicValue);
    const upperDataSet = basicValues.map(([, upperValue]) => upperValue);

    chartData.value.datasets[0].data = basicDataSet;
    chartData.value.datasets[1].data = upperDataSet;

    loaded.value = true;
  } catch (e) {
    console.error(e);
  }
};

onMounted(() => {
  fetchData();
  store2.getFinlife3();
  store2.getFinlife4();
});

</script>

<style scoped>
.div-chart {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.goBackbutton {
  margin-top: 10px;
  align-self: flex-start;
}

</style>

