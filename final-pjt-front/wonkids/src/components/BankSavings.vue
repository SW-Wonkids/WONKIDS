<template>
  <!--BankListSavings > BankSavings 적금 vue page -->
  <div>
    <h5>{{ bank.id }}.</h5>
    <table style="width:80%">
      <tr>
        <th>공시 제출월[YYYYMM]</th>
        <th>금융회사 명</th>
        <th>금융 상품명</th>
        <th>저축 기간 6개월</th>
        <th>저축 기간 12개월</th>
        <th>저축 기간 24개월</th>
        <th>저축 기간 36개월</th>
      </tr>
      <tr>
        <td>{{ bank.dcls_month }}</td>
        <td>{{ bank.kor_co_nm }}</td>
        <td><RouterLink :to="{name: 'BankSavingsDetail', params: {id: bank.id}}">{{ bank.fin_prdt_nm }}</RouterLink></td>
        <td>{{ bank.intr_rate_6 }}</td>
        <td>{{ bank.intr_rate_12 }}</td>
        <td>{{ bank.intr_rate_24 }}</td>
        <td>{{ bank.intr_rate_36 }}</td>
      </tr>
    <!-- <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
    <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
    <p class="product">금융 상품명 : <RouterLink :to="{name: 'BankSavingsDetail', params: {id: bank.id}}">{{ bank.fin_prdt_nm }}</RouterLink></p>
    <p>저축 기간 {{ bank.save_trm_6 }}(개월) - 저축 금리 {{ bank.intr_rate_6 }}</p>
    <p>저축 기간 {{ bank.save_trm_12 }}(개월) - 저축 금리 {{ bank.intr_rate_12 }}</p>
    <p>저축 기간 {{ bank.save_trm_24 }}(개월) - 저축 금리 {{ bank.intr_rate_24 }}</p>
    <p>저축 기간 {{ bank.save_trm_36 }}(개월) - 저축 금리 {{ bank.intr_rate_36 }}</p> -->
    </table>  
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
  text-decoration:cadetblue wavy underline;
}
table, th, td {
  border: 1px solid;
}
</style>