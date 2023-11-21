<script setup>

import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const store = useAuthStore()

</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
    <div class="wrapper">
      <nav v-if="store.isLogin">
        <RouterLink :to="{name: 'home'}">Home</RouterLink>
        <RouterLink :to="{name: 'logout'}">Log Out</RouterLink>
        <RouterLink :to="{name: 'profile'}">Profile</RouterLink>
        <RouterLink :to="{name: 'banktotal'}">Bank</RouterLink>
        <RouterLink :to="{name: 'article-list'}">Article</RouterLink>
        <RouterLink :to="{name: 'poll'}">Poll</RouterLink>
        <RouterLink :to="{name: 'exchange-rate'}">Exchange-rate</RouterLink>
      </nav>
      <nav v-else>
        <RouterLink :to="{name: 'home'}">Home</RouterLink>
        <RouterLink :to="{name: 'signup'}">Sign Up</RouterLink>
        <RouterLink :to="{name: 'login'}">Log In</RouterLink>
        <RouterLink :to="{name: 'banktotal'}">Bank</RouterLink>
        <RouterLink :to="{name: 'article-list'}">Article</RouterLink>
        <RouterLink :to="{name: 'poll'}">Poll</RouterLink>
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
  text-decoration: cadetblue wavy underline;
  
} 

/* header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
</style>
