<template>
  <div class="ct">
    <div class="search">
      <h3>검색하기</h3>
      <b>검색 조건을 입력하세요</b>
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
            v-for="(finance, index) in uniqueFinlifes"
            :key="index"
            :value="finance"
          >
            {{ finance }}
          </option>
        </select>
      </div>
      <div>
        <label for="savings-type-select">저축 유형 선택:</label>
        <br />
        <select
          id="savings-type-select"
          v-model="selectedSavingsType"
          @change="filterBySavingsType"
        >
          <option value="">전체</option>
          <option value="S">정액적립식</option>
          <option value="F">자유적립식</option>
          <!-- 필요한 경우 더 많은 옵션을 추가해주세요 -->
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
            <th>적금유형</th>
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
          <tr v-for="finance in filteredFinances" :key="finance.id">
            <td></td>
            <td>{{ finance.kor_co_nm }}</td>
            <td class="findetail">
              <RouterLink
                class="title"
                :to="{
                  name: 'FinSavingDetailView',
                  params: { fin_prdt_cd: finance.fin_prdt_cd },
                }"
              >
                {{ finance.fin_prdt_nm }}
              </RouterLink>
            </td>
            <td>
              <span v-if="isRegularSavings(finance)">정기적금</span>
              <span v-else-if="isFlexibleSavings(finance)">자유적금</span>
              <span v-else>기타</span>
            </td>
            <td v-for="term in [6, 12, 24, 36]" :key="term">
              {{ getInterestRate(finance, term) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useProductStore } from "@/stores/product.js";

const store = useProductStore();
const selectedSavingsType = ref("");

const uniqueFinlifes = computed(() => [
  ...new Set(store.finlifes2.map((finance) => finance.kor_co_nm)),
]);

const selectedProduct = ref("");

const filterProducts = () => {
  if (!selectedProduct.value) {
    return store.finlifes2;
  } else {
    return store.finlifes2.filter(
      (finance) => finance.kor_co_nm === selectedProduct.value
    );
  }
};

const filteredFinances = computed(() => {
  if (selectedSavingsType.value) {
    return store.finlifes2.filter((finance) => {
      const byBank =
        !selectedProduct.value || finance.kor_co_nm === selectedProduct.value;
      const bySavingsType = finance.savingoptions_set.some(
        (option) => option.rsrv_type === selectedSavingsType.value
      );
      return byBank && bySavingsType;
    });
  } else if (selectedProduct.value) {
    return store.finlifes2.filter(
      (finance) => finance.kor_co_nm === selectedProduct.value
    );
  } else {
    return store.finlifes2;
  }
});
const isRegularSavings = (finance) => {
  return finance.savingoptions_set.some((option) => option.rsrv_type === "S");
};

const isFlexibleSavings = (finance) => {
  return finance.savingoptions_set.some((option) => option.rsrv_type === "F");
};

const getInterestRate = (finance, term) => {
  const option = finance.savingoptions_set.find(
    (option) => option.save_trm === term
  );
  return option && option.intr_rate !== null ? option.intr_rate : " ";
};

const sortByTerm = (term, order) => {
  filteredFinances.value.sort((a, b) => {
    const interestA = getInterestRate(a, term) || 0;
    const interestB = getInterestRate(b, term) || 0;
    return order === "asc" ? interestA - interestB : interestB - interestA;
  });
};

onMounted(() => {
  console.log(store.finlifes2);
});
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
  margin-top: 5px;
}

select {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  margin-top: 5px;
}

.findetail > a{
  text-decoration: none;
  text-decoration-line: none;
  color: black;
}
</style>
