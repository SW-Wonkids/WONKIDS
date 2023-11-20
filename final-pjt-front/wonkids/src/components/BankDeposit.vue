<template>
  <div>
    <h5>{{ bank.id }}.</h5>
    <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
    <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
    <p>금융 상품명 : {{ bank.fin_prdt_nm }}</p>
    <p>저축 기간 {{ bank.save_trm_6 }}(개월) - 저축 금리 {{ bank.intr_rate_6 }}</p>
    <p>저축 기간 {{ bank.save_trm_12 }}(개월) - 저축 금리 {{ bank.intr_rate_12 }}</p>
    <p>저축 기간 {{ bank.save_trm_24 }}(개월) - 저축 금리 {{ bank.intr_rate_24 }}</p>
    <p>저축 기간 {{ bank.save_trm_36 }}(개월) - 저축 금리 {{ bank.intr_rate_36 }}</p>
    <hr>

  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>

<style scoped>

</style>