<template>
  <div class="background">
    <h1>Trainer Community</h1>
    <button type="button" class="btn btn-light" style="margin-left: 33px;"><RouterLink :to="{name:'article-create'}">게시글 생성</RouterLink></button>
    <ul>
      <div
          v-for="article in store.articleList"
          :key="article.pk"
          :article="article"
          @click="goDetail(article.pk)"
          class="card" style="width: 18rem; margin-top: 20px;"
        >

        <div class="card-body">
          <p class="card-title">{{ article.category.name }}</p>
          <p class="card-text"><span>제목 : {{ article.title }} |</span> 내용 : {{ article.content }}</p>
          
        </div>
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
  router.push({name:'article', params:{pk: pk} })
}

</script>

<style scoped>
.background {
  background-image: url('@/assets/case5.png');
  height: 100vh;
}

h1 {
  text-align: center;
}
a {
  text-decoration: none;
  color: rgb(53,106,188);
}

</style>