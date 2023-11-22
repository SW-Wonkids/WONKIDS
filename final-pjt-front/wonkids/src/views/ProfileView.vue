<template>
  <div>
    <h1>profile</h1>
    <p>{{ users }}</p>

  </div>
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:5173';
// User 목록 가져오기, this: 현재 컴포넌트의 인스턴스
export default {
    data() {
        return {
            users: [],  //User 정보 저장할 배열 
        };
    },
    mounted() {
        this.fetchUsers();
    },
    methods: {
        fetchUsers() {
            axios.get('api/users/')
                .then(res => {
                    this.users = res.data
                })
                .catch((error) => {
                    console.error('error is what:', error)
                });
        },
    },
};
</script>

<style scoped>

</style>