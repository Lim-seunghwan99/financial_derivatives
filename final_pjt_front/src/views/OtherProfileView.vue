<template>
  <div class="userprofile">
    <h1>프로필</h1>
    <br />
    <div v-if="profile">
      <div class="userprofile">
        <p><strong>유저 이름 :</strong> {{ profile?.username }}</p>
        <br />
        <p><strong>이메일 :</strong> {{ profile?.email }}</p>
        <br />
        <p><strong>나이 :</strong> {{ profile?.age }}</p>
        <br />
        <p><strong>보유금 :</strong> {{ profile?.money }}</p>
        <br />
        <p><strong>연봉 :</strong> {{ profile?.salary }}</p>
        <br />
        <p><strong>가입상품 :</strong> {{ profile?.financial_products }}</p>
        <br />
        <br />
        <button @click="goBack">뒤로가기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useProductStore } from "@/stores/product";
import { useRoute, useRouter } from "vue-router";
const router = useRouter();
const store1 = useCounterStore();
const store2 = useProductStore();
const route = useRoute()
const profile = ref(null);
const recommendations = ref([]);
const url = ref(`${store1.API_URL}/api/profile/${route.params.username}/`);
const goBack = () => {
  router.back();
};

onMounted(() => {
  axios
    .get(url.value)
    .then((res) => {
      profile.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
});
</script>

<style>
.card-grid {
  display: flex;
  flex-wrap: nowrap;
  gap: 20px;
  /* justify-content: left; */
  width: 100%;
  justify-content: center;
}

.card {
  flex-basis: calc(25% - 50px);
  height: 300px;
  width: 200px;
}

.userprofile {
  /* font-family: "Noto Serif KR", serif; */
  /* font-family: "Diphylleia", serif; */
  font-family: "Diphylleia", serif;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.userprofile > h1 {
  margin: 20px;
}

h3 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card-link {
  text-decoration-line: none;
  color: black;
}

.card-body {
  display: flex;
  align-items: center;
  height: 150px; /* 높이를 원하는 값으로 지정 */
  width: 100%;
}
</style>
