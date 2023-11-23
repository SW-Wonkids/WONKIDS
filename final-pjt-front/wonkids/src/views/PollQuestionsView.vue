<template>
  
  <div id="app" style="margin-left: 55px; margin-right: 55px;font-family: 'NanumBarunGothicYetHangul';">
    <h1 class="koreanfont">나의 포켓몬 유형을 찾아봅시다!</h1>
    <h1 style="  font-family: 'Pixelify Sans', sans-serif;"><strong>Find my Pokemon!</strong></h1>
    <hr>
    <div v-if="showQuiz" style="text-align: center; font-size: 200%;" class="card">
      <div v-if="currentQuestionIndex < questions.length">
        <div class="question" style="font-style: italic;">
          <p>{{ questions[currentQuestionIndex].text }}</p>
          <br>
          <p>{{ answersA[currentQuestionIndex].text }}</p>
          <p>{{ answersB[currentQuestionIndex].text }}</p>
          <br>
          <br>
          <button class="selectbutton btn btn-danger" @click="answerQuestion(1)">
            <img src="@/assets/pokeball.webp" style="width:70px;"><p style="color: black;"><strong>A</strong></p></button>
          <button class="selectbutton btn btn-danger" @click="answerQuestion(0)">
            <img src="@/assets/pokeball.webp" style="width:70px;"><p style="color: black;"><strong>B</strong></p></button>
        </div>
      </div>
      <div v-else>
        <button @click="calculateResult">결과 확인</button>
      </div>
    </div>
    <div class="container">
      <div v-if="showResult" style="text-align: center; padding: 20px;" class="card">
        <h2>결과: {{ result }}</h2>

        <div v-if="result === '꼬부기'" style="font-size:20px;">물 타입 포켓몬인 꼬부기는 잔잔하게 흐르는 물의 특징을 침착하고 차분한 성향으로 연관지어 가정했습니다.<br> 목돈을 한꺼번에 맡기고 차분히 기다릴 수 있는 성향임을 가정하여 예금 4개를 추천합니다.</div>
        <div v-if="result === '파이리'" style="font-size:20px;">불꽃 타입 포켓몬인 파이리는 활활 타오르는 불의 특징을 활발하고 화끈한 성격으로 연관지어 가정했습니다.<br> 꾸준히 일정 금액을 넣으며 만기일을 기다리는 성향임을 가정하여 적금 4개를 추천합니다.</div>
        <div v-if="result === '피카츄'" style="font-size:20px;">전기 타입 포켓몬인 피카츄는 파이리와 꼬부기를 선택한 사람의 중간으로 가정하여, 적금 2개, 예금 2개를 추천합니다.</div>
        <form @submit.prevent="sendResult">
        <button class="submit-button" style="margin-top: 10px;">결과 보러 가기</button>
        </form>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { usePollStore } from '@/stores/polls'
import router from '../router';

const store = usePollStore()

const showQuiz = ref(true)
const showResult = ref(false)
const currentQuestionIndex = ref(0)
const questions = ref([
  { text: "질문1. 만약에 지구상에 나 혼자 살아남게 된다면..." },
  { text: "질문2. 타임머신을 타게된다면 나는... " },
  { text: "질문3. 크리스마스에 나는..." },
  { text: "질문4. 학교를 다니면서 나는..." },
  { text: "질문5. 여행을 간다면 나는..." },
]) 
const answersA = ref([
  { text: "A. 농사를 지으며 지구에서 살아남을 것이다 " },
  { text: "A. 미래로 가서 미래의 나에게 조언을 들을 것이다  " },
  { text: "A. 집에서 트리를 꾸미면서 영화를 볼 것이다" },
  { text: "A. 사물함에 책을 차곡차곡 정리했다 " },
  { text: "A. 조용한 여행지로 가서 힐링할 것이다" },
])
const answersB = ref([
  { text: "B. 우주선을 만들어서 다른 행성을 찾아서 탐험할 것이다" },
  { text: "B. 과거로 가서 투자를 할 것이다" },
  { text: "B. 친구들과 밖에서 눈사람을 만들것이다" },
  { text: "B. 사물함에 책을 마구 던져서 넣었다" },
  { text: "B. 도심으로 여행가서 쇼핑을 할 것이다" },
])
const answers = ref([])

const result = ref("")

const answerQuestion = (score) => {
  answers.value[currentQuestionIndex.value] = score
  nextQuestion()
}

const nextQuestion = () => {
  if (currentQuestionIndex.value < questions.value.length - 1) {
    currentQuestionIndex.value++
  } else {
    calculateResult()
    showResult.value = true
    showQuiz.value = false
  }
}

const calculateResult = () => {
  const score = answers.value.reduce((total, answer) => total + answer, 0);

  if (score === 0 || score === 1) {
    result.value = "파이리"
  } else if (score === 2 || score === 3) {
    result.value = "피카츄"
  } else {
    result.value = "꼬부기"
  }
}

const sendResult = () => {
  const pokemon = result.value
  store.sendResult(pokemon)
  // console.log(pokemon)
  // console.log('send')
  router.push({ name: 'profile' })
}
</script>

<style scoped>
h1 {
  text-align: center;
}
#app {
  background-image: url('@/assets/case1.jpg');
  height: 70vh;
  display: flex;
  flex-direction:column;
  align-content: center;
  align-items: center;
  text-align: center;
}
hr {
  border: 10px solid green;
  border-radius: 5px;
}

.selectbutton {
  border-radius: 30px;
  width: 60px;
  height: 60px;

  font-size: 30px;
  margin-right: 55px;

}

.card {
  width: 80%;
  height: 120%;
  justify-content: center;
  
  background-image: url('@/assets/case5.png');
  border-radius: 5%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.9); 

}

.container {
  display: flex;
  flex-direction:column;
  align-content: center;
  align-items: center;
  text-align: center;
  
}


</style>
