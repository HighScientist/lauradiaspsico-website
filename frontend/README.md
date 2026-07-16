# Laura Dias — Psicóloga · Landing Page

Site estático de apresentação da psicóloga Laura de Oliveira Dias (CRP 04/73471), com foco em psicoterapia online via TCC para adultos e idosos.

Em produção em [lauradiaspsico.com.br](https://lauradiaspsico.com.br/).

## Testar localmente

Na raiz do repositório, execute:

```bash
cd frontend && python3 -m http.server 8000
```

Abra `http://localhost:8000` no navegador. O servidor local garante que caminhos relativos de assets (CSS, JS, imagens) funcionem corretamente — não abra o `index.html` diretamente como arquivo (`file://`).

## Analytics

O `<head>` do `index.html` já inclui o Google tag (gtag.js) apontando para o Measurement ID `G-SWRQXZV02D`, usado para Google Analytics/Google Ads. Para trocar de propriedade, atualize o `id` nas duas ocorrências (`src="...?id=..."` e `gtag('config', '...')`).

## Atualizar fotos e posts

O repositório não guarda mais as fotos originais em alta resolução nem o script de otimização (removidos para manter só o necessário para o site funcionar). Para trocar ou adicionar uma imagem:

1. Otimize a foto você mesmo (redimensionar para o tamanho de exibição real, exportar em `.jpg` e `.webp` com compressão) e salve em `assets/images/photos/` ou `assets/images/posts/`.
2. Aponte a tag `<picture>` correspondente no `index.html` para os novos arquivos.

## Deploy

O deploy atual é automático: GitHub Actions (`.github/workflows/deploy.yml`) publica esta pasta (`frontend/`) no GitHub Pages a cada push em `main`. O domínio customizado é definido pelo arquivo `CNAME` nesta pasta e configurado nos registros DNS do domínio (registro.br → A records apontando para os IPs do GitHub Pages + CNAME de `www`).

Alternativas de hospedagem, caso mude de provedor:

### Netlify ou Vercel (gratuito)

Arraste a pasta `frontend/` diretamente no painel do Netlify/Vercel, ou conecte o repositório Git e configure `frontend/` como diretório de publicação. Depois aponte o domínio customizado nas configurações de DNS conforme as instruções do serviço escolhido.

### Hospedagem comum (cPanel / FTP)

Faça upload de todo o conteúdo da pasta `frontend/` para o diretório `public_html` do servidor via FTP ou pelo gerenciador de arquivos do cPanel. O `index.html` deve ficar na raiz de `public_html`.

---

**Nota:** este site é 100% estático — não há backend, banco de dados nem etapa de build. Qualquer servidor ou serviço de hospedagem de arquivos estáticos funciona.
