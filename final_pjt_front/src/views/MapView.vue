<template>
  <div class="site-container">
    <input
      @keyup.enter="search"
      type="text"
      v-model="keywords"
      placeholder="검색"
      class="inputbox"
    />
    <div class="google-map">
      <GoogleMap
        api-key="AIzaSyCRQecy4yCB4ZNyFdWzyx_HQRitFaXwqPI"
        style="width: 100%; height: 500px"
        :center="center"
        :zoom="zoom"
        language="kor"
      >
        <MarkerCluster>
          <Marker
            v-for="(location, i) in locations"
            :options="{ position: location }"
            :key="i"
          >
            <InfoWindow>
              <div id="contet">
                <div id="siteNotice"></div>
                <h5 id="firstHeading" class="firstHeading">
                  {{ location.name }}
                </h5>
                <div id="bodyContent"></div>
              </div>
            </InfoWindow>
          </Marker>
        </MarkerCluster>
      </GoogleMap>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { GoogleMap, Marker, MarkerCluster, InfoWindow } from "vue3-google-map";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
const zoom = ref(15);
const center = ref({ lat: 36.1081844, lng: 128.4139686 });
const locations = ref([]);
const store = useCounterStore();
const maps = ref("");
const keywords = ref("");

const search = function () {
  locations.value = [];
  axios({
    method: "get",
    url: `${store.API_URL}/maps/api/place/textsearch/json`,
    params: {
      query: `${keywords.value}`,
      key: "AIzaSyCRQecy4yCB4ZNyFdWzyx_HQRitFaXwqPI",
      // language: "ko",
    },
  })
    .then((res) => {
      console.log(res.data.results);
      console.log(res);
      zoom.value = 15;
      if (res.data.results.length > 0) {
        const firstResult = res.data.results[0];
        center.value = {
          lat: firstResult.geometry.location.lat,
          lng: firstResult.geometry.location.lng,
        };
      }
      for (let i = 0; i < res.data.results.length; i++) {
        let temp1 = res.data.results[i].geometry.location.lat;
        let temp2 = res.data.results[i].geometry.location.lng;
        let info = {
          lat: temp1,
          lng: temp2,
          name: res.data.results[i].name, // 추가 정보 예시: 장소의 이름
        };
        locations.value.push(info);
      }
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/map/`,
  })
    .then((res) => {
      maps.value = res.data;
      console.log(maps.value.results);
      for (let i = 0; i < res.data.results.length; i++) {
        let temp1 = res.data.results[i].geometry.location.lat;
        let temp2 = res.data.results[i].geometry.location.lng;
        let info = {
          lat: temp1,
          lng: temp2,
          name: res.data.results[i].name, // 추가 정보 예시: 장소의 이름
        };
        locations.value.push(info);
      }
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped>
.site-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.inputbox {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 8px;
  border-radius: 4px;
  border: solid 1px #a9a9a9;
  width: 30%;
  font-family: "JalnanGothic";
}

.google-map {
  width: 100%;
}
</style>
