<template>
  <div class="container">
    <h1>정기예금 상세</h1>
    <div v-if="finlife">
      <p>금융회사명 : {{ finlife.kor_co_nm }}</p>
      <p>금융상품명 : {{ finlife.fin_prdt_nm }}</p>
      <p>가입대상 : {{ finlife.join_member }}</p>
      <p>가입제한 : {{ finlife.join_deny }}</p>
      <p>가입방법 : {{ finlife.join_way }}</p>
      <p>우대조건 : {{ finlife.spcl_cnd }}</p>
      <p>최고한도 : {{ finlife.max_limit }}</p>
      <strong>옵션 리스트</strong>
      <hr />
      <div v-if="finlife.depositoptions_set">
        <div v-for="option in finlife.depositoptions_set">
          <p>저축금리유형 : {{ option.intr_rate_type }}</p>
          <p>저축금리유형명 : {{ option.intr_rate_type_nm }}</p>
          <p>저축기간 : {{ option.save_trm }}</p>
          <p>저축금리 : {{ option.intr_rate }}</p>
          <p>최고우대금리 : {{ option.intr_rate2 }}</p>
          <button @click="addToFinancialProducts(finlife.fin_prdt_nm)">
            상품추가
          </button>
          <hr />
        </div>
      </div>
    </div>
    <button @click="goBack" class="gobackbutton">뒤로가기</button>
  </div>
  
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useProductStore } from "@/stores/product";
import { useRoute, useRouter  } from "vue-router";

const router = useRouter();
const store = useProductStore();
const storeUser = useCounterStore();
const route = useRoute();
const finlife = ref(null);
const goBack = () => {
  router.back();
};
console.log(finlife)
let financial_products = ref("");
const url = ref(`${store.API_URL}/api/profile/${storeUser.userInfo.username}/`);
const addToFinancialProducts = (product) => {
  if (financial_products.value.includes(product)) {
    console.error(`${product} is already in financial_products.`);
    alert('이미 있는 상품입니다')
    return;
  }
  financial_products.value += product + ", ";
  axios({
    method: "patch",
    url: url.value,
    data: {
      financial_products: financial_products.value,
    },
  })
    .then((res) => {
      console.log(res.data);
      alert('상품이 추가 되었습니다')
      router.back()
    })
    .catch((err) => {
      console.log(err);
    });
};
onMounted(async () => {
  try {
    const response = await axios.get(
      `${store.API_URL}/api/profile/${storeUser.userInfo.username}/`
    );
    financial_products = ref(response.data.financial_products || "");
  } catch (error) {
    console.error(error);
  }
});

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/finlife/deposit-products/${route.params.fin_prdt_cd}/`,
  })
    .then((res) => {
      console.log(res.data);
      finlife.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  font-family: "Diphylleia", serif;
}

.container > h1 {
  font-family: "JalnanGothic";
}

button {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
}

.gobackbutton {
  align-self: flex-start; /* 왼쪽 정렬 */
  margin-top: 10px;
}

@font-face {
  font-family: "JalnanGothic";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_231029@1.1/JalnanGothic.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}


</style>
