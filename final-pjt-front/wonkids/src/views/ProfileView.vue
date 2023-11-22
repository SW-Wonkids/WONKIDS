<template>
  <div>
    <h1>{{ userinfo.username }} 님의 프로필 페이지</h1>
    <hr>  
    <p> 나의 결과는!! {{ userinfo.category }}</p>
    <p> 나의 아이디 : {{ userinfo.id }}</p>
  </div>
  
</template>

<script setup>

import { onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile'

const store = useProfileStore()

const userinfo = store.userinfo

onMounted(() => {
    store.getProfile()
})

</script>

<style scoped>

</style>