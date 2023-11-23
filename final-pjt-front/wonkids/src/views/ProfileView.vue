<template>

  <div class="container koreanfont" style="margin-left: 55px;">
    <h3 style="text-align: center;">포켓몬 트레이너 {{ userinfo.username }} 의 프로필 페이지</h3>
    <hr>  
    <p>나의 이름 : {{ userinfo.username }}</p>
    hello {{ userinfo.category }}
    <div v-if="userinfo.category">
      <p>나의 결과는!! {{ userinfo.category }}</p>
      <p v-if="userinfo.category === '파이리'"><img src="@/assets/pairi.jpg" alt=""></p>
      <p v-if="userinfo.category === '꼬부기'"><img src="@/assets/kobugi.webp" alt=""></p>
      <p v-if="userinfo.category === '피카츄'"><img src="@/assets/pikachu.webp" alt=""></p>


      <hr>
      <p>다시 한번 유형 검사를 하고 싶다면?</p>
      <p>아래의 버튼을 클릭하세요!</p>
      <form @submit.prevent="goPollIndex">
        <input type="submit" value="유형검사 다시 하기">
      </form>

      <hr>
      <p>결과에 따른 추천 상품 목록</p>
      <p>이건 기본금리이고 기본금리, 우대금리에 대한 설명을 작성한 뒤에</p>
      <p>금융 정보를 상세하게 볼 수 있는 페이지로 가서 참고할 수 있게 글을 작성</p>
      <div v-if="pollstore.resultList">
      <div v-if="pollstore.resultList.deposits !== 'null'">
        <p>자세한 것은 정기예금 상품 페이지를 확인해주세요!</p>
       
        <div v-for="depositProduct in pollstore.resultList.deposits" :key="depositProduct.id">
          <div class="card">
            <div class="card-body">
              <h3>{{ depositProduct.fin_prdt_nm }}</h3>
              <h4>{{ depositProduct.kor_co_nm }}</h4>
              <p>금리 (6개월): {{ depositProduct.save_trm_6  + '%'}}</p>
              <p>금리 (12개월): {{ depositProduct.save_trm_12 + '%' }}</p>
              <p>금리 (24개월): {{ depositProduct.save_trm_24 + '%' }}</p>
              <p>금리 (36개월): {{ depositProduct.save_trm_36 + '%' }}</p>
            </div>
          </div>
        </div>
  
      </div>
      <div v-if="pollstore.resultList.savings !== 'null'">
        <p>자세한 것은 정기적금 상품 페이지를 확인해주세요!</p>

        
          <div v-for="savingsProduct in pollstore.resultList.savings" :key="savingsProduct.id">
            <div class="card">
              <div class="card-body">
                <h3>{{ savingsProduct.fin_prdt_nm }}</h3>
                <h4>{{ savingsProduct.kor_co_nm }}</h4>
                <p>금리 (6개월): {{ savingsProduct.save_trm_6 + '%' }}</p>
                <p>금리 (12개월): {{ savingsProduct.save_trm_12 + '%' }}</p>
                <p>금리 (24개월): {{ savingsProduct.save_trm_24 + '%' }}</p>
                <p>금리 (36개월): {{ savingsProduct.save_trm_36 + '%' }}</p>
              </div>
            </div>
          </div>
        
      </div>

      
    </div>
  </div>
  
    <div v-else>
      <p>나의 유형은? 지금 유형검사에 참여하여 나의 유형도 알고</p>
      <p>추천 상품 목록도 확인해보세요!</p>
        <form @submit.prevent="goPollIndex">
          <input type="submit" value="유형검사 하러 가기">
        </form>
    </div>

    

  </div>
</template>

<script setup>

import { onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile'
import { usePollStore } from '@/stores/polls'
import { useRouter } from 'vue-router'

const router = useRouter()
const goPollIndex = () => {
  router.push({ name: 'poll' })
}

const store = useProfileStore()
const pollstore = usePollStore()
const userinfo = store.userinfo

onMounted(() => {
    store.getProfile()
    pollstore.getResult()
})

</script>

<style scoped>
hr {
  border: 10px solid green;
  border-radius: 5px;
}

.card {
  margin-top: 20px;
}
</style>