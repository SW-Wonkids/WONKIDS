<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
      <label for="username">username: </label>
      <input type="text" v-model.trim="username"><br>

      <label for="email">email: </label>
      <input type="email" v-model.trim="email"><br>

      <label for="password1">password: </label>
      <input type="password" v-model.trim="password1"><br>

      <label for="password2">password confirmation: </label>
      <input type="password" v-model.trim="password2"><br>
      
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
  
const store = useAuthStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style scoped>

</style>