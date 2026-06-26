# Laura Dias — Psicóloga · Landing Page

Site estático de apresentação da psicóloga Laura de Oliveira Dias (CRP 04/73471), com foco em psicoterapia online via TCC para adultos e idosos.

## Testar localmente

Na raiz do repositório, execute:

```bash
cd frontend && python3 -m http.server 8000
```

Abra `http://localhost:8000` no navegador. O servidor local garante que caminhos relativos de assets (CSS, JS, imagens) funcionem corretamente — não abra o `index.html` diretamente como arquivo (`file://`).

## Antes de publicar

Substitua todas as ocorrências de `SEU-DOMINIO.com.br` no arquivo `index.html` pelo domínio real adquirido. As ocorrências estão nas seguintes tags:

- `<link rel="canonical">` — URL canônica para indexação no Google
- `<meta property="og:image">` — URL da imagem compartilhada em redes sociais
- JSON-LD (`<script type="application/ld+json">`) — campos `url` e `image` dos dados estruturados

Faça a substituição com um editor de texto ou com o comando:

```bash
sed -i 's/SEU-DOMINIO.com.br/seudominio.com.br/g' index.html
```

## Atualizar fotos e posts

1. Coloque as novas imagens na pasta `context/images/`.
2. Ajuste as listas `PHOTOS` e `POSTS` no arquivo `scripts/optimize-images.py` para incluir os novos nomes de arquivo.
3. Rode o script de otimização a partir da raiz do repositório:

```bash
python3 scripts/optimize-images.py
```

4. O script gera versões otimizadas em `frontend/assets/images/`. Atualize as tags `<picture>` correspondentes no `index.html` para apontar para os novos arquivos.

## Deploy

### Netlify ou Vercel (gratuito, recomendado)

Arraste a pasta `frontend/` diretamente no painel do Netlify/Vercel, ou conecte o repositório Git e configure `frontend/` como diretório de publicação. Depois aponte o domínio customizado nas configurações de DNS conforme as instruções do serviço escolhido.

### Hospedagem comum (cPanel / FTP)

Faça upload de todo o conteúdo da pasta `frontend/` para o diretório `public_html` do servidor via FTP ou pelo gerenciador de arquivos do cPanel. O `index.html` deve ficar na raiz de `public_html`.

### GitHub Pages

Publique a pasta `frontend/` ativando o GitHub Pages nas configurações do repositório (aba *Pages*), selecionando a branch e o diretório `/frontend` como origem. Em seguida, configure o domínio customizado na mesma aba e adicione os registros DNS indicados pelo GitHub no seu provedor de domínio.

---

**Nota:** este site é 100% estático — não há backend, banco de dados nem etapa de build. Qualquer servidor ou serviço de hospedagem de arquivos estáticos funciona.
