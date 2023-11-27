import { createRouter, createWebHistory } from "vue-router";
import ArticleView from "@/views/ArticleView.vue";
import DetailView from "@/views/DetailView.vue";
import CreateView from "@/views/CreateView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import FinLifeView from "@/views/FinLifeView.vue";
import ExchangeRateView from "@/views/ExchangeRateView.vue";
import ProductsView from "@/views/ProductsView.vue";
import MapView from "@/views/MapView.vue";
import FinDetailView from "@/views/FinDetailView.vue";
import ProfileView from "@/views/ProfileView.vue";
import FinSavingDetailView from "@/views/FinSavingDetailView.vue";
import UpdateProfileView from "@/views/UpdateProfileView.vue";
import ArticleEditView from "@/views/ArticleEditView.vue";
import HomeView from "@/views/HomeView.vue";
import OtherProfileView from "@/views/OtherProfileView.vue";
import ChartView from "@/views/ChartView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView,
    },
    {
      path: "/articles/:id",
      name: "DetailView",
      component: DetailView,
    },
    {
      path: "/create",
      name: "CreateView",
      component: CreateView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/products",
      name: "ProductsView",
      component: ProductsView,
    },
    {
      path: "/mapview",
      name: "MapView",
      component: MapView,
    },
    {
      path: "/finlife",
      name: "FinlifeView",
      component: FinLifeView,
    },
    {
      path: "/exchange",
      name: "ExchangeRateView",
      component: ExchangeRateView,
    },
    {
      path: "/finlife/deposit-products/:fin_prdt_cd",
      name: "FinDetailView",
      component: FinDetailView,
    },
    {
      path: "/finlife/saving-products/:fin_prdt_cd",
      name: "FinSavingDetailView",
      component: FinSavingDetailView,
    },
    {
      path: "/api/profile",
      name: "ProfileView",
      component: ProfileView,
    },
    {
      path: "/articles",
      name: "ArticleView",
      component: ArticleView,
    },
    {
      path: "/articles/:id/update",
      name: "ArticleEditView",
      component: ArticleEditView,
    },
    {
      path: "/api/profile",
      name: "UpdateProfileView",
      component: UpdateProfileView,
    },
    {
      path: "/api/profile/:username",
      name: "OtherProfileView",
      component: OtherProfileView,
    },
    {
      path: "/ChartView",
      name: "ChartView",
      component: ChartView,
    }
  ],
});

import { useCounterStore } from "@/stores/counter";

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "ArticleView" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  } else if (
    (to.name === "SignUpView" || to.name === "LogInView") &&
    store.isLogin
  ) {
    window.alert("이미 로그인 했습니다.");
    return { name: "ArticleView" };
  }
});

export default router;
