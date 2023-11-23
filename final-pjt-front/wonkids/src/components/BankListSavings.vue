<template>
  <!--BankListSavings > BankSavings > BankDepositSavingsView 적금 vue page -->
  <div class="koreanfont">
    <h2>정기적금 상품 List 출력</h2>

    <!--금융회사 검색 기능-->
    <label for="companyFilter">금융회사 명:</label>
    <select v-model="selectedCompany" @change="filterBanks">
      <option value="">선택하세용</option>
      <option 
      v-for="company in uniqueCompanies"
      :key="company">
      {{ company }}
      </option>
    </select>
    <hr>
    <BankSavings
      v-for="bank in filteredBanks"
      :key="bank.id"
      :bank="bank"/>

  </div>
</template>

<script setup>
import BankSavings from '@/components/BankSavings.vue'
import { useBankStore } from '@/stores/banks'
import { ref, computed } from 'vue'

const store = useBankStore()
const selectedCompany = ref('')
const uniqueCompanies = computed(() => Array.from(new Set(store.banks.map(bank => bank.kor_co_nm))))
const filteredBanks = computed(() => {
  return selectedCompany.value ? store.banks.filter(bank => bank.kor_co_nm === selectedCompany.value) : store.banks
})

const filterBanks = () => {
  filteredBanks.value = selectedCompany.value ? store.banks.filter(bank => bank.kor_co_nm === selectedCompany.value) : store.banks
}
</script>

<style scoped>

</style>