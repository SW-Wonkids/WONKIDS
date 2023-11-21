import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth.js'
import { useArticleStore } from './articles.js'

export const useCommentStore = defineStore('comment', () => {
  const articleStore = useArticleStore()
  const authStore = useAuthStore()
  const token = ref(authStore.token)

  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/v1/articles/${pk}/comments/`,
      data: {
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articleStore.articleDetail.comment_set.push(res.data))
    .catch(err => console.log(err))
  }

  const deleteComment = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/articles/comments/${pk}/`,
      data: {
        pk
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
  }
  return { commentCreate, deleteComment }
})
