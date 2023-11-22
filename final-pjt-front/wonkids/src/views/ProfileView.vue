<template>
  <div>
    <h1>{{ userinfo.username }} 님의 프로필 페이지</h1>
    <hr>  
    <div v-if="userinfo.category">
      <p>나의 결과는!! {{ userinfo.category }}</p>
      <p>결과에 따른 추천 상품 목록</p>

      <p>다시 한번 유형 검사를 하고 싶다면?</p>
      <p>아래의 버튼을 클릭하세요!</p>
      <form @submit.prevent="goPollIndex">
          <input type="submit" value="유형검사 다시 하기">
        </form>
    </div>

    <div v-else>
      <p>나의 유형은? 지금 유형검사에 참여하여 나의 유형도 알고</p>
      <p>추천 상품 목록도 확인해보세요!</p>
        <form @submit.prevent="goPollIndex">
          <input type="submit" value="유형검사 하러 가기">
        </form>
    </div>
    <p>나의 아이디 : {{ userinfo.username }}</p>
    <p>나의 이메일 : {{ userinfo.email }}</p>
    <p>나의 나이: {{ userinfo.age }}</p>
    <p>나의 학교: {{ userinfo.school }}</p>
    <p>나의 학년: {{ userinfo.grade }}</p>
    <p>나의 반: {{ userinfo.classnum }}</p>
  </div>
  
</template>

<script setup>

import { onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile'
import { usePollStore } from '@/stores/polls'
import { useRouter } from 'vue-router'

const router = useRouter()
const goPollIndex = () => {
  router.push({ name: 'poll' })
}

const store = useProfileStore()
const pollstore = usePollStore()

const userinfo = store.userinfo

onMounted(() => {
    store.getProfile()
    pollstore.getResult()
})

</script>

<style scoped>

</style>