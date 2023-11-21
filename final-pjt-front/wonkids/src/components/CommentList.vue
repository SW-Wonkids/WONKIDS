<template>
  <li>
    <span class="comment-id">{{ comment.id }}</span>. 
    <span class="comment-content">{{ comment.content }}</span>
    <button @click="deleteComment">삭제</button>
  </li>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { useCommentStore } from '@/stores/comments'
import { useRouter } from 'vue-router'

const router = useRouter()
const articleStore = useArticleStore()
const store = useCommentStore()

const props = defineProps({
  comment: Object
})

const deleteComment = function () {
  store.deleteComment(props.comment.id)
  // 페이지 이동
  // router.push({ name: 'detail', params: {pk: pk} })
  router.go(0)
}
</script>

<style scoped>

</style>