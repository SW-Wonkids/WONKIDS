import axios from 'axios'
import { ref } from 'vue'
import { useAuthStore } from './auth.js'
import { defineStore } from 'pinia' 

export const useProfileStore = defineStore('profile', () => {
  const users = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const authStore = useAuthStore()
  const token = ref(authStore.token)

  
  const getProfile = function () {

    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`, 
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
        users.value = res.data
      })
      .catch(err => console.log(err))
  }
  return {users, API_URL, getProfile}
}, {persist: true})
