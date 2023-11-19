import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
    const router = useRouter()
    const API_URL = 'http://127.0.0.1:8000'
    const token = ref(null)

    const signUp = function (payload) {
        const username = payload.username
        const password1 = payload.password1
        const password2 = payload.password2

        axios({
            method: 'post',
            url: `${API_URL}/accounts/signup/`,
            data: {
                username, password1, password2
            }
        })
        .then(res => {
            alert('회원가입이 성공적으로 완료되었습니다!')
        })
        .catch(err => {
            alert('정보를 다시 한번 확인해주세요!')
            console.log(err)
        })
    }

    return { API_URL, token, signUp }
})