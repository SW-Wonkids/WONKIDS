<template>
  <!--BankListDeposit > BankDeposit 정기예금 vue page -->
  <!-- <div class="koreanfont">
    <h5>{{ bank.id }}.</h5>
    <p>공시 제출월[YYYYMM] : {{ bank.dcls_month }}</p>
    <p>금융회사 명 : {{ bank.kor_co_nm }}</p>
    <p class="product">금융 상품명 : <RouterLink :to="{name: 'BankDepositDetail', params: {id: bank.id}}">{{ bank.fin_prdt_nm }} </RouterLink></p>
    <p>저축 기간 {{ bank.save_trm_6 }}(개월) - 저축 금리 {{ bank.intr_rate_6 }}</p>
    <p>저축 기간 {{ bank.save_trm_12 }}(개월) - 저축 금리 {{ bank.intr_rate_12 }}</p>
    <p>저축 기간 {{ bank.save_trm_24 }}(개월) - 저축 금리 {{ bank.intr_rate_24 }}</p>
    <p>저축 기간 {{ bank.save_trm_36 }}(개월) - 저축 금리 {{ bank.intr_rate_36 }}</p>
    <hr>

  </div> -->
  <div class="ag-format-container koreanfont">
    <div class="ag-courses_box">
      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            공시 제출월[YYYYMM]
          </div>

          <div class="ag-courses-item_date-box">
            Day:
            <span class="ag-courses-item_date">
              {{ bank.dcls_month }}
            </span>
          </div>
        </a>
      </div>

      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            금융회사 명 :
          </div>

          <div class="ag-courses-item_date-box">
            Name:
            <span class="ag-courses-item_date">
              {{ bank.kor_co_nm }}
            </span>
          </div>
        </a>
      </div>

      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            저축 기간
          </div>

          <div class="ag-courses-item_date-box">
          
            <span class="ag-courses-item_date">
              <RouterLink :to="{name: 'BankDepositDetail', params: {id: bank.id}}">{{ bank.fin_prdt_nm }} </RouterLink>
            </span>
          </div>
        </a>
      </div>

      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            저축 기간 {{ bank.save_trm_6 }}(개월)
          </div>

          <div class="ag-courses-item_date-box">
            저축 금리 :
            <span class="ag-courses-item_date">
              {{ bank.intr_rate_6 }}
            </span>
          </div>
        </a>
      </div>

      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            저축 기간 {{ bank.save_trm_12 }}(개월)
          </div>

          <div class="ag-courses-item_date-box">
            저축 금리 :
            <span class="ag-courses-item_date">
              {{ bank.intr_rate_12 }}
            </span>
          </div>
        </a>
      </div>

      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            저축 기간 {{ bank.save_trm_24 }}(개월)
          </div>
      
          <div class="ag-courses-item_date-box">
            저축 금리 :
            <span class="ag-courses-item_date">
              {{ bank.intr_rate_24 }}
            </span>
          </div>
        </a>
      </div>

      <div class="ag-courses_item">
        <a href="#" class="ag-courses-item_link">
          <div class="ag-courses-item_bg"></div>

          <div class="ag-courses-item_title">
            저축 기간 {{ bank.save_trm_36 }}(개월)
          </div>

          <div class="ag-courses-item_date-box">
            저축 금리 :
            <span class="ag-courses-item_date">
              {{ bank.intr_rate_36 }}
            </span>
          </div>
        </a>
      </div>

    </div>
  </div>
</template>

<script setup>
import { RouterLink} from 'vue-router'
defineProps({
  bank: Object
})
</script>

<style scoped>
.product { 

  text-decoration: rgb(53,106,188) wavy underline;
}
a{
  text-decoration: none;
}
.ag-format-container {
  width: 1142px;
  margin: 0 auto;
}


body {
  background-color: #000;
}
.ag-courses_box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;

  padding: 50px 0;
}
.ag-courses_item {
  -ms-flex-preferred-size: calc(33.33333% - 30px);
  flex-basis: calc(33.33333% - 30px);

  margin: 0 15px 30px;

  overflow: hidden;

  border-radius: 28px;
}
.ag-courses-item_link {
  display: block;
  padding: 30px 20px;
  background-color: #121212;

  overflow: hidden;

  position: relative;
}
.ag-courses-item_link:hover,
.ag-courses-item_link:hover .ag-courses-item_date {
  text-decoration: none;
  color: #FFF;
}
.ag-courses-item_link:hover .ag-courses-item_bg {
  -webkit-transform: scale(10);
  -ms-transform: scale(10);
  transform: scale(10);
}
.ag-courses-item_title {
  min-height: 87px;
  margin: 0 0 25px;

  overflow: hidden;

  font-weight: bold;
  font-size: 30px;
  color: #FFF;

  z-index: 2;
  position: relative;
}
.ag-courses-item_date-box {
  font-size: 18px;
  color: #FFF;

  z-index: 2;
  position: relative;
}
.ag-courses-item_date {
  font-weight: bold;
  color: #f9b234;

  -webkit-transition: color .5s ease;
  -o-transition: color .5s ease;
  transition: color .5s ease
}
.ag-courses-item_bg {
  height: 128px;
  width: 128px;
  background-color: #f9b234;

  z-index: 1;
  position: absolute;
  top: -75px;
  right: -75px;

  border-radius: 50%;

  -webkit-transition: all .5s ease;
  -o-transition: all .5s ease;
  transition: all .5s ease;
}
.ag-courses_item:nth-child(2n) .ag-courses-item_bg {
  background-color: #3ecd5e;
}
.ag-courses_item:nth-child(3n) .ag-courses-item_bg {
  background-color: #e44002;
}
.ag-courses_item:nth-child(4n) .ag-courses-item_bg {
  background-color: #952aff;
}
.ag-courses_item:nth-child(5n) .ag-courses-item_bg {
  background-color: #cd3e94;
}
.ag-courses_item:nth-child(6n) .ag-courses-item_bg {
  background-color: #4c49ea;
}



@media only screen and (max-width: 979px) {
  .ag-courses_item {
    -ms-flex-preferred-size: calc(50% - 30px);
    flex-basis: calc(50% - 30px);
  }
  .ag-courses-item_title {
    font-size: 24px;
  }
}

@media only screen and (max-width: 767px) {
  .ag-format-container {
    width: 96%;
  }

}
@media only screen and (max-width: 639px) {
  .ag-courses_item {
    -ms-flex-preferred-size: 100%;
    flex-basis: 100%;
  }
  .ag-courses-item_title {
    min-height: 72px;
    line-height: 1;

    font-size: 24px;
  }
  .ag-courses-item_link {
    padding: 22px 40px;
  }
  .ag-courses-item_date-box {
    font-size: 16px;
  }
}
</style>