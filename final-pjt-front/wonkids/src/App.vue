<script setup>

import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const store = useAuthStore()

</script>

<template>
  <header>
    <div class="wrapper">
      <nav v-if="store.isLogin">
        <RouterLink :to="{name: 'home'}"><img src="@/assets/wonkids.png" class="d-block w-100" style="max-width: 100px; height: auto; text-align: left;"></RouterLink>
        <RouterLink :to="{name: 'logout'}">Log Out</RouterLink>
        <RouterLink :to="{name: 'profile'}">Profile</RouterLink>
        <RouterLink :to="{name: 'banktotal'}">Bank</RouterLink>
        <RouterLink :to="{name: 'article-list'}">Article</RouterLink>
        <RouterLink :to="{name: 'poll'}">Pokemon</RouterLink>
        <RouterLink :to="{name: 'exchange-rate'}">Exchange-rate</RouterLink>
      </nav>
      <nav v-else>
        <RouterLink :to="{name: 'home'}"><img src="@/assets/wonkids.png" class="d-block w-100" style="max-width: 100px; height: auto; text-align: left;"></RouterLink>
        <RouterLink :to="{name: 'signup'}">Sign Up</RouterLink>
        <RouterLink :to="{name: 'login'}">Log In</RouterLink>
        <RouterLink :to="{name: 'banktotal'}">Bank</RouterLink>
        <RouterLink :to="{name: 'exchange-rate'}">Exchange-rate</RouterLink>
      </nav>
    </div>
  </header>
  
  
  <RouterView />
  
</template>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}
nav {
  display: flex;
  justify-content: center;
  /* background-color: #333; */
  background-color: rgb(255, 204, 0);
  padding: 1rem 0;
  
}

nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 1rem;
  font-weight: bold;
} 

nav a:hover {
  /* text-decoration: underline overline cadetblue; */
  text-decoration: rgb(53,106,188) wavy underline;
  
} 

nav {
  font-family: 'Pixelify Sans', sans-serif;

}

</style>

<style>
.koreanfont {
  font-family: 'NanumBarunGothicYetHangul';
}
</style>