<template>
  <div style="margin-left: 55px;">
    <div class="koreanfont">
    <div class="accordion koreanfont" id="accordionExample">
      
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            
            <strong>왜 저축을 해야 할까요?</strong>
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>저축은 절약하여 모아 두는 것을 말합니다.</strong><br>
            1. 사고 싶은 물건을 사거나 돈이 많이 드는 물건을 살 때, 하고 싶은 일을 할 때 쓸 수 있어요<br>
            2. 예상치 못한 사고 때문에 돈이 갑자기 필요한 경우 사용할 수 있어요<br>
            3. 저축을 위해 꼭 필요한 물건만 사게 되어 낭비를 줄일 수 있어요<br>
            4. 나중에 나이가 들어 일하던 곳에서 은퇴하거나 일을 하지 못하더라도 걱정 없어요<br>
            <hr>
            <strong>잠깐! 저축이 좋아보인다고 해서 계획 없이 저축을 해서는 안돼요</strong> <br>
            정기 예금이나 정기 적금의 경우 정해진 기간보다 빨리 돈을 찾게 되면 약속한 이자보다 훨씬 적은 이자를 받거나<br>
            전혀 받지 못할 수도 있기 때문입니다. 그러니 돈 쓸 계획을 미리 세운 뒤에 저축을 하는 지혜가 필요하겠죠?<br>
            <hr>
            <strong>그럼 저축의 종류 중 정기 예금과 정기 적금을 알아볼까요?</strong>
            
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            <strong>정기 예금에 대해 알아볼까요?</strong>
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>정기 예금은 큰 돈을 한꺼번에 맡기고 정해진 기간 후에 찾아가는 금융 상품</strong>입니다.<br>
            정해진 기간 이후에 찾아가면 약속한 이자와 함께 맡긴 돈을 찾아올 수 있어요<br>
            주로 3개월 단위로 가입하며 오래 맡길수록 더 높은 이자를 받을 수 있어요<br>
            <hr>
            <strong>그럼 이자가 뭘까요?</strong> 여기서 이자는 저축 금리와 같은 말입니다<br>
            금리는 빌려준 돈이나 예금 따위에 붙는 이자, 또는 그 비율을 의미하는데요<br>
            저축 금리는 저축을 했을 때 그 저축에 붙는 이자, 또는 그 비율을 의미한다고 할 수 있습니다<br>
            금리가 높아질수록 포켓몬 트레이너인 당신이 받게 될 돈도 많아집니다<br>
            <hr>
            <strong>그럼 어떤 정기 예금 상품이 있는지 확인해볼까요?</strong>
            <span><RouterLink :to="{name: 'banklist_deposit'}">정기예금(DEPOSIT)</RouterLink></span>
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
            <strong>정기 적금에 대해 알아볼까요?</strong>
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>정기 적금은 매달 일정한 돈을 정해진 기간 동안 저금한 뒤 약속한 날짜에 찾아가는 금융 상품</strong>입니다<br>
            약속한 날짜에 찾아가면 약속한 이자와 함께 그동안 저금한 돈을 가져올 수 있어요<br>
            정기 적금은 주로 1년 이상으로 가입할 수 있고 오래 맡길수록 더 높은 이자를 받을 수 있어요<br>
            <hr>
            <strong>그럼 이자가 뭘까요?</strong> 여기서 이자는 저축 금리와 같은 말입니다<br>
            금리는 빌려준 돈이나 예금 따위에 붙는 이자, 또는 그 비율을 의미하는데요<br>
            저축 금리는 저축을 했을 때 그 저축에 붙는 이자, 또는 그 비율을 의미한다고 할 수 있습니다<br>
            금리가 높아질수록 포켓몬 트레이너인 당신이 받게 될 돈도 많아집니다<br>
            <hr>
            <strong>그럼 어떤 정기 적금 상품이 있는지 확인해볼까요?</strong>
            <span><RouterLink :to="{name: 'banklist_savings'}">적금(SAVINGS)</RouterLink></span>
          </div>
          </div>  
        </div>
      </div>
    </div>

    <hr>

    <h2 class="koreanfont">근처 은행 카카오맵으로 보기</h2>
    <RouterLink :to="{name: 'bankmap'}" class="koreanfont" style="font-size: 20px;">>>>근처 은행 검색</RouterLink>
  </div>
</template>

<script setup>

</script>

<style scoped>
a {
  text-decoration: none;
  color: rgb(53,106,188);
  border: 3px solid white;
  border-radius: 5px;
  background-color: lightgray;
}

span {
  margin: 5px;
}


</style>