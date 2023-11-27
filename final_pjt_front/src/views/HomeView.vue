<template class="container">
  <main>
    <section class="seciton-center section-tan site-slogan">
      <p>
        <h2>
        "20대에 2억 모으는 쉽고 빠른 비밀 공개! 🚀 돈 버는 효과적인 전략과 함께
        해요!"
      </h2>
      </p>
    </section>
  </main>
  <div class="sortbox">
    <div
      id="carouselExampleAutoplaying"
      class="carousel slide"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img
            src="../assets/bankmain.jpg"
            class="d-block w-100"
            sizes="50%"
            alt="이미지1"
          />
        </div>
        <div class="carousel-item">
          <img
            src="../assets/bank2.jpg"
            class="d-block w-100"
            alt="이미지2"
            sizes="50%"
          />
        </div>
        <div class="carousel-item">
          <img
            src="../assets/bank3.jpg"
            class="d-block w-100"
            alt="이미지3"
            sizes="50%"
          />
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleAutoplaying"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleAutoplaying"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.seciton-center {
  text-align: center;
}

.seciton-tan {
  background: #f6f5ea;
}

.sortbox {
  display: flex;
  justify-content: center;
  align-items: center;

}

.carousel {
  width: 70%;
  /* justify-content: center; */
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
