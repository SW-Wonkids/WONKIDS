<template>
  <!-- 1. 사람이 input값 넣는다
      2. 큰 도시의 구만 드롭다운 만들고 은행 드롭다운 만들어서 
      두개의 벨류값을 합쳐서 제출한다
      -->
  <div>
      <!-- 드롭다운 만들기 -->
    <select v-model="selected" @change="searchPlaces">
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.text }}
      </option>
    </select>
    <div>선택됨: {{ selected }}</div>
    <!-- 지도 표시 -->
    <div id="map"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let map = null;
let infowindow = null;
let ps = null;

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement('script');
    script.onload = () => kakao.maps.load(initMap);
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${import.meta.env.VITE_APP_KAKAO_MAP_KEY}&libraries=services`;
    document.head.appendChild(script);
  }
});

const initMap = () => {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(36.3508, 127.3839),
    level: 7,
  };

  map = new kakao.maps.Map(container, options);
  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  ps = new kakao.maps.services.Places();
};

const selected = ref('');
const options = ref([
{ text: '유성구 은행', value: '대전 은행' },
{ text: '대덕구 은행', value: '대전 대덕구 은행' },
{ text: '서구 은행', value: '대전 서구 은행' },
{ text: '중구 은행', value: '대전 중구 은행' },
{ text: '동구 은행', value: '대전 동구 은행' },
]);

const searchPlaces = () => {
  ps.keywordSearch(selected.value, placesSearchCB);
};

const placesSearchCB = (data, status, pagination) => {
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();

    for (let i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    map.setBounds(bounds);
  }
};

const displayMarker = (place) => {
  const marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  kakao.maps.event.addListener(marker, 'click', () => {
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
    infowindow.open(map, marker);
  });
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 350px;
}
</style>