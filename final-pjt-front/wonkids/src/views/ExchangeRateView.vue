<template>
  <hr style="margin-left: 55px; margin-right: 55px;">
  <h2 class="divider line glow" contenteditable></h2>
  <div id="app">
    <h1><img src="@/assets/exchangeRate.png" class="d-block w-100" style="max-width: 500px; height: auto; text-align: left;"></h1>
    <p class="koreanfont">환율계산기</p>
    <div class="container">
      <div class="container-one">
        <!-- options -->
        
        <select name="first-courrency" id="first-currency" v-model="currency_one">
          <option value="KRW">KRW</option>
          <option value="USD">USD</option>
          <option value="JPY">JPY</option>
          <option value="EUR">EUR</option>
          <option value="GBP">GBP</option>
          <option value="CNY">CNY</option>
        </select>
        <input
          type="number"
          name="input-one"
          id="input-one"
          v-model="amountOne"
          @input="fetchData()">
      </div>

      <!-- change button -->
      <div class="container-two">
        <button @click="switchValues()"><span>Switch</span></button>
        
      </div>
      <h4 class="baseValue koreanfont" style="margin-top: 8px;">1 {{ currency_one }} = {{ rate }} {{ currency_two }}</h4>

      <!-- options -->
      <div class="container-three">
        <select name="second-currency" id="second-currency" v-model="currency_two">
          <option value="KRW">KRW</option>
          <option value="USD">USD</option>
          <option value="JPY">JPY</option>
          <option value="EUR">EUR</option>
          <option value="GBP">GBP</option>
          <option value="CNY">CNY</option>
        </select>
        <input type="number" id="amount-two" placeholder="0" disabled v-model="amountTwo">
      </div>

      <!-- date -->
      <div class="container-four">
        <h4 class="h4 koreanfont" style="margin-top: 5px;">환율 계산 기준 일자:  {{ data.time_last_update_utc }}</h4>
      </div>
      
    </div>
  </div>
  <div class="card koreanfont" style="width: 90vh; margin-top: 50px; margin-right: 55px;">
    <div class="card-body">
      <h5 class="card-title">환율에 대해 알아볼까요?</h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">환율</h6>
      <p class="card-text">
        각 나라마다 쓰는 화폐가 다르기 때문에 그 나라에 간다면 우리나라 돈을 그 나라의 돈으로 바꿔야 해요 <br>
        환율은 이렇게 우리나라 돈과 다른 나라 돈을 교환할 때 사용하는 교환 비율입니다 <br>

        환율이 오른다면 우리나라 돈의 가치가 떨어진다는 의미입니다 <br>
        우리나라에서 1000원이면 살 수 있던 물건을 1300원을 줘야 살 수 있게 되죠 <br>

        반대로 환율이 내린다면 어떨까요? <br> 
        우리나라에서 1000원이면 살 수 있던 물건을 다른 나라에서는 700원을 주고 싸게 살 수 있어요! <br>

        환율은 세계 경제 사정에 따라, 국제 경제 흐름에 따라 매일매일 달라집니다 <br>
        오늘의 환율은 어떤지 한번 확인해볼까요?</p>
 
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const data = ref([
  {
    // 데이터 샘플 내용을 여기에 복사해 넣으세요.
  }
]);
const currency_one = ref('KRW')
const currency_two = ref('USD')
const rate = ref('?')
const amountOne = ref(0)
const amountTwo = ref(0)

const fetchData = () => {
  fetch(`https://v6.exchangerate-api.com/v6/${import.meta.env.VITE_APP_API_KEY}/latest/${currency_one.value}`)
    .then(res => res.json())
    .then(responseData => {
      console.log(responseData)
      data.value = responseData
      rate.value = responseData.conversion_rates[currency_two.value]
      amountTwo.value = (amountOne.value * rate.value)
    });
};

const switchValues = () => {
  const temporaryValue = currency_one.value
  currency_one.value = currency_two.value
  currency_two.value = temporaryValue
  fetchData()
}
</script>

<style scoped>
.divider {
  display: flex;
}
  
.divider::after {
    content: "";
    flex: 1;
  }

.line {
  align-items: center;
  margin: 1em -1em;
}

.line::after {
    height: 1px;
    margin: 0 1em;
  }

.glow {

      height: 6px;
      -webkit-filter: blur(5px);
      border-radius: 5px;
    }
    
.glow::before {
      background: linear-gradient(to right, blue, hotpink);
    }
    
.glow::after {
      background: linear-gradient(to left, blue, hotpink);
    }

hr { 
  border: 20px solid green;
  border-radius: 5px;
}

html {
  background: #f4f4f4f4;
}
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-content: center;
  width: 50%;
  height: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  float: left;
}
.card {
  float: right;
}
h1{
  color: #5fbaaf;
}
.container{
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction:column;
  align-content: center;
  align-items: center;
  text-align: center;
}

.container-two {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 60%;
  
}

.container-two button {
  padding: 4px;
  font-size: 18px;
  background-color: #5fbaaf;
  color: #fff;
  width: 1000%;
  height: 10%;
  border: none;
  outline: none;
  border-radius: 5px;
  text-align: center;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
  margin-left: 3px;
}

.container-two button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.container-two button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;

}

.container-two button:hover span {
  padding-right: 25px;

}

.container-two button:hover span:after {
  opacity: 1;
  right: 0;

}

select {
  padding: 5px;
  margin: 5px;
  border: 1px solid rgba(0,0,0,0,5);
  outline: none;
}

input{
  padding: 5px;
  margin: 5px;
  border: 1px solid rgba(0,0,0,0,5);
  outline: none;
  font-size: 18px;
}

.h4 {
  font-weight: 500;
  font-size: 15px;
}

.baseValue {
  font-weight: 500;
  font-size: 15px;
}

</style>
