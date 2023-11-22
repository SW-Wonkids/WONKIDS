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
import { usePollStore } from '@/stores/polls'

const store = useProfileStore()
const pollstore = usePollStore()

const userinfo = store.userinfo

onMounted(() => {
    store.getProfile()
    pollstore.getResult()
})

</script>

<style scoped>

</style>