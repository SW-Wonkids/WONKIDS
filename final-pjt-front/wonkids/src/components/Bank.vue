<template>
  <div>
    <h5>공시제출월: {{ bank.dcls_month }}</h5>
    <h5>{{ bank.fin_prdt_cd }}</h5>
    <h5>{{ bank.content }}</h5>

  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>

<style scoped>

</style>