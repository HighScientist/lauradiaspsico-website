# Landing Page Laura Dias — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir uma landing page estática, responsiva e animada para a psicóloga Laura de Oliveira Dias (CRP 04/73471), pronta para hospedagem em domínio próprio.

**Architecture:** Site single-page 100% estático em `frontend/` — HTML semântico + um CSS com design tokens + JS vanilla. Carrosséis via Swiper.js (CDN). Scroll animations via IntersectionObserver próprio. Contato 100% por WhatsApp (sem backend). Imagens de `context/images/` são otimizadas para `frontend/assets/images/`.

**Tech Stack:** HTML5, CSS3 (custom properties, grid/flex), JavaScript vanilla (ES6), Swiper.js 11 (CDN), Google Fonts (Cormorant Garamond, Sacramento, Inter), Python/Pillow + cwebp (otimização de imagens), `python3 -m http.server` (preview local).

**Verificação:** Este é um site estático — não há suíte de testes unitários. Cada tarefa é verificada abrindo `http://localhost:8000` no navegador e conferindo o resultado descrito ("Expected"). Servidor local: `cd frontend && python3 -m http.server 8000`.

**Identidade visual / dados** — ver spec: `docs/superpowers/specs/2026-06-26-landing-page-laura-design.md`.
- Cores: creme `#EFE6DD` / `#F5EFE8`, taupe `#7D6B5D`, marrom escuro `#4A3F35`, preto suave `#2B2622`, card `#FBF8F4`, accent `#B89B7A`.
- Fontes: Cormorant Garamond (títulos), Sacramento (manuscrito), Inter (corpo).
- WhatsApp: `https://wa.me/5517981239566?text=` + mensagem.
- Instagram: `https://www.instagram.com/lauradiaspsico/` · Bio: `https://lauradiaspsico.keepo.bio`.

---

## Task 1: Scaffold do projeto e tokens de design

**Files:**
- Delete: `backend/` (não usado)
- Create: `frontend/index.html`
- Create: `frontend/css/styles.css`
- Create: `frontend/js/main.js`
- Create: `frontend/js/carousels.js`
- Create dirs: `frontend/assets/images/photos/`, `frontend/assets/images/posts/`, `frontend/assets/images/hero/`

- [ ] **Step 1: Criar estrutura de pastas e remover backend vazio**

```bash
cd /mnt/c/Users/AryelBezerra/Documents/Laura
rmdir backend 2>/dev/null || rm -rf backend
mkdir -p frontend/css frontend/js frontend/assets/images/photos frontend/assets/images/posts frontend/assets/images/hero
```

- [ ] **Step 2: Criar `frontend/index.html` com skeleton e `<head>` completo**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Laura Dias — Psicóloga | CRP 04/73471</title>
  <meta name="description" content="Psicoterapia online com Terapia Cognitivo-Comportamental (TCC) para adultos e idosos. Ansiedade, depressão, luto, psico-oncologia e avaliação neuropsicológica. Agende pelo WhatsApp." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&family=Sacramento&display=swap" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>
  <!-- nav, sections e footer entram nas próximas tasks -->
  <main></main>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script src="js/carousels.js" defer></script>
  <script src="js/main.js" defer></script>
</body>
</html>
```

- [ ] **Step 3: Criar `frontend/css/styles.css` com reset + design tokens**

```css
/* ===== Design tokens ===== */
:root {
  --cream: #EFE6DD;
  --cream-light: #F5EFE8;
  --card: #FBF8F4;
  --taupe: #7D6B5D;
  --brown: #4A3F35;
  --ink: #2B2622;
  --accent: #B89B7A;
  --white: #FFFFFF;

  --font-display: "Cormorant Garamond", Georgia, serif;
  --font-script: "Sacramento", cursive;
  --font-body: "Inter", system-ui, sans-serif;

  --maxw: 1140px;
  --radius: 18px;
  --shadow: 0 18px 50px -24px rgba(74, 63, 53, 0.35);
  --ease: cubic-bezier(0.22, 1, 0.36, 1);
}

*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
body {
  font-family: var(--font-body);
  color: var(--brown);
  background: var(--cream);
  line-height: 1.65;
  font-weight: 300;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
img { max-width: 100%; display: block; }
a { color: inherit; text-decoration: none; }

/* ===== Layout helpers ===== */
.container { width: 100%; max-width: var(--maxw); margin-inline: auto; padding-inline: 24px; }
.section { padding-block: clamp(64px, 9vw, 130px); }
.eyebrow {
  font-family: var(--font-body); font-size: .8rem; font-weight: 500;
  letter-spacing: .28em; text-transform: uppercase; color: var(--accent);
}
.script { font-family: var(--font-script); color: var(--taupe); font-weight: 400; line-height: 1; }
h1, h2, h3 { font-family: var(--font-display); font-weight: 500; color: var(--ink); line-height: 1.1; letter-spacing: .005em; }
h2.section-title { font-size: clamp(2.2rem, 5vw, 3.4rem); }
.star { color: var(--accent); }

/* ===== Botões ===== */
.btn {
  display: inline-flex; align-items: center; gap: .6em;
  font-family: var(--font-body); font-weight: 500; font-size: .98rem;
  padding: 15px 30px; border-radius: 999px; cursor: pointer;
  transition: transform .35s var(--ease), box-shadow .35s var(--ease), background .35s var(--ease);
  border: 1px solid transparent;
}
.btn-primary { background: var(--brown); color: var(--cream-light); }
.btn-primary:hover { transform: translateY(-3px); box-shadow: var(--shadow); background: var(--ink); }
.btn-ghost { background: transparent; color: var(--brown); border-color: var(--taupe); }
.btn-ghost:hover { background: var(--brown); color: var(--cream-light); }
```

- [ ] **Step 4: Criar `frontend/js/main.js` e `frontend/js/carousels.js` vazios (placeholders preenchidos depois)**

```js
// main.js — nav, smooth scroll, scroll reveal, botão flutuante (Tasks 4 e 13)
```

```js
// carousels.js — init dos Swipers (Tasks 6 e 11)
```

- [ ] **Step 5: Verificar no navegador**

Run: `cd frontend && python3 -m http.server 8000` e abrir `http://localhost:8000`
Expected: Página em branco com fundo creme (`#EFE6DD`), sem erros no console (Network: fonts e swiper carregando 200).

- [ ] **Step 6: Commit**

```bash
cd /mnt/c/Users/AryelBezerra/Documents/Laura
git add -A
git commit -m "feat: scaffold frontend + design tokens"
```

---

## Task 2: Otimização e curadoria das imagens

Copia e otimiza as imagens de `context/images/` para `frontend/assets/images/`, gerando WebP (qualidade 82, largura máx. 1280px) com fallback JPG.

**Files:**
- Create: `scripts/optimize-images.py`
- Output: `frontend/assets/images/photos/*.{webp,jpg}`, `.../posts/*.{webp,jpg}`, `.../hero/*`

- [ ] **Step 1: Criar `scripts/optimize-images.py`**

```python
#!/usr/bin/env python3
"""Otimiza imagens de context/images para frontend/assets/images (WebP + JPG fallback)."""
import pathlib
from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "context" / "images"
DST = ROOT / "frontend" / "assets" / "images"
MAXW = 1280

# Curadoria: fotos profissionais boas para carrossel/hero.
PHOTOS = ["photo_1", "photo_02", "photo_03", "photo_04", "photo_05",
          "photo_06", "photo_07", "photo_08", "photo_09", "photo_10"]
HERO = "photo_1"  # foto de destaque do hero
# Posts curados para o carrossel do Instagram (na ordem desejada).
POSTS = [f"post_{n:02d}" for n in range(1, 18)]

def save(src_path: pathlib.Path, out_base: pathlib.Path):
    img = ImageOps.exif_transpose(Image.open(src_path)).convert("RGB")
    if img.width > MAXW:
        h = round(img.height * MAXW / img.width)
        img = img.resize((MAXW, h), Image.LANCZOS)
    out_base.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_base.with_suffix(".webp"), "WEBP", quality=82, method=6)
    img.save(out_base.with_suffix(".jpg"), "JPEG", quality=82, optimize=True, progressive=True)
    print("ok:", out_base.name)

for name in PHOTOS:
    save(SRC / f"{name}.jpeg", DST / "photos" / name)
save(SRC / f"{HERO}.jpeg", DST / "hero" / "hero")
for name in POSTS:
    save(SRC / f"{name}.jpeg", DST / "posts" / name)
print("Concluído.")
```

- [ ] **Step 2: Rodar o script**

Run: `cd /mnt/c/Users/AryelBezerra/Documents/Laura && python3 scripts/optimize-images.py`
Expected: imprime `ok: ...` para cada imagem e `Concluído.` sem erro.

- [ ] **Step 3: Conferir saída**

Run: `ls -la frontend/assets/images/photos frontend/assets/images/posts frontend/assets/images/hero && du -sh frontend/assets/images`
Expected: arquivos `.webp` e `.jpg` presentes; total tipicamente < 2 MB.

> Nota de curadoria: durante a execução, abra as fotos e descarte qualquer uma de baixa qualidade/duplicada ajustando a lista `PHOTOS`/`POSTS`. `photo_1` é o retrato em pé (bom para hero). `post_01` (sofrer em silêncio) e `post_04` (terapia online, foto da Laura) são fortes para abrir o carrossel.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: otimizar e curar imagens para assets"
```

---

## Task 3: Navbar fixa + menu mobile + smooth scroll

**Files:**
- Modify: `frontend/index.html` (adicionar `<header class="nav">` no topo do body)
- Modify: `frontend/css/styles.css` (estilos do nav)
- Modify: `frontend/js/main.js` (estado scrolled + toggle do menu mobile)

- [ ] **Step 1: Adicionar markup do nav (logo no body, antes de `<main>`)**

```html
<header class="nav" id="nav">
  <div class="container nav__inner">
    <a href="#hero" class="nav__brand">Laura Dias <span class="nav__brand-sub">psicóloga</span></a>
    <button class="nav__toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav__menu" id="navMenu">
      <a href="#sobre">Quem sou eu</a>
      <a href="#abordagem">Abordagem</a>
      <a href="#publico">Para quem</a>
      <a href="#demandas">Atendimentos</a>
      <a href="#funciona">Como funciona</a>
      <a href="https://wa.me/5517981239566?text=Ol%C3%A1%2C%20Laura!%20Vim%20pelo%20seu%20site%20e%20gostaria%20de%20agendar%20um%20atendimento." class="btn btn-primary nav__cta" target="_blank" rel="noopener">Agendar</a>
    </nav>
  </div>
</header>
```

- [ ] **Step 2: CSS do nav (append em styles.css)**

```css
.nav { position: fixed; inset: 0 0 auto 0; z-index: 100; transition: background .4s var(--ease), box-shadow .4s var(--ease), padding .4s var(--ease); padding-block: 18px; }
.nav.scrolled { background: rgba(245,239,232,.92); backdrop-filter: blur(10px); box-shadow: 0 1px 0 rgba(125,107,93,.15); padding-block: 10px; }
.nav__inner { display: flex; align-items: center; justify-content: space-between; }
.nav__brand { font-family: var(--font-display); font-size: 1.5rem; color: var(--ink); font-weight: 600; }
.nav__brand-sub { font-family: var(--font-script); font-size: 1.2rem; color: var(--taupe); margin-left: 4px; }
.nav__menu { display: flex; align-items: center; gap: 30px; }
.nav__menu a:not(.btn) { font-size: .95rem; color: var(--brown); transition: color .3s; }
.nav__menu a:not(.btn):hover { color: var(--accent); }
.nav__cta { padding: 11px 24px; }
.nav__toggle { display: none; flex-direction: column; gap: 5px; background: none; border: 0; cursor: pointer; padding: 6px; }
.nav__toggle span { width: 26px; height: 2px; background: var(--brown); transition: .3s var(--ease); }
@media (max-width: 860px) {
  .nav__toggle { display: flex; }
  .nav__menu {
    position: fixed; inset: 0 0 0 auto; width: min(78vw, 320px);
    flex-direction: column; justify-content: center; gap: 28px;
    background: var(--cream-light); padding: 40px;
    transform: translateX(100%); transition: transform .45s var(--ease); box-shadow: var(--shadow);
  }
  .nav__menu.open { transform: translateX(0); }
  .nav.menu-open .nav__toggle span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
  .nav.menu-open .nav__toggle span:nth-child(2) { opacity: 0; }
  .nav.menu-open .nav__toggle span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
}
body { padding-top: 0; }
```

- [ ] **Step 3: JS do nav (substituir conteúdo de main.js)**

```js
// ===== Navbar: estado scrolled + menu mobile =====
const nav = document.getElementById('nav');
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

navToggle.addEventListener('click', () => {
  const open = navMenu.classList.toggle('open');
  nav.classList.toggle('menu-open', open);
  navToggle.setAttribute('aria-expanded', String(open));
  navToggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
});
navMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  navMenu.classList.remove('open');
  nav.classList.remove('menu-open');
  navToggle.setAttribute('aria-expanded', 'false');
}));
```

- [ ] **Step 4: Verificar**

Run: servidor local + abrir no navegador (desktop e DevTools mobile)
Expected: nav fixa transparente; ao rolar > 40px ganha fundo creme com blur. Em < 860px aparece o hambúrguer que abre/fecha o menu lateral e vira "X". (Âncoras ainda apontam para seções que serão criadas.)

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: navbar fixa com menu mobile e estado scrolled"
```

---

## Task 4: Seção Hero

**Files:**
- Modify: `frontend/index.html` (primeira `<section id="hero">` dentro de `<main>`)
- Modify: `frontend/css/styles.css`

- [ ] **Step 1: Markup do hero**

```html
<section class="hero" id="hero">
  <div class="container hero__inner">
    <div class="hero__text" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> Psicóloga · CRP 04/73471</p>
      <h1 class="hero__title">Você não precisa carregar<br />esse peso <span class="script hero__script">sozinho</span></h1>
      <p class="hero__lead">Psicoterapia online com abordagem em Terapia Cognitivo-Comportamental para adultos e idosos. Um espaço seguro, sem julgamentos, para cuidar de você.</p>
      <div class="hero__actions">
        <a href="https://wa.me/5517981239566?text=Ol%C3%A1%2C%20Laura!%20Vim%20pelo%20seu%20site%20e%20gostaria%20de%20agendar%20um%20atendimento." class="btn btn-primary" target="_blank" rel="noopener">Agendar pelo WhatsApp</a>
        <a href="#sobre" class="btn btn-ghost">Conhecer meu trabalho</a>
      </div>
    </div>
    <div class="hero__media" data-reveal>
      <picture>
        <source srcset="assets/images/hero/hero.webp" type="image/webp" />
        <img src="assets/images/hero/hero.jpg" alt="Laura Dias, psicóloga" width="520" height="640" loading="eager" />
      </picture>
      <span class="hero__badge"><span class="star">✦</span> Atendimento<br />100% online</span>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS do hero (append)**

```css
.hero { position: relative; padding-top: 150px; padding-bottom: clamp(60px, 8vw, 110px); background: radial-gradient(120% 90% at 80% 0%, var(--cream-light) 0%, var(--cream) 55%); }
.hero__inner { display: grid; grid-template-columns: 1.05fr .95fr; gap: clamp(30px, 5vw, 70px); align-items: center; }
.hero__title { font-size: clamp(2.6rem, 6vw, 4.6rem); margin: 18px 0 22px; }
.hero__script { font-size: 1.25em; }
.hero__lead { max-width: 30em; font-size: 1.08rem; color: var(--taupe); }
.hero__actions { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 32px; }
.hero__media { position: relative; justify-self: center; }
.hero__media img { width: min(440px, 80vw); border-radius: 260px 260px 30px 30px; object-fit: cover; aspect-ratio: 5/6; box-shadow: var(--shadow); }
.hero__badge { position: absolute; bottom: 24px; left: -18px; background: var(--white); color: var(--brown); font-size: .82rem; line-height: 1.3; padding: 14px 18px; border-radius: 14px; box-shadow: var(--shadow); }
@media (max-width: 860px) {
  .hero__inner { grid-template-columns: 1fr; text-align: center; }
  .hero__lead { margin-inline: auto; }
  .hero__actions { justify-content: center; }
  .hero__media { order: -1; }
}
```

- [ ] **Step 3: Verificar**

Run: servidor local
Expected: hero com título grande serifado, "sozinho" em manuscrito, dois botões, foto da Laura com cantos arredondados estilo "arco" e badge "Atendimento 100% online". Responsivo: empilha no mobile com a foto acima do texto.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: seção hero"
```

---

## Task 5: Seção "Quem sou eu?" + carrossel de fotos

**Files:**
- Modify: `frontend/index.html` (`<section id="sobre">`)
- Modify: `frontend/css/styles.css`
- Modify: `frontend/js/carousels.js` (init do Swiper de fotos)

- [ ] **Step 1: Markup da seção sobre + carrossel**

```html
<section class="section sobre" id="sobre">
  <div class="container sobre__inner">
    <div class="sobre__text" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> Quem sou eu?</p>
      <h2 class="section-title">Laura de Oliveira Dias</h2>
      <p class="sobre__lead">Sou psicóloga formada pela Universidade Federal do Triângulo Mineiro (UFTM). Mineira, morando em São Paulo. Atuo na clínica e no contexto hospitalar, com formação em Neuropsicologia e Psico-oncologia.</p>
      <p>Acredito que pedir ajuda não te torna fraco — te torna humano. Meu trabalho é oferecer um espaço de escuta acolhedor, onde você possa se reconhecer, entender suas emoções e encontrar caminhos mais leves.</p>
      <ul class="sobre__tags">
        <li>Psicóloga pela UFTM</li>
        <li>Psicóloga clínica e hospitalar</li>
        <li>Neuropsicóloga</li>
        <li>Psico-oncologia</li>
        <li>Abordagem Cognitivo-Comportamental</li>
        <li>Mineira morando em SP</li>
      </ul>
      <!-- TODO (preencher com a Laura): pós-graduações, cursos e experiências hospitalares específicas. -->
    </div>
    <div class="sobre__media" data-reveal>
      <div class="swiper photos-swiper">
        <div class="swiper-wrapper">
          <!-- Slides gerados: repetir para photo_1, photo_02 ... photo_10 -->
          <div class="swiper-slide"><picture><source srcset="assets/images/photos/photo_1.webp" type="image/webp"><img src="assets/images/photos/photo_1.jpg" alt="Laura Dias, psicóloga" loading="lazy"></picture></div>
          <div class="swiper-slide"><picture><source srcset="assets/images/photos/photo_02.webp" type="image/webp"><img src="assets/images/photos/photo_02.jpg" alt="Laura Dias, psicóloga" loading="lazy"></picture></div>
          <div class="swiper-slide"><picture><source srcset="assets/images/photos/photo_03.webp" type="image/webp"><img src="assets/images/photos/photo_03.jpg" alt="Laura Dias, psicóloga" loading="lazy"></picture></div>
          <div class="swiper-slide"><picture><source srcset="assets/images/photos/photo_04.webp" type="image/webp"><img src="assets/images/photos/photo_04.jpg" alt="Laura Dias, psicóloga" loading="lazy"></picture></div>
          <div class="swiper-slide"><picture><source srcset="assets/images/photos/photo_05.webp" type="image/webp"><img src="assets/images/photos/photo_05.jpg" alt="Laura Dias, psicóloga" loading="lazy"></picture></div>
          <div class="swiper-slide"><picture><source srcset="assets/images/photos/photo_06.webp" type="image/webp"><img src="assets/images/photos/photo_06.jpg" alt="Laura Dias, psicóloga" loading="lazy"></picture></div>
        </div>
        <div class="swiper-pagination"></div>
      </div>
    </div>
  </div>
</section>
```

> Durante a execução, inclua apenas os slides cujas fotos passaram na curadoria da Task 2.

- [ ] **Step 2: CSS (append)**

```css
.sobre__inner { display: grid; grid-template-columns: 1.05fr .95fr; gap: clamp(34px, 5vw, 70px); align-items: center; }
.sobre__lead { font-size: 1.12rem; color: var(--brown); margin: 18px 0 16px; }
.sobre .sobre__text p { color: var(--taupe); }
.sobre__tags { list-style: none; padding: 0; margin: 26px 0 0; display: flex; flex-wrap: wrap; gap: 10px; }
.sobre__tags li { font-size: .85rem; color: var(--brown); background: var(--card); border: 1px solid rgba(125,107,93,.18); padding: 8px 16px; border-radius: 999px; }
.photos-swiper { border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }
.photos-swiper .swiper-slide img { width: 100%; aspect-ratio: 4/5; object-fit: cover; }
.photos-swiper .swiper-pagination-bullet { background: var(--white); opacity: .6; }
.photos-swiper .swiper-pagination-bullet-active { background: var(--accent); opacity: 1; }
@media (max-width: 860px) { .sobre__inner { grid-template-columns: 1fr; } }
```

- [ ] **Step 3: Init do Swiper de fotos (carousels.js)**

```js
// ===== Carrossel de fotos profissionais =====
if (document.querySelector('.photos-swiper')) {
  new Swiper('.photos-swiper', {
    loop: true,
    speed: 800,
    autoplay: { delay: 3800, disableOnInteraction: false },
    pagination: { el: '.photos-swiper .swiper-pagination', clickable: true },
  });
}
```

- [ ] **Step 4: Verificar**

Run: servidor local
Expected: seção com texto à esquerda, tags em "pílulas", e carrossel de fotos à direita rodando sozinho (autoplay) com paginação clicável e swipe no touch. Empilha no mobile.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: seção quem sou eu + carrossel de fotos"
```

---

## Task 6: Seção Abordagem (TCC)

**Files:**
- Modify: `frontend/index.html` (`<section id="abordagem">`)
- Modify: `frontend/css/styles.css`

- [ ] **Step 1: Markup**

```html
<section class="section abordagem" id="abordagem">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> Abordagem</p>
      <h2 class="section-title">Terapia Cognitivo-Comportamental</h2>
    </div>
    <div class="abordagem__grid">
      <p class="abordagem__lead" data-reveal>A forma como você interpreta o que acontece influencia diretamente como você se sente e age. O que você diz para si mesmo molda sua autoestima e sua maneira de enfrentar a vida. Na TCC, trabalhamos juntos para identificar padrões de pensamento que geram sofrimento e construir estratégias práticas para lidar com eles — com foco no presente e nos seus objetivos.</p>
      <ul class="abordagem__pillars">
        <li data-reveal><span class="star">✦</span><h3>Baseada em evidências</h3><p>Uma das abordagens com maior comprovação científica de eficácia.</p></li>
        <li data-reveal><span class="star">✦</span><h3>Foco no presente</h3><p>Direcionada a soluções e aos desafios que você vive hoje.</p></li>
        <li data-reveal><span class="star">✦</span><h3>Ferramentas práticas</h3><p>Recursos que você leva para o dia a dia, além das sessões.</p></li>
        <li data-reveal><span class="star">✦</span><h3>Trabalho colaborativo</h3><p>Um processo ativo, construído junto, no seu tempo.</p></li>
      </ul>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS (append) — inclui `.section-head` reutilizável**

```css
.section-head { text-align: center; max-width: 40rem; margin: 0 auto 50px; }
.section-head .eyebrow { display: block; margin-bottom: 10px; }
.abordagem { background: var(--cream-light); }
.abordagem__grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(30px, 5vw, 64px); align-items: start; }
.abordagem__lead { font-size: 1.2rem; line-height: 1.7; color: var(--brown); font-family: var(--font-display); }
.abordagem__pillars { list-style: none; padding: 0; margin: 0; display: grid; gap: 22px; }
.abordagem__pillars li { background: var(--card); border-radius: var(--radius); padding: 24px 26px; border: 1px solid rgba(125,107,93,.12); }
.abordagem__pillars .star { font-size: 1.1rem; }
.abordagem__pillars h3 { font-size: 1.35rem; margin: 6px 0 4px; }
.abordagem__pillars p { color: var(--taupe); font-size: .98rem; }
@media (max-width: 860px) { .abordagem__grid { grid-template-columns: 1fr; } }
```

- [ ] **Step 3: Verificar**

Run: servidor local
Expected: título centralizado, parágrafo serifado à esquerda e 4 cards de pilares à direita. Empilha no mobile.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: seção abordagem TCC"
```

---

## Task 7: Seção Público-Alvo

**Files:**
- Modify: `frontend/index.html` (`<section id="publico">`)
- Modify: `frontend/css/styles.css`

- [ ] **Step 1: Markup**

```html
<section class="section publico" id="publico">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> Para quem é</p>
      <h2 class="section-title">Atendimento a Adultos e Idosos</h2>
    </div>
    <div class="publico__grid">
      <article class="publico__card" data-reveal>
        <h3>Adultos</h3>
        <p>Para quem enfrenta ansiedade, sobrecarga, dores emocionais ou momentos de transição — e quer construir uma relação mais saudável consigo mesmo.</p>
      </article>
      <article class="publico__card" data-reveal>
        <h3>Idosos</h3>
        <p>Acolhimento para lidar com perdas, mudanças, solidão, adoecimento e os desafios dessa fase da vida — com respeito, escuta e cuidado.</p>
      </article>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS (append)**

```css
.publico__grid { display: grid; grid-template-columns: 1fr 1fr; gap: 26px; }
.publico__card { background: var(--card); border-radius: var(--radius); padding: clamp(28px, 4vw, 46px); border: 1px solid rgba(125,107,93,.12); box-shadow: var(--shadow); }
.publico__card h3 { font-size: 1.9rem; margin-bottom: 10px; }
.publico__card p { color: var(--taupe); }
@media (max-width: 700px) { .publico__grid { grid-template-columns: 1fr; } }
```

- [ ] **Step 3: Verificar** — Run: servidor local. Expected: dois cards lado a lado (Adultos / Idosos), empilhando em telas estreitas.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: seção público-alvo"
```

---

## Task 8: Seção Demandas e Atendimentos + bloco Neuropsicologia

**Files:**
- Modify: `frontend/index.html` (`<section id="demandas">`)
- Modify: `frontend/css/styles.css`

- [ ] **Step 1: Markup**

```html
<section class="section demandas" id="demandas">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> Demandas e atendimentos</p>
      <h2 class="section-title">Como posso te ajudar</h2>
    </div>
    <div class="demandas__grid">
      <article class="dcard" data-reveal><h3>Ansiedade</h3><p>Crises, preocupação constante e a sensação de estar sempre em alerta.</p></article>
      <article class="dcard" data-reveal><h3>Depressão</h3><p>Tristeza persistente, desânimo e perda de sentido e prazer nas coisas.</p></article>
      <article class="dcard" data-reveal><h3>Luto</h3><p>Perdas e despedidas: um espaço para elaborar a dor no seu tempo.</p></article>
      <article class="dcard" data-reveal><h3>Câncer · Psico-oncologia</h3><p>Apoio ao paciente oncológico e seus familiares em todas as fases do tratamento.</p></article>
      <article class="dcard" data-reveal><h3>Doenças crônicas</h3><p>Suporte emocional para conviver com diagnósticos e tratamentos de longa duração.</p></article>
      <article class="dcard" data-reveal><h3>Autoestima e autocrítica</h3><p>Transformar o diálogo interno duro em uma relação mais gentil consigo.</p></article>
    </div>

    <div class="neuro" data-reveal>
      <div class="neuro__text">
        <p class="eyebrow"><span class="star">✦</span> Neuropsicologia</p>
        <h3 class="neuro__title">Avaliação Neuropsicológica</h3>
        <p>Investigação aprofundada de funções como atenção, memória e funções executivas. A avaliação auxilia no diagnóstico, gera um laudo e orienta tratamentos, adaptações e autoconhecimento.</p>
      </div>
      <ul class="neuro__tags">
        <li>TDAH</li>
        <li>TEA (Espectro Autista)</li>
        <li>Outras neurodivergências</li>
        <li>Demais transtornos</li>
      </ul>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS (append)**

```css
.demandas__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
.dcard { background: var(--card); border-radius: var(--radius); padding: 30px 28px; border: 1px solid rgba(125,107,93,.12); transition: transform .4s var(--ease), box-shadow .4s var(--ease); }
.dcard:hover { transform: translateY(-6px); box-shadow: var(--shadow); }
.dcard h3 { font-size: 1.45rem; margin-bottom: 8px; }
.dcard p { color: var(--taupe); font-size: .96rem; }
.neuro { margin-top: 30px; background: var(--brown); color: var(--cream-light); border-radius: var(--radius); padding: clamp(30px, 5vw, 54px); display: grid; grid-template-columns: 1.3fr 1fr; gap: 34px; align-items: center; }
.neuro__title { color: var(--cream-light); font-size: 2rem; margin: 8px 0 12px; }
.neuro__text p:last-child { color: rgba(245,239,232,.82); }
.neuro .eyebrow { color: var(--accent); }
.neuro__tags { list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; gap: 12px; align-content: center; }
.neuro__tags li { border: 1px solid rgba(245,239,232,.35); border-radius: 999px; padding: 10px 20px; font-size: .9rem; }
@media (max-width: 920px) { .demandas__grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 760px) { .demandas__grid { grid-template-columns: 1fr; } .neuro { grid-template-columns: 1fr; } }
```

- [ ] **Step 3: Verificar** — Expected: grid de 6 cards (3 colunas no desktop) com hover de elevação; bloco escuro "Avaliação Neuropsicológica" com pílulas TDAH/TEA/etc. Responsivo (2 col → 1 col).

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: seção demandas + neuropsicologia"
```

---

## Task 9: Seção "Como funciona o atendimento"

**Files:**
- Modify: `frontend/index.html` (`<section id="funciona">`)
- Modify: `frontend/css/styles.css`

- [ ] **Step 1: Markup**

```html
<section class="section funciona" id="funciona">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> Como funciona</p>
      <h2 class="section-title">O atendimento, passo a passo</h2>
    </div>
    <div class="funciona__grid">
      <article class="fcard" data-reveal><span class="fcard__num">01</span><h3>100% online</h3><p>De onde você estiver, com a mesma qualidade. A distância não impede o cuidado.</p></article>
      <article class="fcard" data-reveal><span class="fcard__num">02</span><h3>Sessões de 50 min</h3><p>Um encontro semanal de aproximadamente 50 minutos, no seu ritmo.</p></article>
      <article class="fcard" data-reveal><span class="fcard__num">03</span><h3>Sigilo profissional</h3><p>Tudo o que você compartilha é protegido pelo sigilo — um espaço seguro.</p></article>
      <article class="fcard" data-reveal><span class="fcard__num">04</span><h3>Primeira conversa</h3><p>Acolhemos sua demanda e definimos juntos o melhor caminho para você.</p></article>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS (append)**

```css
.funciona { background: var(--cream-light); }
.funciona__grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; }
.fcard { background: var(--card); border-radius: var(--radius); padding: 32px 26px; border: 1px solid rgba(125,107,93,.12); }
.fcard__num { font-family: var(--font-display); font-size: 2.2rem; color: var(--accent); display: block; margin-bottom: 8px; }
.fcard h3 { font-size: 1.3rem; margin-bottom: 6px; }
.fcard p { color: var(--taupe); font-size: .95rem; }
@media (max-width: 920px) { .funciona__grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 560px) { .funciona__grid { grid-template-columns: 1fr; } }
```

- [ ] **Step 3: Verificar** — Expected: 4 cards numerados (01–04). Responsivo 4→2→1.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: seção como funciona o atendimento"
```

---

## Task 10: Seção Instagram + carrossel de posts

**Files:**
- Modify: `frontend/index.html` (`<section id="instagram">`)
- Modify: `frontend/css/styles.css`
- Modify: `frontend/js/carousels.js` (Swiper de posts)

- [ ] **Step 1: Markup (cada slide é um link para o Instagram)**

```html
<section class="section insta" id="instagram">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow"><span class="star">✦</span> @lauradiaspsico</p>
      <h2 class="section-title">Acompanhe no Instagram</h2>
    </div>
    <div class="swiper posts-swiper" data-reveal>
      <div class="swiper-wrapper">
        <!-- Repetir para post_01 ... post_17 (apenas os curados) -->
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_01.webp" type="image/webp"><img src="assets/images/posts/post_01.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_04.webp" type="image/webp"><img src="assets/images/posts/post_04.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_02.webp" type="image/webp"><img src="assets/images/posts/post_02.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_03.webp" type="image/webp"><img src="assets/images/posts/post_03.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_09.webp" type="image/webp"><img src="assets/images/posts/post_09.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_06.webp" type="image/webp"><img src="assets/images/posts/post_06.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
        <a class="swiper-slide post-slide" href="https://www.instagram.com/lauradiaspsico/" target="_blank" rel="noopener"><picture><source srcset="assets/images/posts/post_14.webp" type="image/webp"><img src="assets/images/posts/post_14.jpg" alt="Post de @lauradiaspsico" loading="lazy"></picture></a>
      </div>
      <div class="swiper-button-prev"></div>
      <div class="swiper-button-next"></div>
    </div>
    <div class="insta__cta" data-reveal>
      <a href="https://www.instagram.com/lauradiaspsico" class="btn btn-ghost" target="_blank" rel="noopener">Seguir @lauradiaspsico</a>
      <a href="https://lauradiaspsico.keepo.bio" class="btn btn-ghost" target="_blank" rel="noopener">Todos os links</a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS (append)**

```css
.posts-swiper { padding-bottom: 8px; }
.post-slide { width: 280px; border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }
.post-slide img { width: 100%; aspect-ratio: 4/5; object-fit: cover; transition: transform .5s var(--ease); }
.post-slide:hover img { transform: scale(1.05); }
.posts-swiper .swiper-button-prev, .posts-swiper .swiper-button-next { color: var(--brown); }
.posts-swiper .swiper-button-prev::after, .posts-swiper .swiper-button-next::after { font-size: 22px; }
.insta__cta { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin-top: 40px; }
```

- [ ] **Step 3: Init Swiper de posts (carousels.js, append)**

```js
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
```

- [ ] **Step 4: Verificar** — Expected: carrossel horizontal de posts (vários visíveis), autoplay + setas + swipe; cada post abre o Instagram em nova aba; hover dá leve zoom. Botões CTA abaixo.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: seção instagram + carrossel de posts"
```

---

## Task 11: Seção Contato + rodapé + botão flutuante de WhatsApp

**Files:**
- Modify: `frontend/index.html` (`<section id="contato">`, `<footer>`, botão flutuante)
- Modify: `frontend/css/styles.css`

- [ ] **Step 1: Markup do contato, footer e botão flutuante (após a seção instagram, antes de `</main>` e dos scripts)**

```html
<section class="section contato" id="contato">
  <div class="container contato__inner" data-reveal>
    <p class="eyebrow"><span class="star">✦</span> Agenda aberta</p>
    <h2 class="contato__title">Vamos conversar?</h2>
    <p class="contato__lead">Dar o primeiro passo já é um ato de cuidado. Reserve um momento para cuidar de você.</p>
    <a href="https://wa.me/5517981239566?text=Ol%C3%A1%2C%20Laura!%20Vim%20pelo%20seu%20site%20e%20gostaria%20de%20agendar%20um%20atendimento." class="btn btn-primary contato__btn" target="_blank" rel="noopener">Agendar pelo WhatsApp</a>
    <p class="contato__alt">ou pelo Instagram <a href="https://www.instagram.com/lauradiaspsico" target="_blank" rel="noopener">@lauradiaspsico</a></p>
  </div>
</section>

<footer class="footer">
  <div class="container footer__inner">
    <div>
      <p class="footer__name">Laura de Oliveira Dias</p>
      <p class="footer__role">Psicóloga · CRP 04/73471</p>
    </div>
    <p class="footer__meta">Atendimento online · Sigilo profissional garantido</p>
    <div class="footer__links">
      <a href="https://www.instagram.com/lauradiaspsico" target="_blank" rel="noopener">Instagram</a>
      <a href="https://lauradiaspsico.keepo.bio" target="_blank" rel="noopener">Links</a>
      <a href="https://wa.me/5517981239566" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
  <p class="footer__copy">© 2026 Laura de Oliveira Dias · Todos os direitos reservados</p>
</footer>

<a class="wa-float" href="https://wa.me/5517981239566?text=Ol%C3%A1%2C%20Laura!%20Vim%20pelo%20seu%20site%20e%20gostaria%20de%20agendar%20um%20atendimento." target="_blank" rel="noopener" aria-label="Agendar pelo WhatsApp">
  <svg viewBox="0 0 32 32" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.1 1.6 5.9L4 29l8.3-1.6c1.7.9 3.6 1.4 5.7 1.4 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-4.9 1 1-4.8-.3-.4C5.5 18 5 16.5 5 15 5 9.5 9.9 5 16 5s11 4.5 11 10-4.9 9.8-11 9.8zm5.5-7.4c-.3-.2-1.8-.9-2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.1-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5 0-.2-.7-1.7-1-2.3-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.4z"/></svg>
</a>
```

- [ ] **Step 2: CSS (append)**

```css
.contato { background: radial-gradient(120% 120% at 50% 0%, var(--cream-light), var(--cream)); text-align: center; }
.contato__title { font-size: clamp(2.4rem, 6vw, 4rem); margin: 12px 0 16px; }
.contato__lead { max-width: 34rem; margin: 0 auto 30px; color: var(--taupe); font-size: 1.1rem; }
.contato__btn { font-size: 1.05rem; padding: 17px 38px; }
.contato__alt { margin-top: 18px; font-size: .95rem; color: var(--taupe); }
.contato__alt a { color: var(--accent); font-weight: 500; }
.footer { background: var(--ink); color: var(--cream-light); padding: 50px 0 26px; }
.footer__inner { display: flex; flex-wrap: wrap; gap: 22px; justify-content: space-between; align-items: center; }
.footer__name { font-family: var(--font-display); font-size: 1.4rem; }
.footer__role { color: rgba(245,239,232,.7); font-size: .9rem; }
.footer__meta { color: rgba(245,239,232,.7); font-size: .9rem; }
.footer__links { display: flex; gap: 20px; }
.footer__links a { font-size: .9rem; transition: color .3s; }
.footer__links a:hover { color: var(--accent); }
.footer__copy { text-align: center; color: rgba(245,239,232,.45); font-size: .8rem; margin-top: 30px; }
.wa-float { position: fixed; right: 20px; bottom: 20px; z-index: 90; width: 56px; height: 56px; border-radius: 50%; background: #25D366; color: #fff; display: grid; place-items: center; box-shadow: 0 10px 30px -8px rgba(37,211,102,.6); transition: transform .35s var(--ease); }
.wa-float:hover { transform: scale(1.08); }
@media (max-width: 640px) { .footer__inner { flex-direction: column; text-align: center; justify-content: center; } }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```

- [ ] **Step 3: Verificar** — Expected: seção final centralizada com CTA grande; rodapé escuro com nome+CRP e links; botão verde flutuante de WhatsApp fixo no canto inferior direito (abre conversa com mensagem pré-preenchida). Clicar nos CTAs abre `wa.me` corretamente.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: seção contato, rodapé e botão flutuante de whatsapp"
```

---

## Task 12: Scroll reveal animations (IntersectionObserver)

**Files:**
- Modify: `frontend/css/styles.css` (estados de reveal)
- Modify: `frontend/js/main.js` (observer)

- [ ] **Step 1: CSS dos estados (append)**

```css
[data-reveal] { opacity: 0; transform: translateY(28px); transition: opacity .8s var(--ease), transform .8s var(--ease); }
[data-reveal].is-visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  [data-reveal] { opacity: 1 !important; transform: none !important; transition: none !important; }
}
```

- [ ] **Step 2: JS do observer (main.js, append)**

```js
// ===== Scroll reveal =====
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealEls = document.querySelectorAll('[data-reveal]');
if (reduceMotion || !('IntersectionObserver' in window)) {
  revealEls.forEach(el => el.classList.add('is-visible'));
} else {
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('is-visible'), (i % 4) * 80);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  revealEls.forEach(el => io.observe(el));
}
```

- [ ] **Step 3: Verificar** — Expected: ao rolar, blocos com `data-reveal` entram com fade + slide-up suave, em leve cascata. Com "reduce motion" ativo no SO, tudo aparece estático. Conteúdo nunca fica invisível se o JS falhar? (Se preocupar, garantir fallback — o observer roda no load.)

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: scroll reveal animations com prefers-reduced-motion"
```

---

## Task 13: SEO, Open Graph, favicon e dados estruturados

**Files:**
- Modify: `frontend/index.html` (`<head>`)
- Create: `frontend/assets/favicon.svg`
- Create: `frontend/assets/og-image.jpg` (a partir de uma foto)

- [ ] **Step 1: Gerar OG image (1200×630) a partir do hero**

```bash
cd /mnt/c/Users/AryelBezerra/Documents/Laura
python3 -c "
from PIL import Image, ImageOps
im = ImageOps.fit(Image.open('context/images/photo_1.jpeg').convert('RGB'), (1200,630), Image.LANCZOS)
im.save('frontend/assets/og-image.jpg','JPEG',quality=85)
print('og ok')
"
```

- [ ] **Step 2: Criar `frontend/assets/favicon.svg` (estrela ✦ da marca)**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#4A3F35"/><path d="M50 18c3 18 14 29 32 32-18 3-29 14-32 32-3-18-14-29-32-32 18-3 29-14 32-32z" fill="#B89B7A"/></svg>
```

- [ ] **Step 3: Adicionar meta tags ao `<head>` (após a tag description)**

```html
<link rel="canonical" href="https://SEU-DOMINIO.com.br/" />
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />
<meta name="theme-color" content="#EFE6DD" />
<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content="Laura Dias — Psicóloga | TCC online" />
<meta property="og:description" content="Psicoterapia online (TCC) para adultos e idosos. Ansiedade, depressão, luto, psico-oncologia e avaliação neuropsicológica." />
<meta property="og:image" content="https://SEU-DOMINIO.com.br/assets/og-image.jpg" />
<meta property="og:locale" content="pt_BR" />
<meta name="twitter:card" content="summary_large_image" />
<!-- Dados estruturados -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Psychologist",
  "name": "Laura de Oliveira Dias",
  "honorificSuffix": "CRP 04/73471",
  "jobTitle": "Psicóloga",
  "url": "https://SEU-DOMINIO.com.br/",
  "image": "https://SEU-DOMINIO.com.br/assets/og-image.jpg",
  "knowsAbout": ["Terapia Cognitivo-Comportamental", "Psico-oncologia", "Neuropsicologia", "Ansiedade", "Depressão", "Luto"],
  "availableLanguage": "Portuguese",
  "sameAs": ["https://www.instagram.com/lauradiaspsico"]
}
</script>
```

> `SEU-DOMINIO.com.br` é placeholder — substituir pelo domínio real após a compra (documentado no README, Task 14).

- [ ] **Step 4: Verificar** — Expected: aba do navegador com favicon de estrela e título correto. `view-source` mostra as meta OG e o JSON-LD. Sem erros no console.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: SEO, Open Graph, favicon e JSON-LD"
```

---

## Task 14: README de deploy + QA final responsivo

**Files:**
- Create: `frontend/README.md`
- Create: `README.md` (raiz, breve)

- [ ] **Step 1: Criar `frontend/README.md`**

Conteúdo (deve incluir, em PT-BR):
- O que é o site (landing page estática da Laura).
- **Testar localmente:** `cd frontend && python3 -m http.server 8000` → abrir `http://localhost:8000`.
- **Antes de publicar:** substituir `SEU-DOMINIO.com.br` em `index.html` (canonical, og:image, JSON-LD) pelo domínio real.
- **Atualizar fotos/posts:** colocar novas imagens em `context/images/`, ajustar listas em `scripts/optimize-images.py`, rodar o script e atualizar os `<picture>` no `index.html`.
- **Deploy (escolher uma opção):**
  - **Netlify/Vercel (grátis):** arrastar a pasta `frontend/` no painel ou conectar o repositório; apontar o domínio comprado nos DNS conforme instruções do serviço.
  - **Hospedagem comum (cPanel/FTP):** subir o conteúdo de `frontend/` para a pasta `public_html`.
  - **GitHub Pages:** publicar `frontend/` (ou mover para a raiz) e configurar o domínio customizado.
- Observação: site 100% estático, sem backend nem build.

- [ ] **Step 2: Criar `README.md` na raiz (curto)**

Conteúdo: descrição do projeto, link para o spec (`docs/superpowers/specs/...`) e para `frontend/README.md`, e nota de que `context/` guarda as fontes originais (não publicar).

- [ ] **Step 3: QA final no navegador (DevTools responsivo)**

Verificar em larguras 375px (mobile), 768px (tablet), 1280px (desktop):
- Nav, hero, todas as 8 seções, os 2 carrosséis, botão flutuante e rodapé renderizam sem overflow horizontal.
- Carrosséis arrastam no touch; CTAs de WhatsApp abrem `wa.me` com mensagem; links de Instagram/bio abrem em nova aba.
- Console sem erros.

Expected: tudo conforme acima. Corrigir qualquer overflow/erro encontrado antes do commit.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "docs: README de deploy + QA final responsivo"
```

---

## Self-Review (cobertura do spec)

- §5 seções 1–8 → Tasks 4,5,6,7,8,9,10,11 ✓
- §6 carrosséis (fotos + posts) → Tasks 5 e 10 ✓
- §6 navbar/menu/botão flutuante → Tasks 3 e 11 ✓
- §4 design system (cores/fontes/estrela) → Task 1 ✓
- Animações scroll → Task 12 ✓
- §8 performance/SEO/acessibilidade (lazy, alt, OG, JSON-LD, reduced-motion) → Tasks 2,12,13 ✓
- §9 conformidade CFP (nome+CRP no hero e rodapé, sem promessas) → Tasks 4,11 (copy) ✓
- §10 hospedagem/README → Task 14 ✓
- §3 dados confirmados (CRP 04/73471, WhatsApp, nome) → embutidos no markup ✓

Sem placeholders de implementação pendentes além dos marcados intencionalmente para a Laura preencher (currículo detalhado) e o domínio real (substituir após compra). Nomes de classes/IDs consistentes entre HTML, CSS e JS.
```
