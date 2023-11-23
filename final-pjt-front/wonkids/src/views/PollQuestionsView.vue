<template>
  <hr style="margin-left: 55px; margin-right: 55px;">
  <div id="app" style="margin-left: 55px; margin-right: 55px;font-family: 'NanumBarunGothicYetHangul';">
    <h1>나의 포켓몬 유형을 찾아봅시다</h1>
    <hr>
    <div v-if="showQuiz">
      <div v-if="currentQuestionIndex < questions.length">
        <div class="question">
          <p>{{ questions[currentQuestionIndex].text }}</p>
          <p>{{ answersA[currentQuestionIndex].text }}</p>
          <p>{{ answersB[currentQuestionIndex].text }}</p>
          <button class="selectbutton" @click="answerQuestion(1)">A</button>
          <button class="selectbutton" @click="answerQuestion(0)">B</button>
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
const answersA = ref([
  { text: "답변1A." },
  { text: "답변2A." },
  { text: "답변3A." },
  { text: "답변4A." },
  { text: "답변5A." },
])
const answersB = ref([
  { text: "답변1B." },
  { text: "답변2B." },
  { text: "답변3B." },
  { text: "답변4B." },
  { text: "답변5B." },
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

</style>
