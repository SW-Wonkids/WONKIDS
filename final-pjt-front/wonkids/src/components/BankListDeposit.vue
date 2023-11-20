<template>
  <!--BankListDeposit > BankDeposit 정기예금 vue page -->
  <div>
    <h2>정기예금 상품 List 출력</h2>
    <BankDeposit
      v-for="bank in store.banks"
      :key="bank.id"
      :bank="bank"/>

  </div>
</template>

<script setup>
import BankDeposit from '@/components/BankDeposit.vue'
import { useBankStore } from '@/stores/banks'

const store = useBankStore()
</script>

<style scoped>

</style>