<template>
  <div class="container">
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model="editedArticle.title" />
      </div>
      <label for="content">내용 : </label>
      <div>
        <textarea v-model="editedArticle.content" class="textbox"></textarea>
      </div>
      <input type="submit" value="게시글 수정" />
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const editedArticle = ref({
  title: "",
  content: "",
});

onMounted(async () => {
  try {
    const response = await axios.get(
      `${store.API_URL}/api/v1/articles/${route.params.id}/`
    );
    editedArticle.value = response.data;
  } catch (error) {
    console.error(error);
  }
});

const updateArticle = () => {
  axios({
    method: "PUT",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      title: editedArticle.value.title,
      content: editedArticle.value.content,
    },
  })
    .then(() => {
      console.log("게시글 수정 완료");
      router.push({ name: "DetailView" });
    })
    .catch((err) => {
      console.error("게시글 수정 실패", err);
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
