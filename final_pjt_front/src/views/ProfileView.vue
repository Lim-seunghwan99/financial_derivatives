<template>
  <div class="userprofile">
    <h1>프로필</h1>
    <br />
    <div v-if="profile">
      <div class="userprofile">
        <p><strong>유저 이름 :</strong> {{ profile?.username }}</p>
        <br />
        <p><strong>이메일 :</strong> {{ profile?.email }}</p>
        <br />
        <p><strong>나이 :</strong> {{ profile?.age }}</p>
        <br />
        <p><strong>보유금 :</strong> {{ profile?.money }}</p>
        <br />
        <p><strong>연봉 :</strong> {{ profile?.salary }}</p>
        <br />
        <p><strong>가입상품 :</strong> {{ profile?.financial_products }}</p>
        <br />
        <RouterLink :to="{ name: 'UpdateProfileView' }">프로필 수정</RouterLink>
        <br />
        <button class="chart">
          <RouterLink :to="{ name: 'ChartView',}"> 차트확인
          </RouterLink>
        </button>
        <hr />
      </div>
      <hr />
      <h3>나와 비슷한 사람들이 가입한 상품</h3>
      <div v-if="recommendations.length > 0">
        <br />
        <div class="row">
          <div
            v-for="(recommendation, index) in recommendations"
            :key="`rec-${index}`"
          >
            <div v-if="index !== 0" style="margin-top: 20px"></div>
            <div class="card-grid">
              <div
                v-for="(code, idx) in recommendation.split(',')"
                :key="`code-${idx}`"
                class="card"
                style="width: 18rem; margin-top: 20px"
              >
                <div class="card-body">
                  <div
                    v-if="
                      store2.finlifes.some(
                        (item) => item.fin_prdt_cd === code.trim()
                      )
                    "
                  >
                    <RouterLink
                      :to="`/finlife/deposit-products/${code.trim()}`"
                      class="card-link"
                    >
                      {{
                        store2.finlifes.find(
                          (item) => item.fin_prdt_cd === code.trim()
                        )?.fin_prdt_nm
                      }},
                      <br />
                      가입자:
                      {{
                        store2.finlifes.find(
                          (item) => item.fin_prdt_cd === code.trim()
                        )?.join_member
                      }},
                      <br />
                      은행:
                      {{
                        store2.finlifes.find(
                          (item) => item.fin_prdt_cd === code.trim()
                        )?.kor_co_nm
                      }}
                    </RouterLink>
                  </div>

                  <div
                    v-else-if="
                      store2.finlifes2.some(
                        (item) => item.fin_prdt_cd === code.trim()
                      )
                    "
                  >
                    <RouterLink
                      :to="`/finlife/saving-products/${code.trim()}`"
                      class="card-link"
                    >
                      {{
                        store2.finlifes2.find(
                          (item) => item.fin_prdt_cd === code.trim()
                        )?.fin_prdt_nm
                      }},
                      <br />
                      가입자:
                      {{
                        store2.finlifes2.find(
                          (item) => item.fin_prdt_cd === code.trim()
                        )?.join_member
                      }},
                      <br />
                      은행:
                      {{
                        store2.finlifes2.find(
                          (item) => item.fin_prdt_cd === code.trim()
                        )?.kor_co_nm
                      }}
                    </RouterLink>
                  </div>
                  <div v-else>
                    <p>추천 상품이 없습니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>추천 상품이 없습니다.</p>
      </div>
      <br />
      <br />
      <br />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useProductStore } from "@/stores/product";

const store1 = useCounterStore();
const store2 = useProductStore();
const profile = ref(null);
const recommendations = ref([]);
const url = ref(`${store1.API_URL}/api/profile/${store1.userInfo.username}/`);
const url2 = ref(`${store1.API_URL}/algo/${store1.userInfo.username}/`);

onMounted(() => {
  axios
    .get(url.value)
    .then((res) => {
      profile.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
});

onMounted(() => {
  console.log(profile);
  axios
    .get(url2.value)
    .then((res) => {
      recommendations.value = res.data.recommendations;
    })
    .catch((err) => {
      console.error(err);
    });
});
</script>

<style>
.card-grid {
  display: flex;
  flex-wrap: nowrap;
  gap: 20px;
  /* justify-content: left; */
  width: 100%;
  justify-content: center;
}

.card {
  flex-basis: calc(25% - 50px);
  height: 300px;
  width: 200px;
}

.userprofile {
  /* font-family: "Noto Serif KR", serif; */
  /* font-family: "Diphylleia", serif; */
  font-family: "Diphylleia", serif;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.userprofile > h1 {
  margin: 20px;
}

h3 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card-link {
  text-decoration-line: none;
  color: black;
}

.card-body {
  display: flex;
  align-items: center;
  height: 150px; /* 높이를 원하는 값으로 지정 */
  width: 100%;
}

.chart > a{
  text-decoration: none;
  text-decoration-line: none;
  color: black;
}
</style>
