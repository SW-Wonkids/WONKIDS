<template>
  <div class="post-details">
    <h1>게시글 상세 정보</h1>
    <div class="post-info">
      <p class="category">{{ store.articleDetail.category?.name }}</p>
      <p class="post-id">{{ store.articleDetail.id }} 번 글</p>
      <p class="post-title">{{ store.articleDetail.title }}</p>
    </div>
    <hr>
    <div class="post-dates">
      <p class="created-date">작성일: {{ store.articleDetail.created_at }}</p>
      <p class="updated-date">수정일: {{ store.articleDetail.updated_at }}</p>
    </div>
    <hr>
    <p class="post-content">{{ store.articleDetail.content }}</p>
    <button @click="updateArticle">수정</button>
    <button @click="deleteArticle">삭제</button>
    <hr>
    <CommentCreate 
      :postPk="store.articleDetail.id"
    />
    <ul class="comment-list">
      <CommentList
        v-for="comment in store.articleDetail.comment_set"
        :key="comment.id"
        class="comment-item"
        :comment="comment"
      />
    </ul>
    <hr>
  </div>
</template>

<script setup>
import CommentCreate from '../components/CommentCreate.vue';
import CommentList from '../components/CommentList.vue';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/articles';

const router = useRouter()
const route = useRoute()
const store = useArticleStore()
onMounted(() => {
  store.getArticleDetail(route.params.pk)
})

const updateArticle = function () {
  router.push({ name: 'article-update'})
}

const deleteArticle = function () {
  const pk = store.detailPost.id
  store.deleteArticle(pk)
  router.push({ name: 'article-list' })
}
</script>


<style scoped>
.post-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #fff;
}

.post-info {
  margin-bottom: 20px;
}

.category {
  font-size: 16px;
  color: #333;
}

.post-id {
  font-size: 14px;
  color: #888;
}

.post-title {
  font-size: 24px;
  font-weight: bold;
  margin-top: 10px;
  margin-bottom: 20px;
}

.post-dates {
  font-size: 12px;
  color: #888;
  margin-bottom: 10px;
}

.post-content {
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 20px;
}

.comment-list {
  list-style: none;
  padding: 0;
}

.comment-item {
  font-size: 14px;
  margin-bottom: 10px;
}

.comment-id {
  font-weight: bold;
  margin-right: 5px;
}

.comment-content {
  margin-left: 5px;
}
</style>