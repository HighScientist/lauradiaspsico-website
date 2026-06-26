# Guia passo a passo — Como criar o melhor site para a Laura

Você está em ótima posição: já existe um **spec aprovado**, um **plano** e uma **landing page funcional** em `frontend/`. Este guia te leva do que existe hoje até o site no ar, com qualidade.

---

## Fase 0 — Reunir os materiais (antes de tudo)
Quanto melhor o material de entrada, melhor o site. Junte:
- [ ] **Fotos em alta resolução** da Laura (as de `context/images/` já servem; se houver originais maiores, melhor).
- [ ] **Dados confirmados:** nome completo ✓, CRP 04/73471 ✓, WhatsApp (17) 98123-9566 ✓.
- [ ] **Currículo detalhado** (o que falta): pós-graduações, cursos, experiências hospitalares específicas, ano de formação. — *Peça isso para a Laura.*
- [ ] **Decisões dela:** valor da sessão (mostrar ou não no site?), e-mail profissional, se quer link de agendamento (Calendly) no futuro.
- [ ] **Aprovação da Laura sobre os textos** — obrigatório por ética (CFP). Ela é a responsável técnica pelo conteúdo.

---

## Fase 1 — Gerar o design e os assets (com IA)
1. [ ] Abra o **Claude (modo design/artifacts)** e cole o **PROMPT PARA O CLAUDE** de `docs/prompt-design-completo.md`. Anexe 4–6 fotos boas da Laura.
2. [ ] Peça variações se quiser ("me mostre 2 versões do hero"). Itere até gostar.
3. [ ] No **Cowork** (ou gerador de imagens), use a seção **"ASSETS A GERAR"** do mesmo arquivo para criar: favicon, imagem Open Graph, texturas, ícones e divisores.
4. [ ] **Importante (ética):** use só fotos reais da Laura para retratos — não gere rosto de IA representando-a. Assets decorativos podem ser gerados.

> Dica: você já tem uma landing page pronta em `frontend/`. Pode usar o design gerado pelo Claude como **inspiração/refinamento** dela, ou substituir. Compare os dois e fique com o melhor.

---

## Fase 2 — Montar e refinar o site
1. [ ] Escolha a base: a landing page atual (`frontend/`) **ou** o artifact gerado pelo Claude.
2. [ ] Encaixe os assets gerados (favicon, OG, texturas, ícones) nas pastas `frontend/assets/`.
3. [ ] Substitua/atualize as fotos e posts pelos definitivos.
4. [ ] Revise toda a copy **com a Laura** — ajuste tom, corrija qualquer promessa de resultado (CFP).
5. [ ] Preencha o currículo detalhado na seção "Quem sou eu?".

---

## Fase 3 — Testar antes de publicar
1. [ ] **Local:** `cd frontend && python3 -m http.server 8000` → abra `http://localhost:8000`.
2. [ ] Teste no **celular** (a maioria do público é mobile): tudo legível, botões fáceis de tocar, carrosséis deslizam.
3. [ ] Clique em **todos os botões de WhatsApp** — devem abrir a conversa com a mensagem pronta.
4. [ ] Teste os links de Instagram e da bio.
5. [ ] Verifique a **velocidade** (imagens otimizadas já ajudam). Ferramenta: PageSpeed Insights.
6. [ ] Confira **nome + CRP visíveis** e ausência de promessas/depoimentos (CFP).

---

## Fase 4 — Comprar o domínio
1. [ ] Escolha um domínio. Sugestões: `lauradiaspsicologa.com.br`, `psicologalauradias.com.br`, `lauradiaspsi.com.br`.
2. [ ] Compre em um registrador. `.com.br` é no **registro.br** (exige CPF/CNPJ; barato). `.com` em Namecheap/GoDaddy/Hostinger.
3. [ ] Tendo domínio próprio, você passa credibilidade e some o "/keepo.bio".

---

## Fase 5 — Hospedar (escolha 1)
O site é 100% estático → hospedagem é simples e barata/grátis.
- **Netlify ou Vercel (grátis, recomendado):** arraste a pasta `frontend/` ou conecte um repositório. Apontar o domínio é guiado pelo painel.
- **Hostinger / hospedagem comum (cPanel):** suba o conteúdo de `frontend/` para `public_html` via FTP/Gerenciador de Arquivos.
- **GitHub Pages (grátis):** publique e configure o domínio customizado.

**Antes de publicar:** troque `SEU-DOMINIO.com.br` no `index.html` (canonical, og:image, JSON-LD) pelo domínio real. (Documentado em `frontend/README.md`.)

---

## Fase 6 — Configurar e lançar
1. [ ] Aponte o **DNS** do domínio para a hospedagem (o painel mostra como).
2. [ ] Garanta **HTTPS** (Netlify/Vercel/Hostinger fazem automático — cadeado verde).
3. [ ] Teste o **preview do link** colando a URL no WhatsApp (deve aparecer a imagem Open Graph).
4. [ ] Atualize a **bio do Instagram** com o link do site.
5. [ ] (Opcional) Crie um **Google Meu Negócio** "Psicóloga" para aparecer no Google/Maps.

---

## Fase 7 — Divulgar e manter
- [ ] Anuncie no Instagram (stories + post) que o site está no ar.
- [ ] Adicione o link na bio (keepo e/ou direto).
- [ ] Mantenha o carrossel de posts atualizado (instruções em `frontend/README.md`).
- [ ] Reúna feedback dos primeiros visitantes/pacientes e ajuste.

---

## Princípios para "o melhor site" para uma psicóloga
1. **Mobile primeiro** — quase todo mundo vai abrir no celular.
2. **Um objetivo claro** — agendar pelo WhatsApp. Tudo aponta pra lá.
3. **Confiança** — nome, CRP, formação, foto real e linguagem acolhedora vendem mais que efeitos.
4. **Rápido e leve** — imagens otimizadas, sem excesso de scripts.
5. **Ético (CFP)** — sem promessas, sem depoimentos; informação que acolhe.
6. **Consistência visual** — mesma identidade do Instagram (paleta creme/marrom, serifada, estrela).
7. **Acessível** — bom contraste, textos alternativos, respeitar quem prefere menos animação.

---

### Arquivos de referência no projeto
- `docs/prompt-design-completo.md` — o prompt mestre (Claude design + Cowork).
- `docs/superpowers/specs/2026-06-26-landing-page-laura-design.md` — o spec aprovado.
- `docs/superpowers/plans/2026-06-26-landing-page-laura.md` — o plano técnico.
- `frontend/` — a landing page já construída e funcional.
- `frontend/README.md` — como testar e publicar.
