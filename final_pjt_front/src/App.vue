<template>
  <header>
    <nav v-if="store.isLogin" class="navbar navbar-expand-lg bg-custom-color">
      <div class="container-fluid">
        <router-link :to="{ name: 'HomeView' }" class="navbar-brand">
          <img src="../src/assets/은행-removebg-preview-removebg-preview.png"
        /></router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavDropdown"
          aria-controls="navbarNavDropdown"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link :to="{ name: 'FinlifeView' }" class="nav-link"
                >금융상품</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'ExchangeRateView' }" class="nav-link"
                >환율</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'MapView' }" class="nav-link"
                >지도</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'ArticleView' }" class="nav-link"
                >게시판</router-link
              >
            </li>
          </ul>

          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <div class="d-flex align-items-center">
                <router-link :to="{ name: 'ProfileView' }" class="nav-link me-3"
                  >프로필</router-link
                >
                <form @submit.prevent="store.logOut">
                  <input
                    type="submit"
                    value="로그아웃"
                    class="nav-link btn btn-link"
                  />
                </form>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <nav v-else class="navbar navbar-expand-lg bg-body-tertiary">
      <router-link :to="{ name: 'SignUpView' }" class="nav-link"
        >가입하기</router-link
      >
      |
      <router-link :to="{ name: 'LogInView' }" class="nav-link"
        >로그인</router-link
      >
      |
    </nav>
  </header>
  <router-view />
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
</script>

<style scoped>
.navbar {
  font-size: 32px;
  height: 100px;
  /* font-family: "Noto Serif KR", serif; */
  font-family: "Bagel Fat One", serif;
}

.bg-custom-color {
  background-color: #f1eaff;
}

h1 {
  color: #fff3da;
}

.navbar-brand {
  flex-wrap: wrap;
  /* height: 300px; */
}

.navbar-brand > img {
  width: 80%;
  margin-left: 20px;
}

.nav-link {
  margin: 20px;
}
</style>
