<template>
  <div class="koreanfont">
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
      <label for="username">username: </label>
      <input type="text" v-model.trim="username" style="margin-top: 20px"><br>

      <label for="email">email: </label>
      <input type="email" v-model.trim="email" style="margin-top: 20px"><br>

      <label for="school">school: </label>
      <input type="text" v-model.trim="school" style="margin-top: 20px"><br>

      <label for="grade">grade: </label>
      <input type="number" v-model.trim="grade" style="margin-top: 20px"><br>

      <label for="classnum">classnum: </label>
      <input type="number" v-model.trim="classnum" style="margin-top: 20px"><br>

      <label for="age">age: </label>
      <input type="number" v-model.trim="age" style="margin-top: 20px"><br>

      <label for="password1">password: </label>
      <input type="password" v-model.trim="password1" style="margin-top: 20px"><br>

      <label for="password2">password confirmation: </label>
      <input type="password" v-model.trim="password2" style="margin-top: 20px;"><br>
      
      <input type="submit" value="포켓몬 트레이너가 되기" style="margin-top: 20px;">
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
const email = ref(null)
const age = ref(null)
const school = ref(null)
const grade = ref(null)
const classnum = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    age: age.value,
    school: school.value,
    grade: grade.value,
    classnum: classnum.value
  }
  store.signUp(payload)
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