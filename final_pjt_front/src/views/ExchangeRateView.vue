<template>
  <div class="container">
    <h1>환율 계산기</h1>
    <div class="box">
      <p v-if="rate">현재 환율은 {{ rate }}입니다.</p>
      <div class="nrbox">
        <div class="ch">
          나라 선택
          <select v-model="select2">
            <option v-for="payment in payments" :key="payment" :value="payment">
              <span class="arrow-icon"></span>
              <!-- 나라 선택하는 코드 -->
              {{ payment }}
            </option>
          </select>
          <span class="arrow-icon"></span>
        </div>
        <div class="ch">
          환전할 나라 선택
          <select v-model="select1">
            <option v-for="payment in chk" :key="payment" :value="payment">
              {{ payment }}
            </option>
          </select>
          <span class="arrow-icon"></span>
        </div>
      </div>
      <div class="sort">
        <div>
          <p>입력한 돈</p>
          <input
            type="text"
            v-model.number="payment1"
            @change="updatePayment2((payment1 / rate) * currencyUnit)"
            class="inputbox"
          />
        </div>
        <div>
          <p>환전 받을 돈</p>
          <input
            type="text"
            v-model.number="payment2"
            @change="updatePayment2((payment2 * rate) / currencyUnit)"
            class="inputbox"
          />
        </div>
      </div>
      <!-- 돈 입력받는 코드 -->
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import axios from "axios";
// prettier-ignore
const payments = ref(["EUR(유로)","JPY(일본)","GBP(영국)","CHF(스위스)","CAD(캐나다)","AUD(호주)","CNY(중국)","HKD(홍콩)","SEK(스웨덴)","NZD(뉴질랜드)","KRW(대한민국)","SGD(싱가포르)","NOK(노르웨이)","MXN(멕시코)","INR(인도)","RUB(러시아)","ZAR(남아프리카 공화국)","TRY(터키)","BRL(브라질)","AED(아랍에미리트)","BHD(바레인)","BND(브루나이)","CNH(중국 엔화)","CZK(체코)","DKK(덴마크)","IDR(인도네시아)","ILS(이스라엘)","MYR(말레이시아)","QAR(카타르)","SAR(사우디아라비아)","THB(태국)","TWD(대만)","CLP(칠레)","COP(콜롬비아)","EGP(이집트)","HKD(홍콩)","HUF(헝가리)","KWD(쿠웨이트)","OMR(오만)","PHP(필리핀)","PLN(폴란드)","PKR(파키스탄)","RON(루마니아)","BRL(브라질)","BDT(방글라데시)","DZD(알제리)","ETB(에티오피아)","FJD(피지)","JOD(요르단)","KES(케냐)","KHR(캄보디아)","KZT(카자흐스탄)","LKR(스리랑카)","LYD(리비아)","MMK(미얀마)","MNT(몽골)","MOP(마카오)","NPR(네팔)","TZS(탄자니아)","UZS(우즈베키스탄)","VND(베트남)",
]);

const select1 = ref(null);
const select2 = ref(null);
const chk = ref(["KOR", ""]);
// 두 환율 옵션이 선택되었을 때에 환율 금액 정보 가져오기
watch([select1, select2], ([newOption1, newOption2]) => {
  console.log(select1);
  console.log(select2);
  console.log(newOption2);
  const slicedOption2 = newOption2?.substring(0, 3) || '';
  // chk = ref(["KOR", `${newOption2}`])
  chk.value = ["KOR", `${select2.value}`];
  if (newOption1 !== null && newOption2 !== null) {
    axios({
      url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${slicedOption2}`,
      method: "GET",
    })
      .then(({ data }) => {
        console.log(data);
        rate.value = data[0]?.basePrice || -1;
        currencyUnit.value = data[0]?.currencyUnit || 1;
        console.log(currencyUnit);
        updatePayment2.value = updatePayment2();
      })
      .catch((err) => console.log(err));
  }
});

const payment1 = ref(0);
const payment2 = ref(0);

const updatePayment2 = function () {
  if (select1.value === "KOR") {
    payment2.value = (payment1.value / rate.value) * currencyUnit.value;
  } else {
    payment2.value = (payment1.value * rate.value) / currencyUnit.value;
  }
};

const rate = ref(null);
const currencyUnit = ref(null);
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  font-family: "JalnanGothic";
}

.box {
  border-radius: 5px;
  border: solid 4px #dfccfb;
  /* background-color: #fff3da; */
  width: 900px;
  height: 300px;
  margin: 50px;
  padding: 40px;
  font-family: "JalnanGothic";
}

.box > p {
  display: flex;
  justify-content: center;
}

div > select {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #a9a9a9;
  margin: 5px;
}

.selbox {
  display: flex;
}

.inputbox {
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
}

.selbox > p {
  margin: 10px;
}

.arrow-icon {
  width: 0;
  height: 0;
  border-left: 5px solid transparent; /* 화살표 모양 설정 */
  border-right: 5px solid transparent; /* 화살표 모양 설정 */
  border-top: 5px solid #000; /* 화살표 색상 설정 */
  text-align: center;
  align-items: center;
}

.nrbox {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

.ch {
  display: flex;
  align-items: center;
}

.sort {
  display: flex;
  justify-content: space-evenly;
}

@font-face {
  font-family: "JalnanGothic";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_231029@1.1/JalnanGothic.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
