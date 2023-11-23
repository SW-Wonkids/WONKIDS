<template>
    <div class="koreanfont">
      <h1>LogOut</h1>
      <p>정말로 로그아웃하시겠습니까?</p>
        <form @submit.prevent="store.logOut">
            <input type="submit" value="logOut">
        </form>
    </div>
</template>
  
<script setup>
import { useAuthStore } from '@/stores/auth'
  
const store = useAuthStore()

</script>
  
<style scoped>
div {
    margin-left: 55px;
    text-align: center;
    margin-top: 100px;
}
</style>
  