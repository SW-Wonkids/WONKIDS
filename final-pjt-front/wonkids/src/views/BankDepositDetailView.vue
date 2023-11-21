<!--BankListDepositView > BankListDeposit > BankDeposit 정기예금 vue page -->
<template>
  <div>
    <h1>정기예금 상세</h1>
    <div v-if="bank">
      <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
      <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
      <p>상품명 : {{ bank.fin_prdt_nm }}</p>
      <p>가입제한 : {{ bank.join_deny }}</p>
      <p>가입 방법 : {{ bank.join_way }}</p>
      <p>우대조건 : {{ bank.spcl_cnd }}</p>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import {useBankStore} from '@/stores/banks'

const store = useBankStore()
const route = useRoute()
const bank = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/bank_deposit/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data)
      bank.value = res.data
    })
    .catch((err) => console.log(err))
})

</script>

<style scoped>

</style>

