import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
  
export const useBankStore = defineStore('bank', () => {
  const banks = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 정기예금 데이터 가져오는 함수 
  const getBanksDeposit = function () {
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

  // 적금 데이터 가져오는 함수
  const getBanksSavings = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/bank_savings/`
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
        banks.value = res.data
      })
      .catch(err => console.log(err))
  }
  return { banks, API_URL, getBanksDeposit, getBanksSavings }
}, {persist: true})
