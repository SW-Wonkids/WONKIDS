<template>
  <!--BankListDeposit > BankDeposit 정기예금 vue page -->
  <div class="koreanfont">
    <h5>{{ bank.id }}.</h5>
    <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
    <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
    <p class="product">금융 상품명 : <strong><RouterLink :to="{name: 'BankDepositDetail', params: {id: bank.id}}" style=" text-decoration: underline;border-bottom: 1px solid;">{{ bank.fin_prdt_nm }}</RouterLink></strong><img src="@/assets/arrow.png" style="width:50px;">클릭하면 상세 정보 확인 가능합니다</p>
    <p>저축 기간 {{ bank.save_trm_6 }}(개월) - 저축 금리 {{ bank.intr_rate_6 }}</p>
    <p>저축 기간 {{ bank.save_trm_12 }}(개월) - 저축 금리 {{ bank.intr_rate_12 }}</p>
    <p>저축 기간 {{ bank.save_trm_24 }}(개월) - 저축 금리 {{ bank.intr_rate_24 }}</p>
    <p>저축 기간 {{ bank.save_trm_36 }}(개월) - 저축 금리 {{ bank.intr_rate_36 }}</p>
    <hr>

  </div> 
  
</template>

<script setup>
import { RouterLink} from 'vue-router'
defineProps({
  bank: Object
})
</script>

<style scoped>
.product { 

  
}
a{
  text-decoration: none;
}

</style>