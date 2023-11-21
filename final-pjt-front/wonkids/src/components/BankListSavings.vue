<template>
  <!--BankListSavings > BankSavings 적금 vue page -->
  <div>
    <h2>적금 상품 List 출력</h2>
    <BankSavings
      v-for="bank in store.banks"
      :key="bank.id"
      :bank="bank"/>

  </div>
</template>

<script setup>
import BankSavings from '@/components/BankSavings.vue'
import { useBankStore } from '@/stores/banks'

const store = useBankStore()
</script>

<style scoped>

</style>