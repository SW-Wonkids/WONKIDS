<template>
  <div class="background koreanfont" style="margin-left: 50px; margin-right: 50px;">
    <h1 style="color: aliceblue; font-size: 24px; text-decoration: underline;"><img src="@/assets/articletitle.png" style="width: 30%;"></h1>
    
    <div class="container">
    <p class="card-banner" style="font-size: 18px;text-align: center; width: 60%; height: 60%; margin-bottom: 50px;">
      나와 같은 포켓몬을 잡은 사람은 누구일까요? <br>궁금하다면 해당 <strong>카테고리를 선택</strong>하고 글을 써보세요!<br>
      ↓ 아직 잡은 포켓몬이 없다면 아래로 ↓<br>
      <RouterLink :to="{name: 'poll'}"><span class="clickclick" style="font-size: 40px; color: yellow;">Catch the Pokemon</span></RouterLink>
      </p>
    <p class="card-banner" style="font-size: 18px;text-align: center; width: 55%; margin-top: 0px;"><strong>게시글 작성 규칙</strong><br>
        <br>
        카테고리: 피카츄, 파이리, 꼬부기 중 하나를 선택해주세요<br>
        카테고리는 한번 설정하면 수정을 할 수 없으니 신중하게 골라주세요<br>
        <br>
        제목은 최대 50자까지 작성할 수 있어요<br>
        내용은 최대 250자까지 작성할 수 있어요<br>
        댓글은 최대 250까지 쓸 수 있어요<br>
        <br>
        <strong>P.S. 한 번 작성한 댓글은 수정을 할 수 없으니 신중하게 작성해주세요!</strong></p>

        <button type="button" class="btn btn-light" style="margin-left: 33px;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.9); width: 200px; height: 50px; margint ">
          <RouterLink :to="{name:'article-create'}" style="font-size: 24px;">게시글 생성</RouterLink>
        </button><br>
    
   
    </div>
      <ul>
        <div
            v-for="article in store.articleList"
            :key="article.pk"
            :article="article"
            @click="goDetail(article.pk)"
            class="card" style="width: 18rem; margin-top: 20px;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.9); "
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
  border-radius: 13px;
}

h1 {
  text-align: center;
}
a {
  text-decoration: none;
  color: rgb(53,106,188);
  text-decoration: underline;
  border-bottom: 3px solid;
}

.container {
  display: flex;
  flex-direction:column;
  align-content: center;
  align-items: center;
  text-align: center;
  
}

.card-banner {
  background-image: url('@/assets/case5.png');
  border-radius: 5%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.9); 
  
}

.clickclick {
  font-family: 'Pixelify Sans', sans-serif;
}


</style>