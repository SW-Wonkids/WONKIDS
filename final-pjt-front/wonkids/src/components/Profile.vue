<template>
  
  <div>


    <h1>{{ user.username }} 님의 프로필 페이지</h1>
    <hr>  
    <p> 나의 결과는!! 카테고리 입력될 부분{{ user.category }}</p>
    <p> 나의 아이디 : {{ user.id }}</p>


  </div>
</template>

<script setup>
defineProps({
  user: Object
})

</script>

<style scoped>
h1 {
  text-align: center;
}

</style>