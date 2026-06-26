// ===== Carrossel de fotos profissionais =====
if (document.querySelector('.photos-swiper')) {
  new Swiper('.photos-swiper', {
    loop: true,
    speed: 800,
    autoplay: { delay: 3800, disableOnInteraction: false },
    pagination: { el: '.photos-swiper .swiper-pagination', clickable: true },
  });
}
