<template>
  <div class="ct">
    <div class="search">
      <h3>검색하기</h3>
      <hr />
      <div>
        <label for="product-select">은행 선택:</label>
        <br />
        <select
          id="product-select"
          v-model="selectedProduct"
          @change="filterProducts"
          class="inputbox"
        >
          <option value="">전체 은행</option>
          <option
            v-for="(finlife, index) in uniqueFinlifes"
            :key="index"
            :value="finlife"
          >
            {{ finlife }}
          </option>
        </select>
      </div>
    </div>
    <div class="dv">
      <table class="table table-hover">
        <thead>
          <tr>
            <th class="tc"></th>
            <th>금융회사명</th>
            <th>상품명</th>
            <th>
              6개월
              <span @click="sortByTerm(6, 'asc')">▲</span>
              <span @click="sortByTerm(6, 'desc')">▼</span>
            </th>
            <th>
              12개월
              <span @click="sortByTerm(12, 'asc')">▲</span>
              <span @click="sortByTerm(12, 'desc')">▼</span>
            </th>
            <th>
              24개월
              <span @click="sortByTerm(24, 'asc')">▲</span>
              <span @click="sortByTerm(24, 'desc')">▼</span>
            </th>
            <th>
              36개월
              <span @click="sortByTerm(36, 'asc')">▲</span>
              <span @click="sortByTerm(36, 'desc')">▼</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="finlife in filteredFinlifes" :key="finlife.id">
            <td></td>
            <td>{{ finlife.kor_co_nm }}</td>
            <td class="findetail">
              <RouterLink
                class="title"
                :to="{
                  name: 'FinDetailView',
                  params: { fin_prdt_cd: finlife.fin_prdt_cd },
                }"
              >
                {{ finlife.fin_prdt_nm }}
              </RouterLink>
            </td>
            <td
              v-for="mn in finlife.depositoptions_set"
              :class="{ hidden: mn.save_trm !== 6 }"
            >
              <span>{{ mn.intr_rate }}</span>
            </td>
            <td
              v-for="mn in finlife.depositoptions_set"
              :class="{ hidden: mn.save_trm !== 12 }"
            >
              <span>{{ mn.intr_rate }}</span>
            </td>
            <td
              v-for="mn in finlife.depositoptions_set"
              :class="{ hidden: mn.save_trm !== 24 }"
            >
              <span>{{ mn.intr_rate }}</span>
            </td>
            <td
              v-for="mn in finlife.depositoptions_set"
              :class="{ hidden: mn.save_trm !== 36 }"
            >
              <span>{{ mn.intr_rate }}</span>
            </td>
            <!-- 필요한 만큼 열 추가 -->
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useProductStore } from "@/stores/product.js";

const store = useProductStore();
const uniqueFinlifes = ref([
  ...new Set(store.finlifes.map((finlife) => finlife.kor_co_nm)),
]);

const selectedProduct = ref("");

const filterProducts = () => {
  if (!selectedProduct.value) {
    return store.finlifes;
  } else {
    return store.finlifes.filter(
      (finlife) => finlife.kor_co_nm === selectedProduct.value
    );
  }
};

const filteredFinlifes = computed(() => {
  return filterProducts();
});
const sortByTerm = (term, order) => {
};
</script>

<style scoped>
.ct {
  display: flex;
  margin: 10px;
  /* justify-content: space-between; */
  padding: 5px;
}

tr > th {
  padding: 10px;
}

.tc {
  margin: 50px;
}
.jump {
  padding: 0px;
}

.hidden {
  display: none;
}

.inputbox {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  margin-top: 10px;
}

.findetail > a{
  text-decoration: none;
  text-decoration-line: none;
  color: black;
}
</style>