<template>
  <div>
    <h1>poll index</h1>
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

</style>