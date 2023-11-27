<template>
  <div class="ct">
    <div class="s">
      <label for="type-select">상품 유형:</label>
      <br />
      <select id="type-select" v-model="selectedType" @change="filterByType">
        <option value="">전체</option>
        <option value="S">정액적립식</option>
        <option value="F">자유적립식</option>
      </select>
    </div>
    <table>
      <thead>
        <tr>
          <th>은행 명</th>
          <th>상품 명</th>
          <th>유형 별</th>
          <th>6개월</th>
          <th>12개월</th>
          <th>24개월</th>
          <th>36개월</th>
        </tr>
      </thead>
      <tbody
        v-for="finance in filteredFinances"
        :key="finance.rsrv_type"
        v-if="selectedType === 'S'"
      >
        <tr
          v-if="
            finance.savingoptions_set.filter((item) => item.rsrv_type === 'S')
              .length != 0
          "
        >
          <td>{{ finance.kor_co_nm }}</td>

          <RouterLink
            class="title"
            :to="{
              name: 'FinSavingDetailView',
              params: { fin_prdt_cd: finance.fin_prdt_cd },
            }"
          >
            {{ finance.fin_prdt_nm }}
          </RouterLink>
          <!-- S -->
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.rsrv_type && item.rsrv_type === "S";
              })
                ? finance.savingoptions_set.find((item) => {
                    return item.rsrv_type && item.rsrv_type === "S";
                  }).rsrv_type_nm
                : "-"
            }}
          </td>

          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 6 && item.rsrv_type === "S";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 6 && item.rsrv_type === "S"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 6 && item.rsrv_type === "S"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 12 && item.rsrv_type === "S";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 12 && item.rsrv_type === "S"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 12 && item.rsrv_type === "S"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 24 && item.rsrv_type === "S";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 24 && item.rsrv_type === "S"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 24 && item.rsrv_type === "S"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 36 && item.rsrv_type === "S";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 36 && item.rsrv_type === "S"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 36 && item.rsrv_type === "S"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
        </tr>
      </tbody>

      <tbody
        v-for="finance in filteredFinances"
        :key="finance.rsrv_type"
        v-if="selectedType === 'F'"
      >
        <tr
          v-if="
            finance.savingoptions_set.filter((item) => item.rsrv_type === 'F')
              .length != 0
          "
        >
          <td>{{ finance.kor_co_nm }}</td>

          <RouterLink
            class="title"
            :to="{
              name: 'FinSavingDetailView',
              params: { fin_prdt_cd: finance.fin_prdt_cd },
            }"
          >
            {{ finance.fin_prdt_nm }}
          </RouterLink>

          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.rsrv_type && item.rsrv_type === "F";
              })
                ? finance.savingoptions_set.find((item) => {
                    return item.rsrv_type && item.rsrv_type === "F";
                  }).rsrv_type_nm
                : "-"
            }}
          </td>

          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 6 && item.rsrv_type === "F";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 6 && item.rsrv_type === "F"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 6 && item.rsrv_type === "F"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 12 && item.rsrv_type === "F";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 12 && item.rsrv_type === "F"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 12 && item.rsrv_type === "F"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 24 && item.rsrv_type === "F";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 24 && item.rsrv_type === "F"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 24 && item.rsrv_type === "F"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
          <td>
            {{
              finance.savingoptions_set.find((item) => {
                return item.save_trm === 36 && item.rsrv_type === "F";
              })
                ? finance.savingoptions_set.find(
                    (item) => item.save_trm === 36 && item.rsrv_type === "F"
                  ).intr_rate
                  ? finance.savingoptions_set.find(
                      (item) => item.save_trm === 36 && item.rsrv_type === "F"
                    ).intr_rate
                  : "-"
                : "-"
            }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useProductStore } from "@/stores/product.js";
import FinlifeList from "@/components/FinlifeList.vue";
import FinlifeSavingList from "@/components/FinlifeSavingList.vue";

const store = useProductStore();
console.log(store);
const options = ref(["정기예금", "정기적금"]);
const selectedOption = ref("정기예금");
onMounted(() => {
  store.getFinlife();
  store.getFinlife2();
});

const selectedType = ref("S");

const filteredFinances = computed(() => {
  return store.finlifes2.filter((finance) =>
    finance.savingoptions_set.some(
      (item) => item.rsrv_type === selectedType.value
    )
  );
});

const manyfinance = computed(() => {
  return store.finlifes2;
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

.tc {
  margin: 50px;
}
.jump {
  padding: 0px;
}

.hidden {
  display: none;
}
</style>
