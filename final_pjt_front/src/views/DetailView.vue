<template class="template">
  <div v-if="article">
    <h2>{{ article.title }}</h2>
    <hr />
    <div>
      <p>
        작성일:
        {{ article.created_at.slice(0, 10) }}
        수정일: {{ article.updated_at.slice(0, 10) }}
      </p>

      <p>
        작성자:
        <span class="router-article">
          <RouterLink
            :to="{
              name: 'OtherProfileView',
              params: { username: article.username },
            }"
          >
            {{ article.username }}
          </RouterLink>
        </span>
      </p>
      <hr />
      <div class="container2">
        <h5>{{ article.content }}</h5>
      </div>
      <div class="container">
        <div
          v-if="article.username == store.userInfo.username"
          class="articleupdate"
        >
          <RouterLink
            :to="{ name: 'ArticleEditView', params: { id: article.id } }"
            ><button class="articleupdatebutton">
              게시글 수정
            </button></RouterLink
          >
          <button @click="deleteArticle(article.id)">게시글 삭제</button>
        </div>
      </div>
      <hr />
      <form @submit.prevent="createComment">
        <label for="content">내용 : </label>
        <input type="text" v-model="content" class="inputbox2" />
        <button type="submit" class="commentbotton">댓글 작성</button>
      </form>
      <hr />
      <div v-if="article.comment_set">
        <p v-for="comment in article.comment_set" :key="comment.id">
          <span class="comment-router">
            <RouterLink
              :to="{
                name: 'OtherProfileView',
                params: { username: comment.username },
              }"
              >{{ comment.username }}</RouterLink
            >
            - {{ comment.content }}
          </span>
          <button
            v-if="store.userInfo.username === comment.username"
            @click="deleteComment(comment.id)"
          >
            삭제
          </button>
        </p>
      </div>
    </div>
    <button @click="goBack">뒤로가기</button>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";
const router = useRouter();
const store = useCounterStore();
const route = useRoute();
const article = ref(null);
const content = ref("");
const comments = ref(null);
console.log(route.params);
const goBack = () => {
  router.back();
};
const createComment = () => {
  axios({
    method: "POST",
    url: `${store.API_URL}/api/comments/${route.params.id}/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      article.value.comment_set.push(res.data);
      article.value = { ...article.value };
      content.value = "";
    })
    .catch((err) => {
      console.log(err);
    });
};

const deleteComment = (commentId) => {
  axios
    .delete(
      `${store.API_URL}/api/${route.params.id}/comments/${commentId}/delete`,
      {
        headers: {
          Authorization: `Token ${store.token}`,
        },
      }
    )
    .then((response) => {
      if (response.status === 204) {
        console.log("삭제 성공");
        article.value.comment_set = article.value.comment_set.filter(
          (comment) => comment.id !== commentId
        );
      } else {
        console.log("삭제 실패.");
      }
    })
    .catch((error) => {
      console.error(error);
    });
};

const deleteArticle = () => {
  axios({
    method: "delete",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/delete/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("삭제 완료");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data);
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style>
.articleupdate > a {
  text-decoration: none;
  text-decoration-line: none;
  color: black;
  padding-right: 15px;
}

.comment-router > a {
  text-decoration: none;
  text-decoration-line: none;
  color: black;
  padding-left: 5px;
}

.router-article > a {
  text-decoration: none;
  text-decoration-line: none;
  color: black;
}
h1 {
  font-size: 52px;
  font-family: "JalnanGothic";
  margin: 30px;
}

.inputbox2 {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  width: 250px;
  font-family: "JalnanGothic";
  margin-left: 10px;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  font-family: "Diphylleia", serif;
}
.container2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 30px;
  font-family: "Diphylleia", serif;
  height: 250px;
}

.commentbotton{
  margin-left: 10px;
}
</style>
