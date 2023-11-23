<template>
  <div>
    <h1>Catch the Pokemon!</h1>
    <p>유형검사를 시작해봅시다!</p>
    <form @submit.prevent="goPollQuestions">
        <input type="submit" value="유형 검사 시작하기">
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const goPollQuestions = () => {
  router.push({ name: 'poll-questions' })
}
</script>

<style scoped>

h1 {
  font-family: 'Pixelify Sans', sans-serif;
  text-align: center;
}

div {
  background-image: url('@/assets/case1.jpg');
  height: 100vh;
  opacity:0.8;
  display: flex;
  flex-direction:column;
  align-content: center;
  align-items: center;
  text-align: center;
}

div p {
  text-align: center;
}

div input {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 25px;
  font-size: 15px;
  text-align: center;
  cursor: pointer;
  outline: none;
  color: black;
  /* background-color: #04AA6D; */
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}
div input:hover {background-color: #343634}

div input:active {
  /* background-color: #3e8e41; */
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
</style>