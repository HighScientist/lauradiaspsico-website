# Laura Dias — Psicóloga · Repositório do Projeto

Landing page estática para a psicóloga Laura de Oliveira Dias (CRP 04/73471), desenvolvida para apresentar seus serviços de psicoterapia online via TCC para adultos e idosos.

Site em produção: [lauradiaspsico.com.br](https://lauradiaspsico.com.br/), publicado via GitHub Pages (GitHub Actions).

## Estrutura

- **`frontend/`** — todo o código do site (HTML, CSS, JS, imagens já otimizadas). É esta pasta que o workflow de deploy publica (`.github/workflows/deploy.yml`).
- **`.github/workflows/deploy.yml`** — build e deploy automático no GitHub Pages a cada push em `main`.

Materiais de design (specs, prompts, fotos originais em alta resolução, script de otimização de imagens) foram removidos do repositório para manter apenas o necessário para o site funcionar — não fazem parte do build publicado.

## Documentação

- Instruções de teste local, deploy e manutenção do site: [`frontend/README.md`](frontend/README.md)

## Início rápido

```bash
cd frontend && python3 -m http.server 8000
```

Acesse `http://localhost:8000` no navegador.
