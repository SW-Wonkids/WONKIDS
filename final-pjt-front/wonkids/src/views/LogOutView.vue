<template>
    <div>
      <h1>LogOut</h1>
      <p>정말로 로그아웃하시겠습니까?</p>
        <form @submit.prevent="store.logOut">
            <input type="submit" value="logOut">
        </form>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()

  </script>
  
  <style scoped>
  
  </style>
  