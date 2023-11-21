<template>
  <div>
    <div>
      <div>
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
      <div>
        <button @click="switchValues()">Switch</button>
        <h4>1 {{ currency_one }} = {{ rate }} {{ currency_two }}</h4>
      </div>

      <!-- options -->
      <div>
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
      <div>
        <h4>반영 날짜:  {{ data.time_last_update_utc }}</h4>
      </div>
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
  // fetch(`https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${currency_one.value}`)
  // fetch(`https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?${process.env.VUE_APP_KEY}&searchdate=20180102&data=AP01`)
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
</style>
