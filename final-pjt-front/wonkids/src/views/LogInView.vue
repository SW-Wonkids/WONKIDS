<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <label for="username">username: </label>
      <input type="text" v-model.trim="username"><br>

      <label for="password">password: </label>
      <input type="password" v-model.trim="password"><br>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
  
const store = useAuthStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>

</style>
