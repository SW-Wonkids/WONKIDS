import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia' 

export const useProfileStore = defineStore('profile', () => {
  const users = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`
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
