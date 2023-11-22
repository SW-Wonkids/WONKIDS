import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from '@/stores/auth'


export const useArticleStore = defineStore('article', () => {
    const authStore = useAuthStore()
    const token = ref(authStore.token)
    
    const articleList = ref([])

    // article 전체 조회
    const getArticleList = function () {
        axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/articles/',
        headers: {
            Authorization: `Token ${token.value}`
        }
        })
        .then(res => articleList.value = res.data)
        .catch(err => console.log(err))
    }

    const articleDetail = ref([])
    
    // article 하나 조회
    const getArticleDetail = function (pk) {
        axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/articles/${pk}`,
        headers: {
            Authorization: `Token ${token.value}`
        }
        })
        .then(res => articleDetail.value = res.data)
        .catch(err => console.log(err))
    }

    // article 생성
    const createArticle = function ({category, title, content}) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/articles/',
        data: {
            category,
            title,
            content
        },
        headers: {
            Authorization: `Token ${token.value}`
        }
    })
    }

    // article 수정
    const updateArticle = function ({category, title, content, pk}) {
        axios({
        method: 'put',
        url: `http://127.0.0.1:8000/api/v1/articles/${pk}/`,
        data: {
        category,
        title,
        content,
        },
        headers: {
            Authorization: `Token ${token.value}`
        }
    })
    .then((res) => {
        getArticleDetail(pk)
    })
    }
    
    // article 삭제
    const deleteArticle = function (pk) {
        axios({
            method: 'delete',
            url: `http://127.0.0.1:8000/api/v1/articles/${pk}/`,
            data: {
                pk
            },
            headers: {
                Authorization: `Token ${token.value}`
            }
        })
        .then(res => {
            getArticleList()
        })
    }

  
  return { articleList, getArticleList, articleDetail, getArticleDetail, createArticle, updateArticle, deleteArticle }
})
