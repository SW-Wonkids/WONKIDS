<template>
  <div>
    <RouterLink :to="{name: 'banktotal'}">전체 금융상품 확인하기</RouterLink>    |
    <RouterLink :to="{name: 'banklist_deposit'}">정기예금(DEPOSIT) 금융상품은 여기서 확인해보세요!</RouterLink>  
    <!-- <h1>적금 금융상품을 여기서 확인해보세요!</h1> -->
    <hr>
    <BankListSavings />

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBankStore } from '@/stores/banks'
import BankListSavings from '@/components/BankListSavings.vue'

const store = useBankStore()

onMounted(() => {
  store.getBanksSavings()
})
</script>

<style scoped>

</style>