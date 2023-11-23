<template>
  <hr>
  <div id="app">
    <h1>Vue Type Quiz</h1>
    <hr>
    <div v-if="showQuiz">
      <div v-if="currentQuestionIndex < questions.length">
        <div class="question">
          <p>{{ questions[currentQuestionIndex].text }}</p>
          <button @click="answerQuestion(1)">1점을 가지는 선택지</button>
          <button @click="answerQuestion(0)">0점을 가지는 선택지</button>
        </div>
      </div>
      <div v-else>
        <button @click="calculateResult">결과 확인</button>
      </div>
    </div>
    <div v-if="showResult">
      <h2>결과: {{ result }}</h2>
      <p>유형에 대한 설명을 작성해보자</p>
      <form @submit.prevent="sendResult">
      <button class="submit-button">결과 보러 가기</button>
      </form>
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
  { text: "질문1." },
  { text: "질문2." },
  { text: "질문3." },
  { text: "질문4." },
  { text: "질문5." },
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
    result.value = "피카츄"
  } else if (score === 2 || score === 3) {
    result.value = "파이기"
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
hr {
  border: 10px solid green;
  border-radius: 5px;
}
</style>
