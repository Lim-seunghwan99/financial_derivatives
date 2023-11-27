<template>
  <div class="container">
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <p><input type="text" v-model.trim="username" class="inputbox" /></p>
      <p><input type="password" v-model.trim="password" class="inputbox" /></p>
      <p><input type="submit" value="로그인" /></p>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password = ref(null);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style>
.inputbox {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  width: 100%;
  font-family: "JalnanGothic";
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  font-family: "JalnanGothic";
  text-align: center;
}
</style>
