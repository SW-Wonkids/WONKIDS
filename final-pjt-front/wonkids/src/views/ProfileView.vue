<template>
  <div>
    <Profile 
    v-for="user in store.users"
    :key="user.id"
    :user="user"/>
  </div>
</template>

<script setup>

import Profile from '@/components/Profile.vue'
import { onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile'

const store = useProfileStore()

onMounted(() => {
    store.getProfile()
})
</script>

<style scoped>

</style>