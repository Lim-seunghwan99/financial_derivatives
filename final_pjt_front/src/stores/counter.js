import { ref, computed, watch } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import axios from "axios";

// const OMDB_API_KEY = process.env.OMDB_API_KEY

export const useCounterStore = defineStore(
  "counter",
  () => {
    const router = useRouter();
    const articles = ref([]);
    const finlifes = ref([]);
    const mapview = ref([]);
    const profile = ref("");
    const userInfo = ref("");
    const API_URL = "http://127.0.0.1:8000";
    const API_KEY = import.meta.env.VITE_APP_API_KEY
    const token = ref(null);
    const isAuthenticated = ref(false);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });
    watch(token, () => {
      isAuthenticated.value = token.value === null ? false : true;
    });

    // DRF에 article 조회 요청을 보내는 action
    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res);
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getUserInfo = () => {
      axios({
        method: "GET",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((response) => {
          userInfo.value = response.data;
          console.log(userInfo);
        })
        .catch((err) => console.log(err.response));
    };

    const getMap = function () {
      axios({
        method: "get",
        url: `${API_URL}/maps/`,
      })
        .then((res) => {
          mapview.value = res.data;
          console.log(mapview.value);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const signup = function (payload) {
      const { username, password1, password2, email, age, money, salary } =
        payload;
      console.log(payload);
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          email,
          age,
          money,
          salary,
          // financial_products
          // 사인업 axios에러 여기 수정해야함
        },
      })
        .then((res) => {
          console.log(res);
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const logIn = function (payload) {
      const { username, password } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          console.log(res.config.data);
          console.log(token);
          getUserInfo();
          router.push({ name: "HomeView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const logOut = function () {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          token.value = null;
          router.push({ name: "ArticleView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      articles,
      API_URL,
      getArticles,
      signup,
      logIn,
      token,
      isLogin,
      logOut,
      finlifes,
      getMap,
      mapview,
      profile,
      userInfo,
    };
  },
  { persist: true }
);
