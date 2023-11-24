<template>

  <div class="container koreanfont" style="font-size: 30px;margin-left: 55px;">
    <h3 style="text-align: center; font-size: 50px;">포켓몬 트레이너 {{ userinfo.username }} 의 프로필 페이지</h3>
    <hr>  
    <p>나의 이름 : {{ userinfo.username }}</p>
    <div v-if="userinfo.category">
      <p>안녕하세요! {{ userinfo.username }} 포켓몬 트레이너는 {{ userinfo.category }}를 잡으셨군요!</p>
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
      <div class="study">
        <p>
          <strong>기본 금리란?</strong>다양한 금융 제품에서 해당 금융 기관이 제공하는 금융 상품의 핵심적인 이자율을 나타냅니다.<br>
          예금 상품의 경우, 고객이 입금한 자금에 대한 기본 이자율입니다.<br>
          예금 금리는 예금 유형 및 금액, 예치 기간 등에 따라 다를 수 있습니다.<br>
        </p>
        <p>
          <strong>우대 금리란?</strong>금융 제품에서 특정 조건을 만족하는 고객들에게 적용되는 혜택적인 이자율을 나타냅니다.<br>
          이는 대출, 예금, 신용 카드 및 다른 금융 상품에서 찾을 수 있습니다.<br> 
          고객이 특정 조건을 충족하면 해당 금융 제품의 우대 금리를 받게 되어 이자 수익을 증대시킬 수 있습니다.
        </p>
        <p>이 웹사이트에 있는 금리는 모두 <strong>기본 금리</strong> 기준으로 볼 수 있습니다</p>
      </div>
      <br>
      <div v-if="pollstore.resultList">
      <div v-if="pollstore.resultList.deposits !== 'null'">
        <p>자세한 것은 <RouterLink :to="{name: 'banklist_deposit'}">정기예금 상품 페이지(Click HERE!)</RouterLink>를 확인해주세요!</p>
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
        <p>자세한 것은 <RouterLink :to="{name: 'banklist_savings'}">정기적금 상품 페이지(Click HERE!)</RouterLink>를 확인해주세요!</p>

        
          <div v-for="savingsProduct in pollstore.resultList.savings" :key="savingsProduct.id">
            <div class="card" >
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
      <p>안녕하세요! {{ userinfo.username }} 포켓몬 트레이너는 아직 포켓몬을 잡지 않으셨군요!</p>
      <p>지금 포켓몬 잡기에 참여하여 같은 포켓몬을 잡은 사람끼리 이야기하고</p>
      <p>추천 상품 목록도 확인해보세요!</p>
        <form @submit.prevent="goPollIndex">
          <input type="submit" value="포켓몬 잡으러 가기">
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
  background-color: azure;
}

p img {
  width: 15%;
}

</style>