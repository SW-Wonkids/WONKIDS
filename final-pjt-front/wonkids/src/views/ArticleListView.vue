<template>
  <div>
    <h1>article list</h1>
    <RouterLink :to="{name:'article-create'}">게시글 생성</RouterLink>
    <ul>
      <div
          v-for="article in store.articleList"
          :key="article.pk"
          :post="article"
          @click="goDetail(article.pk)"
        >
        <p>{{ article.category.name }}</p>
        <h3> <span>{{ article.pk }}번 글 |</span>  {{ article.title }}</h3>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useArticleStore } from '../stores/articles'
import { useRouter } from 'vue-router'


const router = useRouter()
const store = useArticleStore()
onMounted(() => {
  store.getArticleList()
})

const goDetail = (pk) => {
  router.push({name:'article', params:{pk: pk}})
}

</script>

<style scoped>

</style>