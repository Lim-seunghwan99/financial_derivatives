<template>
  <div class="container">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 </label>
        <input type="text" v-model.trim="title" id="title" class="inputbox" />
      </div>
      <label for="content">내용</label>
      <div>
        <textarea
          v-model.trim="content"
          id="content"
          class="textbox"
        ></textarea>
      </div>
      <input class="btn btn-primary" type="submit" value="제출" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const title = ref(null);
const content = ref(null);
const store = useCounterStore();
const router = useRouter();

const createArticle = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  font-family: "Diphylleia", serif;
  align-items: center;
}

.textbox {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  margin-top: 10px;
  width: 400px;
  height: 400px;
}
</style>
