<template>
  <div>
    <h5>BankList</h5>
    <BankList />

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBankStore } from '@/stores/banks'
import BankList from '@/components/BankList.vue'

const store = useBankStore()

onMounted(() => {
  store.getBanks()
})
</script>

<style scoped>

</style>