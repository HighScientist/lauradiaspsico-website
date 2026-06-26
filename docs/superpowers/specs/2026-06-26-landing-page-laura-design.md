# Landing Page — Laura de Oliveira Dias (Psicóloga)

**Data:** 2026-06-26
**Status:** Spec aprovada (aguardando revisão final do usuário)

## 1. Objetivo

Landing page single-page, estática e responsiva para a psicóloga **Laura de Oliveira Dias (CRP 04/73471)**, apresentando sua atuação e convertendo visitantes (vindos principalmente do Instagram, em mobile) em agendamentos via WhatsApp. O site deve ser dinâmico visualmente (carrosséis de imagens + scroll animations), com design derivado da identidade visual já existente da profissional, e ficar pronto para hospedagem em domínio próprio comprado pelo usuário.

## 2. Decisões travadas

| Tema | Decisão |
|------|---------|
| Stack | HTML/CSS/JS puro (sem framework, sem build obrigatório) |
| Backend | Nenhum — site 100% estático. A pasta `backend/` será removida |
| Contato/Agendamento | Botão WhatsApp direto (`wa.me/5517981239566`) com mensagem pré-preenchida |
| Posts do Instagram | Imagens curadas estáticas (as 17 já baixadas em `context/images/`) |
| Carrosséis | Swiper.js via CDN (touch/swipe, leve) |
| Scroll animations | IntersectionObserver próprio (sem lib pesada) |
| Idioma | PT-BR |
| Conformidade | Normas de publicidade do CFP (nome + CRP visíveis, sem promessa de resultado, sem sensacionalismo, sem depoimentos) |

## 3. Dados da profissional (confirmados)

- **Nome completo:** Laura de Oliveira Dias
- **CRP:** 04/73471 (Minas Gerais)
- **Formação:** Psicóloga pela UFTM (Universidade Federal do Triângulo Mineiro)
- **Atuação:** Psicóloga clínica e hospitalar · Neuropsicóloga · Psico-oncologia
- **Abordagem:** Terapia Cognitivo-Comportamental (TCC)
- **Origem:** Mineira morando em SP
- **WhatsApp:** +55 17 98123-9566 → `https://wa.me/5517981239566`
- **Instagram:** https://www.instagram.com/lauradiaspsico/ (@lauradiaspsico)
- **Bio (links):** https://lauradiaspsico.keepo.bio

> **A confirmar com a Laura na fase de conteúdo:** cidade/região de atendimento, currículo detalhado (pós/cursos, experiências hospitalares específicas), e-mail de contato (opcional). Esses campos ficam marcados como placeholder no conteúdo, sem inventar dados.

## 4. Identidade visual (derivada das fontes)

### Paleta
- Fundo creme/bege: `#EFE6DD` (e variação mais clara `#F5EFE8`)
- Taupe/marrom médio (texto secundário, traços): `#7D6B5D`
- Marrom escuro (texto principal): `#4A3F35`
- Preto suave (detalhes): `#2B2622`
- Branco / off-white para cards: `#FFFFFF` / `#FBF8F4`
- Accent dourado/caramelo sutil para a estrela e hovers: `#B89B7A`

### Tipografia (Google Fonts)
- **Títulos (display serifado):** Cormorant Garamond
- **Destaques manuscritos:** Sacramento (ou Dancing Script)
- **Corpo (sans serif):** Inter (ou Lato)

### Elementos gráficos
- Estrela ✦ de 4 pontas (motivo recorrente)
- Cantos arredondados suaves, sombras leves, generoso espaço em branco
- Linhas finas conectoras (estilo "constelação de atributos" do post "Quem sou eu?")

## 5. Estrutura de seções (single-page, navbar com âncoras)

1. **Hero** — nome, "Psicóloga · CRP 04/73471", frase de acolhimento, botão WhatsApp (CTA primário), foto da profissional, motivo estrela ✦. Parallax sutil.
2. **Quem sou eu?** — bio em primeira pessoa, formação (UFTM), CRP, currículo e experiência (clínica/hospitalar/neuro/psico-oncologia), no estilo "constelação de atributos". Inclui **Carrossel A — fotos profissionais** (photo_*.jpeg).
3. **Abordagem (TCC)** — explicação acessível da Terapia Cognitivo-Comportamental: o que é, como funciona, para quem ajuda.
4. **Público-Alvo** — foco em **Adultos e Idosos** (com nota acolhedora sobre cada fase).
5. **Demandas e Atendimentos** — grid de cards:
   - Câncer / Psico-oncologia
   - Doenças Crônicas
   - Luto
   - Depressão
   - Ansiedade
   - Bloco **Neuropsicologia**: avaliação neuropsicológica — TDAH, TEA e outras neurodivergências/transtornos.
6. **Como funciona o atendimento** — Online · sessões de 50 minutos · sigilo profissional · pontos práticos (como é a primeira sessão, plataforma, etc.).
7. **Instagram** — **Carrossel B — posts curados** (post_*.jpeg) + CTA para @lauradiaspsico e link da bio (keepo).
8. **Contato / Agendamento** — CTA WhatsApp reforçado + Instagram + rodapé com nome, CRP, e aviso de sigilo/LGPD.

## 6. Componentes interativos

- **Navbar fixa** com links âncora, smooth scroll, estado "scrolled" (encolhe/ganha fundo). Menu hambúrguer no mobile.
- **Carrossel A (fotos):** Swiper, autoplay suave, loop, paginação, swipe touch.
- **Carrossel B (posts IG):** Swiper, formato quadrado/retrato, cada slide linka para o Instagram.
- **Botão flutuante de WhatsApp** fixo no canto (mobile e desktop).
- **Scroll reveal:** elementos entram com fade + slide-up via IntersectionObserver (com `prefers-reduced-motion` respeitado).

## 7. Estrutura de arquivos

```
frontend/
  index.html
  css/
    styles.css            (design system: variáveis, tipografia, layout, componentes, animações)
  js/
    main.js               (navbar, smooth scroll, scroll reveal, botão flutuante)
    carousels.js          (init dos Swipers)
  assets/
    images/
      photos/             (fotos profissionais otimizadas p/ web)
      posts/              (posts IG otimizados p/ web)
      hero/               (imagem(ns) do hero)
    icons/                (estrela, whatsapp, instagram — SVG inline ou arquivos)
    og-image.jpg          (preview p/ WhatsApp/redes)
    favicon.svg / .ico
  README.md               (passo a passo de deploy no domínio)
docs/superpowers/specs/   (este spec)
context/                  (fontes originais: imagens — não publicado)
```

> As imagens em `context/images/` serão otimizadas (redimensionadas + comprimidas, idealmente WebP com fallback JPG) e copiadas para `frontend/assets/images/`. O `context/` permanece como fonte/arquivo, fora do deploy.

## 8. Performance, SEO e acessibilidade

- Mobile-first, responsivo (breakpoints para celular, tablet, desktop).
- Imagens otimizadas, `loading="lazy"`, dimensões definidas (evitar layout shift).
- Meta tags: `title`, `description`, OpenGraph + Twitter Card (preview no WhatsApp/redes), `lang="pt-BR"`, canonical.
- Dados estruturados JSON-LD `Person` / `MedicalBusiness` (psicóloga) para SEO local.
- Acessibilidade: contraste adequado, `alt` em imagens, navegação por teclado, `prefers-reduced-motion`, landmarks semânticos.
- Favicon + `apple-touch-icon`.

## 9. Conformidade (CFP / LGPD)

- Nome completo + CRP visíveis (hero e rodapé).
- Sem promessa de cura/resultado, sem sensacionalismo, sem antes/depois, sem depoimentos de pacientes.
- Linguagem informativa e acolhedora.
- Rodapé com nota de sigilo profissional; se houver qualquer coleta de dado (não há formulário neste escopo), mencionar LGPD. Como o contato é via WhatsApp, não há coleta de dados pelo site.

## 10. Hospedagem (entregável final)

Site estático → o usuário compra o domínio e sobe o conteúdo de `frontend/`. O `README.md` cobrirá: como testar localmente, e opções de deploy (Hostinger/hospedagem comum via FTP, Netlify, Vercel, GitHub Pages) + como apontar o domínio.

## 11. Fora de escopo (YAGNI)

- Backend, banco de dados, formulários server-side.
- Feed dinâmico do Instagram via API.
- Blog/CMS, área logada, sistema de agendamento próprio.
- Multi-idioma.

## 12. Critérios de sucesso

- Todas as 8 seções implementadas com o conteúdo definido.
- Dois carrosséis funcionais (fotos + posts) com swipe no mobile.
- Scroll animations suaves e botão WhatsApp funcional com mensagem pré-preenchida.
- Responsivo e rápido em mobile.
- Conteúdo verídico, em PT-BR, conforme CFP.
- Pasta `frontend/` pronta para upload em domínio, com README de deploy.
