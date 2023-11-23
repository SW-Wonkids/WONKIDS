<template>
  <!--BankListDeposit > BankDeposit > BankDepositDetailView 정기예금 vue page -->
  <div class="koreanfont">
    <h2>정기예금 상품 List 출력</h2>

    <label for="companyFilter">금융회사 명:</label>
    <select v-model="selectedCompany" @change="filterBanks">
      <option value="">선택하세용</option>
      <option v-for="company in uniqueCompanies" :key="company">{{ company }}</option>
    </select>
    <hr>

    <!--BankDeposit.vue 금융상품 전체목록 출력-->
    <BankDeposit
      v-for="bank in filteredBanks"
      :key="bank.id"
      :bank="bank"/>

  </div>
</template>

<script setup>
import BankDeposit from '@/components/BankDeposit.vue'

import { useBankStore } from '@/stores/banks'
import { ref, computed } from 'vue'

const store = useBankStore()
const selectedCompany = ref('')
const uniqueCompanies = computed(() => Array.from(new Set(store.banks.map(bank => bank.kor_co_nm))))
const filteredBanks = computed(() => {
  return selectedCompany.value
    ? store.banks.filter(bank => bank.kor_co_nm === selectedCompany.value)
    : store.banks
});

const filterBanks = () => {
  // 사용자가 선택한 회사를 변경할 때 호출되는 함수
  // filteredBanks computed property를 업데이트하는 로직
  filteredBanks.value = selectedCompany.value
    ? store.banks.filter(bank => bank.kor_co_nm === selectedCompany.value)
    : store.banks

}
</script>

<style scoped>

</style>