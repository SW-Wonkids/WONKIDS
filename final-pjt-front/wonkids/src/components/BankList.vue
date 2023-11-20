<template>
  <div>
    <h2>정기예금 상품 List 출력</h2>
    <Bank 
      v-for="bank in store.banks"
      :key="bank.id"
      :bank="bank"/>

  </div>
</template>

<script setup>
import Bank from '@/components/Bank.vue'
import { useBankStore } from '@/stores/banks'

const store = useBankStore()
</script>

<style scoped>

</style>