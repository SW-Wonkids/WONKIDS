import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from '@/stores/auth'


export const usePollStore = defineStore('poll', () => {
  const authStore = useAuthStore()
  const token = ref(authStore.token)
  
  const sendResult = function (pokemon) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/poll/',
      data: {
        pokemon
      },
      headers: {
          Authorization: `Token ${token.value}`
      }
    })
  }

  const getResult = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/poll/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
  }
  return { sendResult }
})
  