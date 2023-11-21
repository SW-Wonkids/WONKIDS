<!--BankListSavingsView > BankListSavings > BankSavings > BankSavingsDetailView -->

<template>
  <div>
    <p class="topic">구체적으로 이 적금 금융상품에 대해 알아보자!</p>
    <div v-if="bank">
      <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
      <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
      <p>상품명 : {{ bank.fin_prdt_nm }}</p>
      <p>가입제한 : {{ bank.join_deny }}</p>
      <p>가입 방법 : {{ bank.join_way }}</p>
      <p>우대조건 : {{ bank.spcl_cnd }}</p>
      <RouterLink :to="{name: 'banklist_savings'}">
      [BACK]
      </RouterLink>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import {useBankStore} from '@/stores/banks'
import { RouterLink} from 'vue-router'
const store = useBankStore()
const route = useRoute()
const bank = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/bank_savings/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data)
      bank.value = res.data
    })
    .catch((err) => console.log(err))
})

</script>

<style scoped>
.topic {
  text-decoration: cadetblue wavy underline;
}
</style>

