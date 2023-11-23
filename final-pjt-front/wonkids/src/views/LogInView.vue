<template>
  <div class="koreanfont">
    <h1 style="margin-bottom: 30px;">Login</h1>
    <form @submit.prevent="logIn">
      <label for="username">username: </label>
      <input type="text" v-model.trim="username" style="margin-bottom: 15px; margin-left: 15px;"><br>

      <label for="password">password: </label>
      <input type="password" v-model.trim="password" style="margin-left: 15px;"><br>

      <input type="submit" style="margin-top: 30px;" value="포켓몬 월드 입장하기">
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
div {
    margin-left: 55px;
    text-align: center;
    margin-top: 100px;
    background-image: url('@/assets/pokeball.webp');
    background-repeat: no-repeat;
    height: 100vh;
}
</style>
