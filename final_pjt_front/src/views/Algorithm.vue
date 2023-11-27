<template>
    <h1>알고리즘</h1>
    <br>
    유저 이름 : {{ profile?.username }}
    <br>
    이메일 : {{ profile?.email }}
    <br>
    나이 : {{ profile?.age }}
    <br>
    보유금 : {{ profile?.money }}
    <br>
    월급 : {{ profile?.salary }}
    <br>
    가입상품 : {{ profile?.financial_products }}
    <br>
    <div v-for="recommendation in recommendations">
        나와 비슷한 사람이 가입한 상품 : {{ recommendation }}
    </div>
    <hr>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useProductStore } from "@/stores/product";

const store1 = useCounterStore();
const storefin = useProductStore();
const profile = ref(null);
const recommendations = ref([]);
console.log(store1.API_URL)
console.log(store1.userInfo.username)
const url = ref(`${store1.API_URL}/api/profile/${store1.userInfo.username}/`)
const url2 = ref(`${store1.API_URL}/algo/${store1.userInfo.username}/`)
console.log(url.value)
onMounted(() => {
  axios({
    method: "get",
    url: url.value,
  })
    .then((res) => {
      console.log(res.data)
      profile.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
onMounted(() => {
  axios({
    method: "get",
    url: url2.value,
  })
    .then((res) => {
      recommendations.value = res.data.recommendations
      console.log(recommendations.value)
    })
    .catch((err) => {
      console.log(err);
    });
});

</script>

<style></style>
