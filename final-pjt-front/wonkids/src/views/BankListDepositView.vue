<template>
  <!--BankListDepositView > BankListDeposit > BankDeposit 정기예금 vue page -->
  <div>
    <RouterLink :to="{name: 'banktotal'}">전체 금융상품 확인하기</RouterLink><br>  
    <RouterLink :to="{name: 'banklist_savings'}">정기적금(SAVINGS) 금융상품은 여기서 확인해보세요!</RouterLink>  
    <hr>
    <BankListDeposit />

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBankStore } from '@/stores/banks'
import BankListDeposit from '@/components/BankListDeposit.vue'

const store = useBankStore()

onMounted(() => {
  store.getBanksDeposit()
})
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>  