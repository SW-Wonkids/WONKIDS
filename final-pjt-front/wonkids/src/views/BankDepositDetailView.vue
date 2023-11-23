<!--BankListDepositView > BankListDeposit > BankDeposit > BankDepositDetailView -->
<template>
  <div class="koreanfont">
    
    <div v-if="bank">
    <p style="font-size: 20px; text-align: center; margin-top: 30px;">구체적으로 <strong>{{ bank.fin_prdt_nm }}</strong> 에 대해 알아보자!</p>

      <div class="container">
      <div class="card">
      <div class="card-body">
      <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
      <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
      <p>상품명 : {{ bank.fin_prdt_nm }}</p>
      <p>가입제한 : {{ bank.join_deny }}</p>
      <p>가입 방법 : {{ bank.join_way }}</p>
      <p>우대조건 : {{ bank.spcl_cnd }}</p>
      <RouterLink :to="{name: 'banklist_deposit'}">
      [BACK]
      </RouterLink>
    </div>
    </div>
    </div>
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
.card {
  width: 50%;
  border: 2px solid rgb(53,106,188);
  border-radius: 2%;
  margin-top: 30px;
  margin-left: 55px;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

a{
  text-decoration: none;
}
</style>

