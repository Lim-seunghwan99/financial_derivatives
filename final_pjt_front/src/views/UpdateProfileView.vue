<template>
  <div class="container">
    <form @submit.prevent="updateProfile">
      <h1>프로필 수정</h1>
      <div class="container">
        <label for="name">이름</label>
        <input type="text" id="name" v-model="username" /><br />
        <label for="email">이메일</label>
        <input type="email" id="email" v-model="email" /><br />
        <label for="age">나이</label>
        <input type="number" id="age" v-model="age" /><br />
        <label for="money">보유금</label>
        <input type="number" id="money" v-model="money" /><br />
        <label for="salary">월급</label>
        <input type="number" id="salary" v-model="salary" /><br />
        <input type="submit" value="프로필 수정" />
      </div>
    </form>
  </div>
  <hr />
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const username = ref("");
const email = ref("");
const age = ref(0);
const money = ref(0);
const salary = ref(0);
onMounted(async () => {
  try {
    const response = await axios.get(
      `${store.API_URL}/api/profile/${store.userInfo.username}/`
    );
    username.value = response.data.username;
    email.value = response.data.email;
    age.value = response.data.age;
    money.value = response.data.money;
    salary.value = response.data.salary;
  } catch (error) {
    console.error(error);
  }
});

const url = ref(`${store.API_URL}/api/profile/${store.userInfo.username}/`);
const updateProfile = function () {
  axios({
    method: "patch",
    url: url.value,
    data: {
      username: username.value,
      email: email.value,
      age: age.value,
      money: money.value,
      salary: salary.value,
    },
  })
    .then((res) => {
      console.log(res.data);
      router.push({ name: "ProfileView" });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.container > input {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
}
</style>
