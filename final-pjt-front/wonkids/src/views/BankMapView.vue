<template>
  <div>
      <!-- Dropdown <select> -->
    <select v-model="selected" @change="searchBanks" style="margin-left: 50px;">
      <option 
      v-for="option in options" 
      :key="option.value" 
      :value="option.value">
        {{ option.text }} 
      </option>
    </select>

    <div><p style="margin-top: 10px; margin-left: 50px; font-family: 'NanumBarunGothicYetHangul';">우리동네 근처 은행을 검색하자:</p> {{ selected }} </div>

    <!--지도가 표시되는 영역 id=map으로 설정 -->
    <div id="map"></div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// 입력값에 따라 변할 수 있도록 let 사용
let map = null;
let infowindow = null;
let places = null;

onMounted(() => {
  // window DOM 에 카카오 객체가 있고 카카오 맵도 그릴 수 있다면 initMap()으로 맵을 실행한다 
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
   
    const script = document.createElement('script');
    script.onload = () => kakao.maps.load(initMap);
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${import.meta.env.VITE_APP_KAKAO_MAP_KEY}&libraries=services`;
    document.head.appendChild(script);
  }
});

// 지도를 띄우는 함수 
// map 객체 두번째 파라미터 options의 속성 중 center는 지도 생성에 반드시 필요
const initMap = () => {
  const container = document.getElementById('map');  // 지도를 담을 영역의 DOM 레퍼런스
  const options = {  // 지도를 생성할 때 필요한 기본 옵션
    center: new kakao.maps.LatLng(37.566826, 126.9786567),   // 지도의 중심좌표: LatLng 클래스는 위도, 경도 좌표값 입력
    level: 7,    //지도의 레벨 (확대, 축소 정도)  
  };

  map = new kakao.maps.Map(container, options)  // 지도 생성 및 객체 리턴
  // 검색하기 위한 변수들
  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
  places = new kakao.maps.services.Places()
};

const selected = ref('');
const options = ref([
{ text: '서울 마포구 은행', value: '서울 마포구 은행' },
{ text: '서울 용산구 은행', value: '서울 용산구 은행' },
{ text: '서울 성동구 은행', value: '서울 성동구 은행' },
{ text: '서울 광진구 은행', value: '서울 광진구 은행' },
{ text: '서울 강서구 은행', value: '서울 강서구 은행' },
{ text: '서울 서대문구 은행', value: '서울 서대문구 은행' },
{ text: '서울 은평구 은행', value: '서울 은평구 은행' },
{ text: '대전 유성구 은행', value: '대전 유성구 은행' },
{ text: '대전 유성구 은행', value: '대전 유성구 은행' },
{ text: '대전 유성구 은행', value: '대전 유성구 은행' },
{ text: '대전 유성구 은행', value: '대전 유성구 은행' },
{ text: '대전 대덕구 은행', value: '대전 대덕구 은행' },
{ text: '대전 서구 은행', value: '대전 서구 은행' },
{ text: '대전 중구 은행', value: '대전 중구 은행' },
{ text: '대전 동구 은행', value: '대전 동구 은행' },
{ text: '대구 동구 은행', value: '대구 동구 은행' },
{ text: '대구 수성구 은행', value: '대구 수성구 은행' },
{ text: '대구 달서구 은행', value: '대구 달서구 은행' },
{ text: '대구 북구 은행', value: '대구 북구 은행' },
{ text: '대구 달성군 은행', value: '대구 달성군 은행' },
{ text: '대구 서구 은행', value: '대구 서구 은행' },
{ text: '대구 중구 은행', value: '대구 중구 은행' },
{ text: '대구 남구 은행', value: '대구 남구 은행' },

]);

const searchBanks = () => {
  places.keywordSearch(selected.value, placesSearchCallback);
};

const placesSearchCallback = (data, status) => {
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
  width: 500px;
  height: 400px;
  margin-left: 50px;
  border: 5px dashed pink
}

</style>