# Prompt mestre — Design completo da landing page da Laura

> Cole este conteúdo no **Claude (modo design / artifacts)** para gerar o design e o HTML completo,
> e use a seção "ASSETS A GERAR" no **Cowork** (ou em qualquer gerador de imagens) para criar os elementos visuais.
> Substitua os trechos entre `[colchetes]` antes de enviar.

---

## 🧠 PROMPT PARA O CLAUDE (DESIGN / ARTIFACTS)

Copie tudo abaixo desta linha:

═══════════════════════════════════════════════════════════════

Você é um designer e desenvolvedor front-end sênior, especialista em landing pages de alta conversão para profissionais de saúde. Quero que você **desenhe e construa uma landing page single-page completa, responsiva e animada**, em **HTML + CSS + JavaScript puro** (sem framework), para a psicóloga abaixo. Entregue um artifact único e funcional.

### Quem é a profissional
- **Nome:** Laura de Oliveira Dias
- **Registro:** Psicóloga · CRP 04/73471 (Minas Gerais)
- **Formação:** Psicóloga pela Universidade Federal do Triângulo Mineiro (UFTM). Mineira, morando em São Paulo.
- **Atuação:** Clínica e hospitalar · Neuropsicóloga · Psico-oncologia
- **Abordagem:** Terapia Cognitivo-Comportamental (TCC)
- **Atendimento:** 100% online, sessões de ~50 minutos, sob sigilo profissional
- **Contato:** WhatsApp `https://wa.me/5517981239566` · Instagram `@lauradiaspsico` (https://www.instagram.com/lauradiaspsico/) · Bio https://lauradiaspsico.keepo.bio

### Objetivo
Apresentar o trabalho dela e converter visitantes (a maioria vinda do Instagram, em celular) em agendamentos pelo WhatsApp. Mobile-first.

### Identidade visual (siga à risca)
- **Estética:** elegante, acolhedora, minimalista, "clean girl", tons quentes e terrosos. Muito espaço em branco.
- **Paleta:**
  - Fundo creme `#EFE6DD` e creme claro `#F5EFE8`
  - Cartões off-white `#FBF8F4`
  - Texto principal marrom escuro `#4A3F35`, secundário taupe `#7D6B5D`
  - Detalhe/acento dourado-caramelo `#B89B7A`
  - Preto suave `#2B2622`
- **Tipografia:** títulos em serifada elegante (**Cormorant Garamond**); destaques manuscritos pontuais (**Sacramento**); corpo em sans-serif limpa (**Inter**). Use Google Fonts.
- **Elemento gráfico:** uma **estrela ✦ de 4 pontas** como motivo recorrente; cantos arredondados suaves; sombras leves; finas linhas conectoras.
- **Mood:** sofisticado, feminino, calmo, profissional e humano — nunca clínico/frio nem sensacionalista.

### Tom de voz da copy (português do Brasil)
Acolhedor, direto, empático, em primeira pessoa quando ela fala. Frases curtas. Inspire-se nestas frases reais dos posts dela: "Você não precisa carregar esse peso sozinho", "Sofrer em silêncio não é força", "Falar sobre o que sente não é fraqueza, é libertação", "Pedir ajuda não te torna fraco, te torna humano", "Você merece ser feliz", "Reserve um momento para cuidar de você".

### Estrutura (8 seções, nesta ordem) + conteúdo
1. **Hero** — eyebrow "✦ Psicóloga · CRP 04/73471"; título "Você não precisa carregar esse peso *sozinho*" ("sozinho" em manuscrito); subtítulo sobre TCC online para adultos e idosos; botão primário "Agendar pelo WhatsApp" + botão secundário "Conhecer meu trabalho"; foto da Laura com moldura em arco; selo "Atendimento 100% online".
2. **Quem sou eu?** — nome completo, CRP, formação UFTM, atuação clínica/hospitalar/neuro/psico-oncologia; parágrafo humano sobre acolhimento; "pílulas" com: Psicóloga pela UFTM · Clínica e hospitalar · Neuropsicóloga · Psico-oncologia · Abordagem Cognitivo-Comportamental · Mineira morando em SP. Ao lado, **carrossel de fotos profissionais** dela.
3. **Abordagem (TCC)** — explicação acessível da Terapia Cognitivo-Comportamental + 4 pilares: Baseada em evidências · Foco no presente · Ferramentas práticas · Trabalho colaborativo.
4. **Para quem é** — dois cartões: **Adultos** e **Idosos**, com texto acolhedor para cada.
5. **Demandas e Atendimentos** — grade de cartões: Ansiedade · Depressão · Luto · Câncer/Psico-oncologia · Doenças crônicas · Autoestima/autocrítica. Em seguida, um bloco destacado escuro **"Avaliação Neuropsicológica"** com pílulas: TDAH · TEA · Outras neurodivergências · Demais transtornos.
6. **Como funciona** — 4 cartões numerados: 01 100% online · 02 Sessões de 50 min · 03 Sigilo profissional · 04 Primeira conversa.
7. **Instagram** — **carrossel dos posts** dela (formato 4:5), cada slide linkando para o perfil; botões "Seguir @lauradiaspsico" e "Todos os links" (keepo).
8. **Contato/Agendamento** — chamada "Vamos conversar?", frase "Dar o primeiro passo já é um ato de cuidado", botão grande de WhatsApp; depois **rodapé escuro** com nome + CRP + "Atendimento online · Sigilo profissional garantido" + links.

### Comportamento e interações
- Navbar fixa com âncoras + smooth scroll; menu hambúrguer no mobile; muda de fundo ao rolar.
- **Dois carrosséis** (fotos e posts) com swipe/touch e autoplay — use a biblioteca **Swiper.js** via CDN.
- **Scroll reveal**: elementos surgem com fade + slide-up ao entrar na viewport (IntersectionObserver); respeite `prefers-reduced-motion`.
- **Botão flutuante de WhatsApp** fixo no canto.
- Todos os botões de WhatsApp devem abrir `https://wa.me/5517981239566?text=Olá, Laura! Vim pelo seu site e gostaria de agendar um atendimento.` (URL-encode o texto).

### Performance, SEO e conformidade
- `loading="lazy"` nas imagens, `alt` descritivo, `lang="pt-BR"`, meta description, Open Graph + Twitter Card, JSON-LD do tipo `Psychologist`, favicon de estrela.
- **Conformidade com o CFP (Conselho Federal de Psicologia):** nome + CRP sempre visíveis; **sem** promessa de cura/resultado, **sem** sensacionalismo, **sem** depoimentos de pacientes, **sem** antes/depois. Linguagem informativa e acolhedora.

### Imagens (importante — ética)
Use **apenas fotos reais da Laura** para a imagem pessoal/retratos (vou fornecê-las). **Não gere rostos de IA** representando-a. Para os posts, use as artes reais do Instagram dela. Elementos puramente decorativos (texturas de fundo, a estrela, ícones, divisores) podem ser gerados/estilizados. Onde eu ainda não fornecer a imagem, deixe um placeholder com proporção correta e um comentário indicando qual arquivo entra ali.

### Entrega
Um artifact HTML único e funcional, com CSS e JS embutidos ou bem organizados, comentado em português, pronto para eu hospedar. Caprichado no espaçamento, na hierarquia tipográfica e na sensação de "site premium de psicóloga".

═══════════════════════════════════════════════════════════════

---

## 🎨 ASSETS A GERAR (use no Cowork / gerador de imagens)

Gere **apenas elementos decorativos** — as fotos pessoais e os posts são reais da Laura.
Mantenha SEMPRE a paleta: creme `#EFE6DD`, taupe `#7D6B5D`, marrom `#4A3F35`, dourado `#B89B7A`.

1. **Favicon / logo-marca** — uma estrela ✦ de 4 pontas dourada (`#B89B7A`) sobre quadrado marrom (`#4A3F35`) com cantos arredondados. Formatos: SVG + PNG 512×512.
2. **Imagem Open Graph (1200×630)** — fundo creme texturizado, o nome "Laura Dias · Psicóloga" em Cormorant Garamond, CRP 04/73471, a estrela, e espaço para a foto dela à direita. (Para preview em WhatsApp/Google.)
3. **Texturas de fundo sutis** — papel/linho em tom creme, granulado leve, para usar atrás das seções (PNG/JPG, sem elementos chamativos).
4. **Conjunto de ícones em linha fina** (estilo do Instagram dela), na cor taupe: cérebro/neuro, coração, folha, calendário, balão de conversa, escudo (sigilo), relógio (50 min), monitor (online). SVG.
5. **Divisores/ornamentos** — pequenas estrelas e linhas finas conectoras para separar seções. SVG.
6. **(Opcional) Molduras de foto em arco** — máscara/overlay para padronizar os retratos com cantos arredondados estilo arco.
7. **(Opcional) Template de post do Instagram** — para a Laura manter a identidade ao postar: fundo creme, frase em serifada + manuscrito, @lauradiaspsico, a estrela.

**Prompt-base para cada asset (adapte o objeto):**
> "Minimalist elegant [OBJETO], thin line style, warm earthy beige and taupe palette (#EFE6DD, #7D6B5D, #4A3F35, #B89B7A), soft, feminine, sophisticated wellness/therapy aesthetic, lots of negative space, no text [exceto quando pedir], flat, high quality, transparent background where applicable."

---

## 📁 Fotos a fornecer (você já tem em `context/images/`)
- Retratos profissionais: `photo_1` … `photo_14` (escolha as melhores; `photo_1` é ótima para o hero).
- Posts do Instagram: `post_01` … `post_17`.
- O design atual já usa: 6 fotos no carrossel + hero, e 7 posts curados — você pode ampliar.
