import { ref, computed, watch } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import axios from "axios";

export const useProductStore = defineStore(
  "product",
  () => {
    const finlifes = ref([]);
    const finlifes2 = ref([]);
    const finlifes3 = ref([]);
    const finlifes4 = ref([]);
    const profile = ref("");
    const API_URL = "http://127.0.0.1:8000";
    const API_KEY = "AIzaSyCRQecy4yCB4ZNyFdWzyx_HQRitFaXwqPI";
    const token = ref(null);

    const getFinlife = function () {
      axios({
        method: "get",
        url: `${API_URL}/finlife/deposit-products/`,
      })
        .then((res) => {
          console.log(res.data)
          finlifes.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getFinlife2 = function () {
        axios({
          method: "get",
          url: `${API_URL}/finlife/saving-products/`,
        })
          .then((res) => {
            finlifes2.value = res.data;
          })
          .catch((err) => {
            console.log(err);
          });
      };
  const getFinlife3 = function () {
    axios({
      method: "get",
      url: `${API_URL}/finlife/saving-products-options/`,
    })
      .then((res) => {
        finlifes3.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getFinlife4 = function () {
    axios({
      method: "get",
      url: `${API_URL}/finlife/saving-products-options/`,
    })
      .then((res) => {
        finlifes4.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
    

    return {
      API_URL,
      token,
      getFinlife,
      getFinlife2,
      finlifes,
      finlifes2,
      profile,
      getFinlife3,
      getFinlife4,
      finlifes3,
      finlifes4
    };
  },
  { persist: true }
);
