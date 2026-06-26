// ===== Carrossel de fotos profissionais =====
if (document.querySelector('.photos-swiper')) {
  new Swiper('.photos-swiper', {
    loop: true,
    speed: 800,
    autoplay: { delay: 3800, disableOnInteraction: false },
    pagination: { el: '.photos-swiper .swiper-pagination', clickable: true },
  });
}

// ===== Carrossel de posts do Instagram =====
if (document.querySelector('.posts-swiper')) {
  new Swiper('.posts-swiper', {
    slidesPerView: 'auto',
    spaceBetween: 22,
    loop: true,
    speed: 700,
    autoplay: { delay: 3000, disableOnInteraction: false },
    navigation: { nextEl: '.posts-swiper .swiper-button-next', prevEl: '.posts-swiper .swiper-button-prev' },
  });
}
