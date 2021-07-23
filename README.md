<p align="center">
<a href="https://t.me/kannaxupdates"><img src="https://telegra.ph/file/c005ca2f522659da9b978.png" width="400" height="400"/>
</p>
<p align="center">
<a href="https://github.com/fnixdev"><img title="Author" src="https://img.shields.io/badge/Author-fnixdev-red.svg?style=for-the-badge&logo=github"></a>
<a href="http://fnixdev.github.io/"><img title="Bio" src="https://img.shields.io/badge/FNIXDEV-BIO-red.svg?style=for-the-badge&logo=appveyor"></a>
</p>
<p align="center">
<a href="https://t.me/kannaxupdates"><img src="https://img.shields.io/badge/Join-Telegram%20Group-red.svg?style=flat-square&logo=Telegram"></a>
<a href="https://github.com/fnixdev/KannaX/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/fnixdev/KannaX?style=flat-square"></a>
<a href="https://github.com/fnixdev/KannaX/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/fnixdev/KannaX?style=flat-square"></a>
<a href="https://github.com/fnixdev/KannaX/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/fnixdev/KannaX?style=flat-square"></a>
<a href="https://github.com/fnixdev/KannaX/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/fnixdev/KannaX?style=flat-square"></a>
</p>

## Disclaimer
```
/**
   ⚠️Kang por sua própria conta e risco⚠️
    Sua conta do Telegram pode ser banida.
    Eu não sou responsável por qualquer uso indevido deste bot.
    Você acabou enviando spam para grupos, sendo denunciado
    e no final a Equipe do Telegram
    excluiu sua conta?
    Estarei rolando no chão rindo de você.
    Sim! você ouviu direito.
/**
```
## Requisitos 
* Python 3.8 ou Superior
* Telegram [API Keys](https://my.telegram.org/apps)
* Google Drive [API Keys](https://console.developers.google.com/)
* MongoDB [Database URL](https://cloud.mongodb.com/)

## Como Instalar

<details>
  <summary><b>Detalhes e Guias</b></summary>

### Pelo Heroku
<p>- Clique aqui para dar deploy ao KannaX.</p>
<p><a href = "https://heroku.com/deploy?template=https://github.com/fnixdev/KannaX-Deploy"><img src="https://www.herokucdn.com/deploy/button.svg" alt="MyGpac"> </a></p>
<p>- Preencha API_ID | API_HASH | DATABASE_URL | LOG_CHANNEL_ID | HEROKU_APP_NAME | HEROKU_API_KEY <strong>(obrigatorio)<strong></p>
<p>- Cique no botao Deploy.</p>
<p>- Ligue o Dyno na aba de Resource.</p>
<p>- É isso ... Comece a usar KannaX.</p>
<p>Você pode adicionar tambem <a href="https://telegra.ph/VARs-N%C3%A3o-Obrigatorias-KannaX-07-23">VARs não obrigatorias</a> mais tarde de acordo com suas necessidades. Esses vars são usados por seus respectivos plug-ins no userbot para funcionar. Para saber como adicionar vars não obrigatórios, verifique este <a href="https://fnixdev.gitbook.io/kannax/">Guia</a>.</p>

### Instalando com Metodo Tradicional

#### Metodo fácil e automatico
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ bash <(curl -s https://fnixdev.github.io/Setup_Local_VPS.sh)
</code></pre></div></div>
   
#### Método manual

<p><strong>1. Instalando os pacotes</strong></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ sudo apt install tree wget2 p7zip-full jq ffmpeg wget git
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ sudo apt install ./google-chrome-stable_current_amd64.deb
</code></pre></div></div>

<p><strong>2. Clone o Repositorio</strong></p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>git clone https://github.com/fnixdev/KannaX.git <span class="o">&amp;&amp;</span> <span class="nb">cd </span>KannaX
</code></pre></div></div>

<p><strong>3. Instale os requisitos</strong></p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>pip3 <span class="nb">install</span> <span class="nt">-r</span> requirements.txt
</code></pre></div></div>

<p><strong>4. Crie config.env como config.env.sample e preencha as Vars</strong></p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span><span class="nb">cp </span>config.env.sample config.env
</code></pre></div></div>

<p><strong>5. Obtenha a Session String e adicione-a ao config.env</strong></p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>bash genStr
</code></pre></div></div>
<p>Ou voce pode usar <a href="https://replit.com/@fnixdev/StringSessionKX">REPL</a> para obter a string.</p>

<p><strong>6. Finalmente execute o KannaX</strong></p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>bash run
</code></pre></div></div>
</details>

## String Session
- VAR -> `HU_STRING_SESSION`

#### Pelo HEROKU
- [Abra seu app heroku](https://dashboard.heroku.com/apps/) clique em **more** -> **run console** e digite `bash genStr` e clique em **run**.

#### Pelo REPL (Metodo mais facil)
- [Gerar String no REPL](https://replit.com/@fnixdev/StringSessionKX)

### Créditos pelo Projeto
* [USERGE-X](https://github.com/code-rgb/USERGE-X)
* [Pyrogram Assistant](https://github.com/pyrogram/assistant)
* [PyroGramBot](https://github.com/SpEcHiDe/PyroGramBot)
* [PaperPlane](https://github.com/RaphielGang/Telegram-Paperplane)
* [Uniborg](https://github.com/SpEcHiDe/UniBorg)

### Direitos e Licensa
[**GNU General Public License v3.0**](https://github.com/fnixdev/KannaX/blob/master/LICENSE)
