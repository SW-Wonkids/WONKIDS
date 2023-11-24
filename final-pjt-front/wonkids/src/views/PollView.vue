<template>
  <div class="koreanfont" style="margin-left: 55px; margin-right: 55px; font-size: 30px;">
    <h1><strong>Catch the Pokemon!</strong></h1>
    <p class="koreanfont">포켓몬을 잡으러 모험을 떠나봅시다!</p>
    <p class="warning">주의! 포켓몬은 한 사람 당 한 포켓몬만 데리고 있을 수 있어요.<br>
      만약 기존에 포켓몬을 데리고 있었다면 그 포켓몬은 사라지니 조심하세요!
    </p>
    <form @submit.prevent="goPollQuestions">
        <input type="submit" value="출발!" class="koreanfont" style="font-size: 25px;">
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
  margin-top: 30px;
  font-size: 50px;
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

.warning {
  font-size: 18px;
}
</style>