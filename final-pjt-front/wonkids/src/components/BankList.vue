<template>
  <div>
    <h3>banklist 출력</h3>
    <Bank
      v-for="bank in store.banks"
      :key="bank.id"
      :bank="bank"
    />

  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/banks';
import Bank from '@/components/Bank.vue'

const store = useBankStore()

</script>

<style scoped>

</style>