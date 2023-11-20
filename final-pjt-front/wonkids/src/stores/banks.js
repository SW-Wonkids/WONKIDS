import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBankStore = defineStore('bank', () => {
  const banks = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getBanks = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/bank_deposit/`
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
        banks.value = res.data
      })
      .catch(err => console.log(err))
  }
  return {banks, API_URL,getBanks }
}, {persist: true}) 