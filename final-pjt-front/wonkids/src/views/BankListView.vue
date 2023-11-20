<template>
  <div>
    <h1>banklist</h1>
    <BankList />

  </div>
</template>

<script setup>
import BankList from '@/components/BankList.vue';
import { onMounted } from 'vue'
import { useBankStore } from '@/stores/banks';

const bank = useBankStore()

onMounted(() => {
  bank.getBanks()
})
</script>

<style scoped>

</style>