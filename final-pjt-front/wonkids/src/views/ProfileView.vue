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
import { usePollStore } from '@/stores/polls'

const store = useProfileStore()
const pollstore = usePollStore()

onMounted(() => {
    store.getProfile()
    pollstore.getResult()
})
</script>

<style scoped>

</style>