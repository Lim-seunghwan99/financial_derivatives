<template>
  <div class="container">
    <h1>Community</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      <button class="btn btn-secondary">게시글 작성</button>
    </RouterLink>
  </div>
  <ArticleList />
</template>

<script setup>
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import ArticleList from "@/components/ArticleList.vue";

const store = useCounterStore();
onMounted(() => {
  store.getArticles();
});
</script>

<style>
.box > h1 {
  display: flex;
  justify-content: center;
  align-items: center;
}

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

.btn-secondary {
  background-color: white;
  border: 1px solid #a9a9a9;
  color: black;
}

@font-face {
  font-family: "JalnanGothic";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_231029@1.1/JalnanGothic.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
