<template>
  <div class="opbox">
    <div class="title">
      <div class="option-buttons">
        <button @click="selectOption('정기예금')">정기예금</button>
        <button @click="selectOption('정기적금')">정기적금</button>
      </div>
    </div>
    <div v-if="selectedOption === '정기예금'">
      <FinlifeList />
    </div>
    <div v-if="selectedOption === '정기적금'">
      <FinlifeSavingList />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useProductStore } from "@/stores/product.js";
import FinlifeList from "@/components/FinlifeList.vue";
import FinlifeSavingList from "@/components/FinlifeSavingList.vue";

const store = useProductStore();
console.log(store);
const options = ref(["정기예금", "정기적금"]);
const selectedOption = ref("정기적금");

onMounted(() => {
  store.getFinlife();
  store.getFinlife2();
});


const selectOption = (option) => {
  selectedOption.value = option;
};
</script>

<style>
.inputbox {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
}

.opbox {
  margin-top: 30px;
  font-family: "SUITE-Regular";
  font-size: 18px;
}

.option-buttons button {
  margin-right: 10px;
  padding: 5px 10px;
  cursor: pointer;
}

.option-buttons {
  justify-content: flex-start;
  display: flex;
  font-family: "JalnanGothic";
  margin-left: 50px;
}

@font-face {
  font-family: "JalnanGothic";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_231029@1.1/JalnanGothic.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "SUITE-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
}
</style>
