<template>
  <!--BankListDepositView > BankListDeposit > BankDeposit 정기예금 vue page 
    + BankListSavingsView > BankListSavings > BankSavings 적금 vue page -->
  <div>
    <p>정기예금 & 적금 금융상품을 여기서 확인해보세요!</p>
    <RouterLink :to="{name: 'banklist_deposit'}">정기예금(DEPOSIT)</RouterLink>   | 
    <RouterLink :to="{name: 'banklist_savings'}">적금(SAVINGS)</RouterLink>    |
   
    <p>근처 은행 카카오맵으로 보기</p>
    <RouterLink :to="{name: 'bankmap'}">근처 은행 검색</RouterLink>

  </div>
</template>

<script setup>

</script>

<style scoped>

</style>