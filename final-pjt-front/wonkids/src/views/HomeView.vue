<!-- bootstrap text code -->
<template>
  <div class="koreanfont" style="margin-left: 55px; margin-right: 55px;">
    <RouterLink :to="{name: 'home'}"><img src="@/assets/wonkids.png" class="d-block w-100" style="max-width: 500px; height: auto; margin: auto; display: block; width: 60%"></RouterLink>
    
    <div id="carouselExampleCaptions" class="carousel slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="@/assets/exchange.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
          <h5>예금 & 적금 금융상품의 금리를 비교해볼 수 있어요!</h5>
          <p>금융 상품을 금융회사를 기준으로 필터링해 금리 정보를 비교할 수 있어요!<br>
          각 상품을 클릭하면 상세 페이지로 이동해서 가입방법, 우대조건을 알아봅시다.</p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="@/assets/poll.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
          <h5>설문조사를 활용한 금융상품 추천 서비스</h5>
          <p>포켓몬을 활용한 미니 설문조사를 통해 나의 성향을 파악하고 필요한 금융상품을 추천받을 수 있는 서비스입니다. 
            
          </p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="@/assets/bank.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
          <h5>환율 계산기</h5>
          <p>환율을 계산할 수 있는 계산기가 있어요.<br> 해외에서 내가 가진 돈이 얼마인지 함께 계산해봐요</p>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>

<style scoped>
.icon-bar {
  width: 50px; /* Set a specific width */
  background-color: #555; /* Dark-grey background */
}

.icon-bar a {
  display: block; /* Make the links appear below each other instead of side-by-side */
  text-align: center; /* Center-align text */
  padding: 16px; /* Add some padding */
  transition: all 0.3s ease; /* Add transition for hover effects */
  color: white; /* White text color */
  font-size: 20px; /* Increased font-size */
}

.icon-bar a:hover {
  background-color: #000; /* Add a hover color */
}

.active {
  background-color: #04AA6D; /* Add an active/current color */
}

</style>