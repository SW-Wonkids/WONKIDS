<template>
<div class="container">
    <div class="background koreanfont">
        <h1 style="margin-top: 35px; margin-bottom: 5px; font-weight: 800;">404 ERROR</h1>
        <h1>정상적인 접근이 아닙니다!&#x1F603;</h1>
        <p style="margin-top: 10px;">이전 페이지로 돌아가주세요!	&#129505;</p>
    </div>
</div>
</template>

<script setup>

</script>

<style scoped>
.background {
    background-image: url('@/assets/sleep.png');
    height: 90vh;
    border-radius: 45%;
    width: 70%;
        
}

h1, p {
    color: white;
    font-weight: 100;
    text-align: center;
    border-top: 50px;
    margin-top: 50px;
}
.container {
    display: flex;
    flex-direction:column;
    align-content: center;
    align-items: center;
    text-align: center;
}
</style>