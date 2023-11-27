<template>
  <div class="container">
    <h1>Signup</h1>
    <form @submit.prevent="signup">
      username <input type="text" v-model.trim="username" />
      <br />
      password <input type="password" v-model.trim="password1" />
      <br />
      password2 <input type="password" v-model.trim="password2" />
      <br />
      email <input type="text" v-model.trim="email" />
      <br />
      Age <input type="number" v-model.number="age" />
      <br />
      Money <input type="number" v-model.nubmer="money" />
      <br />
      Salary <input type="number" v-model.number="salary" />
      <br />
      <input type="submit" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const age = ref(0);
const money = ref(0);
const salary = ref(0);
const financialProducts = ref([]);

const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };

  if (email.value !== null && email.value !== "") {
    payload.email = email.value;
  }
  if (age.value !== null && age.value !== "") {
    payload.age = Number(age.value);
  }
  if (money.value !== null && money.value !== "") {
    payload.money = parseInt(money.value);
    console.log(payload.money);
  }
  if (salary.value !== null && salary.value !== "") {
    payload.salary = Number(salary.value);
  }
  // if (financialProducts.value !== null && financialProducts.value !== "") {
  //   payload.financial_products = financialProducts.value;
  // }
  console.log(payload);
  store.signup(payload);
};
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  font-family: "JalnanGothic";
}

.container input {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  width: 100%;
  font-family: "JalnanGothic";
}
</style>
