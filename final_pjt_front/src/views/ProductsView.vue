<template>
  <div>
    <ul v-if="products.length">
      <li v-for="product in products" :key="product.fin_prdt_cd">
        {{ product.fin_prdt_cd }} - {{ product.kor_co_nm }}
        <!-- 필요한 다른 속성도 같이 출력 가능 -->
      </li>
    </ul>
    <p v-else>No products available</p>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const products = ref([]); // 불러온 데이터를 저장할 ref

onMounted(async () => {
  try {
    const apiKey = import.meta.env.VUE_APP_API_KEY; // .env 파일에서 API 키 가져오기
    const response = await axios.get("YOUR_API_ENDPOINT", {
      headers: {
        Authorization: `Bearer ${apiKey}`, // API 키를 헤더에 추가
      },
    });
    products.value = response.data; // 가져온 데이터를 products ref에 할당
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});
</script>
