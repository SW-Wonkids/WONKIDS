import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

// export const useArticleStore = defineStore('article', () => {
//   const articleList = ref([])
//   const getArticleList = function () {
//     axios({
//       method: 'get',
//       url: 'http://127.0.0.1:8000/api/v1/articles/'
//     })
//     .then(res => articleList.value = res.data)
//     .catch(err => console.log(err))
//   }
//   const articleDetail = ref([])
//   const getArticleDetail = function (pk) {
//     axios({
//       method: 'get',
//       url: `http://127.0.0.1:8000/api/v1/articles/${pk}`
//     })
//     .then(res => articleDetail.value = res.data)
//     .catch(err => console.log(err))
//   }

//   const createArticle = function ({pokemon, title, content}) {
//     axios({
//       method: 'post',
//       url: 'http://127.0.0.1:8000/api/v1/articles/',
//       data: {
//         pokemon,
//         title,
//         content
//       }
//     })
//   }
//   return { articleList, getArticleList, articleDetail, getArticleDetail, createArticle }
// })
