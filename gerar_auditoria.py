
# Script para gerar os 4 arquivos da auditoria com design clean preto e branco

import os

base = "C:/Users/guilherme/"

# ============================================================
# PECA 1 - SUMARIO EXECUTIVO
# ============================================================
sumario = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Sumário Executivo — Auditoria Sabor do Sul Pizzas</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Segoe UI',Arial,sans-serif; background:#ebebeb; color:#111; }
.page { max-width:800px; margin:40px auto; background:#fff; border:1px solid #ccc; }
.header { background:#111; color:#fff; padding:48px; }
.header-top { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:32px; }
.logo h1 { font-size:20px; font-weight:900; letter-spacing:4px; text-transform:uppercase; }
.logo p { font-size:11px; color:#888; margin-top:4px; letter-spacing:2px; text-transform:uppercase; }
.badge { border:1px solid #555; color:#aaa; font-size:10px; font-weight:700; padding:5px 14px; letter-spacing:2px; text-transform:uppercase; }
.header h2 { font-size:28px; font-weight:800; line-height:1.2; margin-bottom:6px; }
.header .sub { font-size:11px; color:#777; margin-top:8px; letter-spacing:2px; text-transform:uppercase; }
.body { padding:48px; }
.score-box { display:flex; align-items:center; gap:36px; border:1.5px solid #111; padding:28px 36px; margin-bottom:40px; }
.score-num { font-size:80px; font-weight:900; color:#111; line-height:1; }
.score-den { font-size:28px; color:#bbb; font-weight:300; }
.score-info { flex:1; }
.score-info h3 { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:3px; margin-bottom:10px; }
.score-info p { font-size:13px; color:#666; line-height:1.6; margin-bottom:14px; }
.bar-row { display:flex; align-items:center; gap:10px; margin-bottom:7px; }
.bar-label { font-size:10px; color:#999; width:85px; letter-spacing:1px; text-transform:uppercase; }
.bar-track { flex:1; background:#eee; height:3px; }
.bar-fill { height:3px; background:#111; }
.bar-val { font-size:11px; color:#111; font-weight:700; width:28px; text-align:right; }
.section { margin-bottom:40px; }
.section-label { font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#999; margin-bottom:8px; }
.section h3 { font-size:18px; font-weight:700; margin-bottom:18px; }
.cards { display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; }
.card { border:1px solid #ddd; border-top:2px solid #111; padding:18px; }
.card strong { display:block; font-size:11px; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }
.card p { font-size:13px; color:#555; line-height:1.6; }
.conclusion-box { border:1.5px solid #111; padding:28px; margin-bottom:36px; }
.conclusion-box p { font-size:14px; color:#444; line-height:1.9; margin-bottom:12px; }
.conclusion-box p:last-child { margin-bottom:0; }
.conclusion-box em { font-style:normal; font-weight:700; }
.divider { height:1px; background:#eee; margin:36px 0; }
.signatures { display:flex; gap:14px; }
.sig-card { flex:1; border:1px solid #eee; padding:18px; text-align:center; }
.sig-role { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#999; margin-bottom:6px; }
.sig-name { font-size:14px; font-weight:700; margin-bottom:4px; }
.sig-area { font-size:11px; color:#888; line-height:1.4; }
.footer { background:#111; padding:24px 48px; color:#fff; display:flex; justify-content:space-between; align-items:center; }
.footer p { font-size:12px; color:#777; }
@media print { body{background:#fff} .page{margin:0;border:none} }
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <div class="header-top">
      <div class="logo"><h1>AppCheck</h1><p>Consultoria Digital</p></div>
      <div class="badge">Sumário Executivo</div>
    </div>
    <h2>Auditoria Digital —<br>Sabor do Sul Pizzas</h2>
    <p class="sub">Documento Confidencial &nbsp;·&nbsp; Versão 1.0 &nbsp;·&nbsp; Abril de 2026</p>
  </div>
  <div class="body">
    <div class="score-box">
      <div><div class="score-num">4.3<span class="score-den">/10</span></div></div>
      <div class="score-info">
        <h3>Nota Geral do Aplicativo</h3>
        <p>Média calculada a partir dos três blocos de auditoria realizados pela equipe entre os dias 14 e 22 de abril de 2026.</p>
        <div class="bar-row"><span class="bar-label">Experiência</span><div class="bar-track"><div class="bar-fill" style="width:50%"></div></div><span class="bar-val">5.0</span></div>
        <div class="bar-row"><span class="bar-label">LGPD</span><div class="bar-track"><div class="bar-fill" style="width:34%"></div></div><span class="bar-val">3.4</span></div>
        <div class="bar-row"><span class="bar-label">Segurança</span><div class="bar-track"><div class="bar-fill" style="width:42%"></div></div><span class="bar-val">4.2</span></div>
      </div>
    </div>
    <div class="section">
      <div class="section-label">Pontos Fortes</div>
      <h3>O que a empresa acerta</h3>
      <div class="cards">
        <div class="card"><strong>App acessível e gratuito</strong><p>Disponível em iOS e Android, instalação rápida e nota 4.4/5 na App Store — resultado claramente puxado pela qualidade do produto.</p></div>
        <div class="card"><strong>Rede física consolidada</strong><p>São 8 unidades espalhadas pela Bahia, Alagoas e Rio Grande do Sul — mostra que a empresa tem estrutura real por trás do app.</p></div>
        <div class="card"><strong>Pedido digital funciona</strong><p>O fluxo básico de fazer um pedido, escolher o pagamento e receber a confirmação por e-mail funciona sem grandes problemas.</p></div>
      </div>
    </div>
    <div class="divider"></div>
    <div class="section">
      <div class="section-label">Pontos Críticos — Ação Imediata Necessária</div>
      <h3>O que preocupa — e muito</h3>
      <div class="cards">
        <div class="card"><strong>Contradição grave de dados</strong><p>Na App Store está escrito que "nenhum dado é coletado". Mas a política de privacidade lista nome, e-mail, telefone, endereço e rastreadores como Facebook Pixel e Google Analytics. Violação direta da LGPD.</p></div>
        <div class="card"><strong>Política parada no tempo</strong><p>A última atualização da política foi em outubro de 2020 — mais de cinco anos atrás. Não há uma palavra sobre dados de crianças e adolescentes, mesmo o app sendo classificado como A16.</p></div>
        <div class="card"><strong>DPO via Gmail pessoal</strong><p>O canal do Encarregado de Dados — figura obrigatória pela LGPD — é um endereço Gmail comum. Sem prazo de resposta, sem protocolo, sem identidade corporativa.</p></div>
      </div>
    </div>
    <div class="divider"></div>
    <div class="conclusion-box">
      <div class="section-label">Conclusão</div>
      <p>A Sabor do Sul Pizzas claramente investe no produto — as pizzas são boas, a rede cresceu, e o app existe. Mas o digital ainda não acompanhou esse crescimento. Durante a visita à loja, o próprio funcionário que abordamos não sabia que a pizzaria tinha um aplicativo. Isso diz muito sobre como o canal digital ainda é tratado internamente.</p>
      <p>Do ponto de vista de privacidade, a situação é mais séria: <em>a empresa está exposta a risco real de sanção pela ANPD.</em> Declarar que nenhum dado é coletado enquanto a política diz o contrário não é um detalhe — é exatamente o tipo de inconsistência que os fiscais buscam. A adequação precisa acontecer com urgência.</p>
    </div>
    <div class="section">
      <div class="section-label">Equipe Auditora</div>
      <h3>AppCheck Consultoria Digital</h3>
      <div class="signatures">
        <div class="sig-card"><div class="sig-role">Papel 1</div><div class="sig-name">Guilherme Argollo</div><div class="sig-area">Auditor de Experiência e Integração Omnichannel</div></div>
        <div class="sig-card"><div class="sig-role">Papel 2</div><div class="sig-name">João Pedro Menezes</div><div class="sig-area">Auditor de Privacidade e LGPD</div></div>
        <div class="sig-card"><div class="sig-role">Papel 3</div><div class="sig-name">Elô</div><div class="sig-area">Auditor de Segurança e Desempenho Técnico</div></div>
      </div>
    </div>
  </div>
  <div class="footer">
    <div><strong style="color:#fff;letter-spacing:1px;">AppCheck Consultoria Digital</strong><p>Documento confidencial · Abril de 2026</p></div>
    <p style="color:#fff;font-weight:700;font-size:13px;">Nota Geral: 4.3 / 10</p>
  </div>
</div>
</body></html>"""

# ============================================================
# PECA 2 - RELATORIO TECNICO
# ============================================================
relatorio = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Relatório Técnico — Auditoria Sabor do Sul Pizzas</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Segoe UI',Arial,sans-serif; background:#ebebeb; color:#111; }
.page { max-width:800px; margin:40px auto; background:#fff; border:1px solid #ccc; }
.capa { background:#111; color:#fff; padding:80px 48px; min-height:420px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
.capa .logo { font-size:24px; font-weight:900; letter-spacing:4px; text-transform:uppercase; margin-bottom:4px; }
.capa .logo-sub { font-size:11px; color:#888; letter-spacing:2px; text-transform:uppercase; margin-bottom:52px; }
.capa h1 { font-size:30px; font-weight:800; line-height:1.2; margin-bottom:10px; }
.capa .empresa { font-size:18px; color:#aaa; margin-bottom:52px; font-weight:300; letter-spacing:1px; }
.capa .divider-line { width:40px; height:2px; background:#fff; margin:20px auto; opacity:0.3; }
.capa .meta { font-size:12px; color:#777; line-height:2.2; letter-spacing:1px; }
.body { padding:48px; }
.section { margin-bottom:44px; }
.section-label { font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#999; margin-bottom:8px; }
.section h2 { font-size:20px; font-weight:800; margin-bottom:16px; border-bottom:1.5px solid #111; padding-bottom:10px; }
.section h3 { font-size:15px; font-weight:700; margin-bottom:10px; color:#111; margin-top:24px; text-transform:uppercase; letter-spacing:1px; }
.section p { font-size:14px; color:#444; line-height:1.9; margin-bottom:12px; }
.divider { height:1px; background:#eee; margin:40px 0; }
.info-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:16px; }
.info-item { background:#f7f7f7; padding:14px 16px; border-left:2px solid #111; }
.info-item strong { display:block; font-size:10px; text-transform:uppercase; letter-spacing:2px; color:#999; margin-bottom:4px; }
.info-item span { font-size:13px; color:#333; }
table { width:100%; border-collapse:collapse; margin-top:16px; font-size:13px; }
thead { background:#111; color:#fff; }
thead th { padding:12px 14px; text-align:left; font-weight:700; font-size:11px; text-transform:uppercase; letter-spacing:1px; }
thead th:last-child { text-align:center; width:60px; }
tbody td { padding:11px 14px; border-bottom:1px solid #eee; color:#444; vertical-align:top; line-height:1.5; }
tbody td:last-child { text-align:center; font-weight:800; }
tbody tr:nth-child(even) { background:#fafafa; }
.media-row td { background:#f0f0f0; font-weight:700; border-top:2px solid #111; }
.nota-m { color:#555; }
.nota-b { color:#111; }
.matrix { border-collapse:collapse; width:100%; font-size:11px; margin-top:12px; }
.matrix th,.matrix td { border:1px solid #ccc; padding:10px; text-align:center; vertical-align:middle; }
.matrix th { background:#111; color:#fff; font-size:10px; text-transform:uppercase; letter-spacing:1px; }
.risk-critico { background:#111; color:#fff; padding:3px 7px; font-size:10px; font-weight:700; display:inline-block; margin:2px; letter-spacing:1px; }
.risk-alto { background:#555; color:#fff; padding:3px 7px; font-size:10px; font-weight:700; display:inline-block; margin:2px; letter-spacing:1px; }
.risk-medio { background:#ccc; color:#111; padding:3px 7px; font-size:10px; font-weight:700; display:inline-block; margin:2px; letter-spacing:1px; }
.rec-item { border-left:2px solid #111; background:#f7f7f7; padding:16px 20px; margin-bottom:10px; }
.rec-num { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#999; margin-bottom:5px; }
.rec-prob { font-size:14px; font-weight:700; margin-bottom:5px; }
.rec-sol { font-size:13px; color:#555; line-height:1.6; margin-bottom:4px; }
.rec-prazo { font-size:11px; font-weight:700; color:#111; letter-spacing:1px; }
.evidence-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px; }
.evidence-item { border:1px solid #eee; padding:14px; }
.ev-type { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#999; margin-bottom:6px; }
.ev-desc { font-size:13px; color:#444; line-height:1.5; }
.ev-placeholder { background:#f7f7f7; border:1px dashed #ccc; height:80px; display:flex; align-items:center; justify-content:center; font-size:11px; color:#bbb; margin-top:8px; letter-spacing:1px; }
.alert-box { border-left:2px solid #111; background:#f7f7f7; padding:14px 18px; margin:16px 0; font-size:13px; color:#444; line-height:1.7; }
.footer { background:#111; padding:24px 48px; color:#fff; display:flex; justify-content:space-between; align-items:center; }
.footer p { font-size:12px; color:#777; }
.footer strong { color:#fff; letter-spacing:1px; }
@media print { body{background:#fff} .page{margin:0;border:none} .capa{page-break-after:always} }
</style>
</head>
<body>
<div class="page">
  <div class="capa">
    <div class="logo">AppCheck</div>
    <div class="logo-sub">Consultoria Digital</div>
    <h1>Relatório Técnico de<br>Auditoria Digital</h1>
    <div class="divider-line"></div>
    <div class="empresa">Sabor do Sul Pizzas</div>
    <div class="meta">
      Versão 1.0 &nbsp;·&nbsp; Abril de 2026<br>
      Guilherme Argollo — Experiência e Omnichannel<br>
      João Pedro Menezes — Privacidade e LGPD<br>
      Elô — Segurança e Desempenho Técnico
    </div>
  </div>
  <div class="body">

    <div class="section">
      <div class="section-label">Seção 1</div>
      <h2>Metodologia</h2>
      <p>Nossa auditoria foi conduzida entre os dias 14 e 22 de abril de 2026. A escolha da Sabor do Sul Pizzas veio de um critério simples: a empresa tem app, tem lojas físicas acessíveis e lida com dados pessoais de clientes — atendendo os três requisitos da atividade. Também nos pareceu interessante auditar uma rede de alimentação regional, um segmento que costuma ter presença digital ainda em desenvolvimento.</p>
      <p>Dividimos a auditoria em três frentes: Guilherme Argollo ficou responsável pela experiência do usuário e pela integração com a loja física; João Pedro Menezes ficou com toda a parte de LGPD e privacidade; e Elô cuidou da análise técnica, de segurança e desempenho. Todos participamos da visita de campo e do teste do app.</p>
      <div class="info-grid">
        <div class="info-item"><strong>Empresa Auditada</strong><span>Sabor do Sul Pizzas</span></div>
        <div class="info-item"><strong>Período</strong><span>14 a 22 de abril de 2026</span></div>
        <div class="info-item"><strong>Plataformas Testadas</strong><span>iOS (App Store) e Android (Google Play)</span></div>
        <div class="info-item"><strong>Versão do App</strong><span>10.9.8 — plataforma terceirizada Neemo</span></div>
        <div class="info-item"><strong>Unidades Físicas</strong><span>8 unidades em BA, AL e RS</span></div>
        <div class="info-item"><strong>Avaliações Lidas</strong><span>78 na App Store + 20 no Google Play</span></div>
        <div class="info-item"><strong>Documentos Analisados</strong><span>Política de privacidade do site oficial</span></div>
        <div class="info-item"><strong>Persona Utilizada</strong><span>Jovem de 22 anos, primeiro pedido pelo app</span></div>
      </div>
    </div>

    <div class="divider"></div>

    <div class="section">
      <div class="section-label">Seção 2 — Bloco A</div>
      <h2>Experiência e Integração Omnichannel</h2>
      <p>Análise conduzida por Guilherme Argollo. O foco foi entender como o app se comporta na prática e se ele realmente conversa com as lojas físicas da rede.</p>
      <table>
        <thead><tr><th>Critério</th><th>O que observamos</th><th>Nota</th></tr></thead>
        <tbody>
          <tr><td><strong>Download e instalação</strong></td><td>Encontramos o app facilmente na App Store. Instalação rápida, 29.1 MB, gratuito. A nota de 4.4/5 com 78 avaliações é boa — embora os elogios sejam sobre a pizza, não sobre o app.</td><td class="nota-m">7/10</td></tr>
          <tr><td><strong>Integração com a loja física</strong></td><td>Durante a visita à unidade, não encontramos nenhum QR Code, banner ou totem mencionando o app. O funcionário disse que raramente os clientes usavam o aplicativo.</td><td class="nota-b">3/10</td></tr>
          <tr><td><strong>Usabilidade e design</strong></td><td>A interface é funcional e direta — dá pra fazer o pedido sem dificuldade. Design básico. Tivemos dois momentos de lentidão durante o teste.</td><td class="nota-m">5/10</td></tr>
          <tr><td><strong>Funcionalidades exclusivas</strong></td><td>O app se limita a fazer pedidos e mandar notificação por e-mail. Sem programa de fidelidade, rastreio em tempo real, chat ou cupons exclusivos.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Custo-benefício</strong></td><td>É gratuito, o que ajuda. Mas tentamos ligar para o WhatsApp exibido no app e não obtivemos resposta. Usuários relatam erros na montagem dos pedidos.</td><td class="nota-m">6/10</td></tr>
          <tr class="media-row"><td colspan="2"><strong>Média do Bloco A</strong></td><td>5.0/10</td></tr>
        </tbody>
      </table>
      <h3>Nossa análise — Bloco A</h3>
      <p>O que mais nos chamou atenção durante a visita foi o desconhecimento do próprio funcionário sobre o app. Isso não é um detalhe pequeno: se a equipe interna não usa nem divulga o aplicativo, o cliente também não vai usar. A integração entre o canal digital e a loja física praticamente não existe — não há QR Code, não há promoção exclusiva, não há retirada no balcão para quem pediu pelo app. O digital e o físico funcionam como dois mundos separados.</p>
      <p>Do ponto de vista do usuário, o app cumpre o básico: dá pra pedir. Mas nada além disso justifica instalá-lo. Sem benefício exclusivo, sem rastreio, sem chat — qualquer pessoa prefere pedir pelo site ou pelo telefone. E quando o telefone não funciona, a experiência desmorona.</p>
    </div>

    <div class="divider"></div>

    <div class="section">
      <div class="section-label">Seção 3 — Bloco B</div>
      <h2>Privacidade e Conformidade com a LGPD</h2>
      <p>Análise conduzida por João Pedro Menezes. Aqui estão os achados mais preocupantes de toda a auditoria — e os que mais expõem a empresa a risco real.</p>
      <table>
        <thead><tr><th>Critério</th><th>O que observamos</th><th>Nota</th></tr></thead>
        <tbody>
          <tr><td><strong>Política de privacidade</strong></td><td>Existe e está acessível, mas a última atualização foi em outubro de 2020 — mais de cinco anos. Hospedada em um link do Google Docs, o que já é incomum para uma rede com 8 unidades.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Encarregado de dados (DPO)</strong></td><td>O contato indicado é sabordosulpizzas@gmail.com — endereço Gmail sem identidade corporativa, sem prazo de resposta e sem sistema de protocolo. Não atende ao art. 41 da LGPD.</td><td class="nota-b">3/10</td></tr>
          <tr><td><strong>Minimização de dados</strong></td><td>A política lista coleta de nome, e-mail, telefone, endereço, dados demográficos e métricas de navegação. Não fica claro por que todos esses dados são necessários para pedir uma pizza.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Consentimento</strong></td><td>A política menciona marketing "quando você nos der consentimento", mas durante o cadastro não encontramos opt-in separado e claro. O consentimento parece estar embutido nos termos gerais.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Permissões do app</strong></td><td>Achado mais grave: App Store afirma que "nenhum dado é coletado". Ao mesmo tempo, a política do site lista Facebook Pixel, Google Analytics, Google AdWords e Google Tag Manager. As duas informações não podem ser verdadeiras ao mesmo tempo.</td><td class="nota-b">2/10</td></tr>
          <tr><td><strong>Direitos do titular</strong></td><td>A política menciona os direitos de acesso, correção e exclusão. Porém, o único canal disponível é o e-mail Gmail, sem formulário, sem prazo e sem protocolo.</td><td class="nota-m">5/10</td></tr>
          <tr><td><strong>Cookies e rastreadores</strong></td><td>O site possui aviso de cookies, mas sem opção real de recusa por categoria. O usuário ou aceita tudo ou não usa o site.</td><td class="nota-b">3/10</td></tr>
          <tr><td><strong>Bases legais</strong></td><td>A política faz referência vaga a "legislação vigente" sem especificar qual base legal do art. 7 da LGPD justifica cada tipo de tratamento.</td><td class="nota-b">3/10</td></tr>
          <tr><td><strong>Dados de crianças/adolescentes</strong></td><td>Nenhuma cláusula sobre dados de menores. Especialmente preocupante porque a classificação etária do app é A16 — referências a álcool, tabaco ou drogas em uma pizzaria. Algo que por si só levantou nossas dúvidas.</td><td class="nota-b">2/10</td></tr>
          <tr><td><strong>Transparência sobre compartilhamento</strong></td><td>A política menciona compartilhamento com "parceiros comerciais de confiança" e transferências internacionais de dados. Não diz quem são esses parceiros nem para qual país os dados podem ir.</td><td class="nota-b">4/10</td></tr>
          <tr class="media-row"><td colspan="2"><strong>Média do Bloco B</strong></td><td>3.4/10</td></tr>
        </tbody>
      </table>
      <h3>Nossa análise — Bloco B</h3>
      <p>A contradição entre a declaração da App Store e a política de privacidade é, sem dúvida, o achado mais grave de toda a auditoria. Não é possível que "nenhum dado seja coletado" e, ao mesmo tempo, a empresa use Facebook Pixel, Google Analytics e Google AdWords. Um desses documentos está errado — e os dois são públicos, acessíveis a qualquer usuário ou fiscal.</p>
      <p>O que nos preocupou igualmente foi a política de 2020. Naquele ano, a LGPD ainda estava em fase de implementação. De lá pra cá, as obrigações ficaram mais claras, as multas começaram a ser aplicadas — mas a política da empresa ficou congelada naquele momento, como se o tempo não tivesse passado.</p>
      <p>A classificação A16 do app por referências a álcool, tabaco ou drogas também nos surpreendeu — e não encontramos nenhuma justificativa para isso dentro do aplicativo. Um app de pizzaria comum não deveria ter essa classificação.</p>
      <h3>Matriz de Risco LGPD</h3>
      <table class="matrix">
        <thead><tr><th></th><th>Impacto Baixo</th><th>Impacto Médio</th><th>Impacto Alto</th></tr></thead>
        <tbody>
          <tr><td><strong>Prob. Alta</strong></td><td><span class="risk-medio">Cookies sem recusa</span></td><td><span class="risk-alto">Política desatualizada</span> <span class="risk-alto">DPO via Gmail</span> <span class="risk-alto">Bases vagas</span> <span class="risk-alto">Retenção indefinida</span></td><td><span class="risk-critico">Contradição App Store vs. Política</span></td></tr>
          <tr><td><strong>Prob. Média</strong></td><td></td><td></td><td><span class="risk-critico">Sem proteção para menores (A16)</span></td></tr>
          <tr><td><strong>Prob. Baixa</strong></td><td></td><td><span class="risk-medio">Transfer. internacionais</span></td><td></td></tr>
        </tbody>
      </table>
      <p style="margin-top:10px;font-size:11px;color:#888;letter-spacing:1px;">
        <span class="risk-critico">CRÍTICO</span> Risco de sanção ANPD &nbsp;
        <span class="risk-alto">ALTO</span> Correção imediata &nbsp;
        <span class="risk-medio">MÉDIO</span> Melhoria recomendada
      </p>
    </div>

    <div class="divider"></div>

    <div class="section">
      <div class="section-label">Seção 4 — Bloco C</div>
      <h2>Segurança e Desempenho Técnico</h2>
      <p>Análise conduzida por Elô. O foco foi entender como o app se comporta tecnicamente — autenticação, estabilidade, velocidade e o que os usuários relatam sobre falhas.</p>
      <table>
        <thead><tr><th>Critério</th><th>O que observamos</th><th>Nota</th></tr></thead>
        <tbody>
          <tr><td><strong>Autenticação</strong></td><td>Login com e-mail e senha. Sem autenticação em dois fatores, sem login via Google ou Apple. Não identificamos política de força de senha durante o cadastro.</td><td class="nota-m">5/10</td></tr>
          <tr><td><strong>Estabilidade</strong></td><td>Durante nossos testes, o app travou uma vez ao carregar o cardápio. Nas avaliações, relatos frequentes de fechamentos inesperados em iOS e Android.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Desempenho</strong></td><td>O carregamento inicial é aceitável, mas o cardápio demora. Usuários relatam que o app trava na hora de finalizar o pedido — o pior momento possível.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Atualizações</strong></td><td>A nota da última versão é "Correção de push!" — sem nenhuma descrição do que foi corrigido ou do que mudou para o usuário.</td><td class="nota-b">4/10</td></tr>
          <tr><td><strong>Avaliações técnicas</strong></td><td>Problemas recorrentes: WhatsApp não responde, pedidos com sabores errados, espera acima de 2h sem atualização de status.</td><td class="nota-b">4/10</td></tr>
          <tr class="media-row"><td colspan="2"><strong>Média do Bloco C</strong></td><td>4.2/10</td></tr>
        </tbody>
      </table>
      <h3>Nossa análise — Bloco C</h3>
      <p>Um detalhe importante: o app é desenvolvido e mantido pela plataforma terceirizada Neemo. Isso significa que a Sabor do Sul Pizzas não tem controle direto sobre o código — quando algo precisa ser corrigido, depende do fornecedor. Isso ajuda a explicar a lentidão nas correções e a falta de comunicação sobre atualizações.</p>
      <p>A ausência de autenticação em dois fatores deixa as contas dos usuários vulneráveis. O que mais incomodou foi o WhatsApp não funcional. Quando um pedido dá errado, o usuário tenta entrar em contato e não consegue — isso não é apenas um problema técnico, é um problema de confiança.</p>
    </div>

    <div class="divider"></div>

    <div class="section">
      <div class="section-label">Seção 5</div>
      <h2>Recomendações Acionáveis</h2>
      <div class="rec-item">
        <div class="rec-num">Recomendação 01 — Crítico</div>
        <div class="rec-prob">App Store diz "nenhum dado coletado" — política diz o contrário</div>
        <div class="rec-sol">Atualizar imediatamente a ficha nas duas lojas de aplicativos para refletir os dados realmente coletados. Contratar DPO profissional para revisão completa da política.</div>
        <div class="rec-prazo">Prazo: Imediato — até 30 dias</div>
      </div>
      <div class="rec-item">
        <div class="rec-num">Recomendação 02 — Crítico</div>
        <div class="rec-prob">Política de 2020 sem revisão e sem cláusula para menores</div>
        <div class="rec-sol">Revisar e republicar a política com bases legais específicas por tipo de dado, prazo de retenção definido e cláusula dedicada ao tratamento de dados de menores (art. 14 da LGPD).</div>
        <div class="rec-prazo">Prazo: Até 60 dias</div>
      </div>
      <div class="rec-item">
        <div class="rec-num">Recomendação 03 — Alto</div>
        <div class="rec-prob">Canal do DPO é um Gmail pessoal sem estrutura de atendimento</div>
        <div class="rec-sol">Criar e-mail corporativo dedicado (ex: privacidade@sabordosulpizzas.com.br), formulário de solicitação de direitos e prazo de resposta publicado (15 dias úteis).</div>
        <div class="rec-prazo">Prazo: Até 60 dias</div>
      </div>
      <div class="rec-item">
        <div class="rec-num">Recomendação 04 — Alto</div>
        <div class="rec-prob">App e lojas físicas funcionam como canais completamente separados</div>
        <div class="rec-sol">Implementar pelo menos uma funcionalidade que conecte o digital ao físico: retirada na loja, QR Codes visíveis nas unidades ou cupom exclusivo para usuários do app.</div>
        <div class="rec-prazo">Prazo: Até 6 meses</div>
      </div>
      <div class="rec-item">
        <div class="rec-num">Recomendação 05 — Médio</div>
        <div class="rec-prob">Instabilidade técnica, WhatsApp não funcional e autenticação básica</div>
        <div class="rec-sol">Abrir chamado com a Neemo para correção dos bugs e do canal de contato. Avaliar adição de login via Google/Apple e autenticação em dois fatores.</div>
        <div class="rec-prazo">Prazo: Até 45 dias</div>
      </div>
      <div class="rec-item">
        <div class="rec-num">Recomendação 06 — Médio</div>
        <div class="rec-prob">Notas de atualização sem nenhuma informação útil ao usuário</div>
        <div class="rec-sol">Adotar política de notas de versão detalhadas a cada atualização, informando correções de bugs, melhorias de segurança e mudanças que afetam os dados dos usuários.</div>
        <div class="rec-prazo">Prazo: Na próxima atualização</div>
      </div>
    </div>

    <div class="divider"></div>

    <div class="section">
      <div class="section-label">Seção 6</div>
      <h2>Evidências Coletadas</h2>
      <div class="evidence-grid">
        <div class="evidence-item"><div class="ev-type">Evidência 01 — App Store</div><div class="ev-desc">Print da ficha afirmando "Nenhum dado coletado" — contradição com a política de privacidade do site.</div><div class="ev-placeholder">[Inserir print]</div></div>
        <div class="evidence-item"><div class="ev-type">Evidência 02 — Política de Privacidade</div><div class="ev-desc">Print listando coleta de dados e rastreadores. Última atualização: outubro de 2020.</div><div class="ev-placeholder">[Inserir print]</div></div>
        <div class="evidence-item"><div class="ev-type">Evidência 03 — Tela de Cadastro</div><div class="ev-desc">Print da tela de cadastro. Tempo cronometrado: aproximadamente 2 minutos e 50 segundos.</div><div class="ev-placeholder">[Inserir print]</div></div>
        <div class="evidence-item"><div class="ev-type">Evidência 04 — Avaliações de Usuários</div><div class="ev-desc">Prints de avaliações negativas: WhatsApp sem resposta, pedidos errados, atrasos acima de 2h.</div><div class="ev-placeholder">[Inserir print]</div></div>
        <div class="evidence-item"><div class="ev-type">Evidência 05 — Nota de Versão</div><div class="ev-desc">Print da versão 10.9.8 com apenas "Correção de push!" — sem transparência técnica.</div><div class="ev-placeholder">[Inserir print]</div></div>
        <div class="evidence-item"><div class="ev-type">Evidência 06 — Visita de Campo</div><div class="ev-desc">Fotos da unidade visitada: ausência de QR Code ou comunicação sobre o app. Anotações da conversa com o funcionário.</div><div class="ev-placeholder">[Inserir fotos]</div></div>
      </div>
    </div>

  </div>
  <div class="footer">
    <div><strong>AppCheck Consultoria Digital</strong><p>Relatório Técnico Confidencial · Abril de 2026</p></div>
    <p style="color:#fff;font-weight:700;font-size:13px;">Nota Geral: 4.3 / 10</p>
  </div>
</div>
</body></html>"""

# ============================================================
# PECA 3 - DASHBOARD
# ============================================================
dashboard = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Dashboard — Auditoria Sabor do Sul Pizzas</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Segoe UI',Arial,sans-serif; background:#ebebeb; color:#111; }
.page { max-width:800px; margin:40px auto; background:#fff; border:1px solid #ccc; }
.header { background:#111; color:#fff; padding:28px 40px; display:flex; justify-content:space-between; align-items:center; }
.header .brand { font-size:16px; font-weight:900; letter-spacing:3px; text-transform:uppercase; }
.header .title { text-align:right; }
.header .title p { font-size:11px; color:#888; letter-spacing:2px; text-transform:uppercase; margin-bottom:2px; }
.header .title h2 { font-size:17px; font-weight:700; color:#fff; }
.dash { padding:32px 40px; }

/* ROW 1 - NOTA GERAL + BLOCOS */
.row1 { display:grid; grid-template-columns:1fr 2fr; gap:20px; margin-bottom:20px; }
.nota-box { border:1.5px solid #111; padding:28px 24px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
.nota-label { font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#999; margin-bottom:8px; }
.nota-num { font-size:72px; font-weight:900; line-height:1; }
.nota-den { font-size:22px; color:#bbb; font-weight:300; }
.nota-selo { margin-top:12px; font-size:10px; font-weight:700; letter-spacing:2px; text-transform:uppercase; border:1px solid #111; padding:5px 12px; }

.blocos-col { display:flex; flex-direction:column; gap:12px; }
.bloco-item { border:1px solid #ddd; padding:16px 20px; display:flex; align-items:center; gap:20px; }
.bloco-name { font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#999; width:110px; flex-shrink:0; }
.bloco-bar-wrap { flex:1; }
.bloco-bar-track { background:#eee; height:8px; width:100%; }
.bloco-bar-fill { height:8px; background:#111; }
.bloco-val { font-size:22px; font-weight:900; color:#111; width:48px; text-align:right; flex-shrink:0; }

/* ROW 2 - ACHADOS */
.row2 { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:20px; }
.achados-box { border:1px solid #ddd; padding:20px; }
.achados-box h4 { font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#999; margin-bottom:16px; padding-bottom:10px; border-bottom:1px solid #eee; }
.achado-item { display:flex; gap:12px; margin-bottom:12px; align-items:flex-start; }
.achado-num { font-size:11px; font-weight:700; color:#999; min-width:20px; margin-top:1px; }
.achado-text { font-size:13px; color:#444; line-height:1.5; }
.achado-text strong { display:block; font-size:12px; color:#111; margin-bottom:2px; text-transform:uppercase; letter-spacing:0.5px; }

/* ROW 3 - LGPD */
.row3 { border:1px solid #111; padding:20px; margin-bottom:20px; }
.row3 h4 { font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#999; margin-bottom:16px; }
.lgpd-grid { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.lgpd-item { display:flex; align-items:center; gap:10px; padding:8px 12px; background:#f7f7f7; }
.lgpd-badge { font-size:9px; font-weight:700; letter-spacing:1px; text-transform:uppercase; padding:3px 8px; flex-shrink:0; }
.lgpd-badge.critico { background:#111; color:#fff; }
.lgpd-badge.alto { background:#555; color:#fff; }
.lgpd-badge.medio { background:#ccc; color:#111; }
.lgpd-txt { font-size:12px; color:#444; line-height:1.4; }

/* FRASE */
.frase-box { background:#111; color:#fff; padding:24px 40px; text-align:center; }
.frase-box p { font-size:18px; font-weight:800; line-height:1.3; letter-spacing:0.5px; }
.frase-box small { font-size:11px; color:#777; display:block; margin-top:8px; letter-spacing:1px; }

.footer { padding:18px 40px; display:flex; justify-content:space-between; align-items:center; border-top:1px solid #eee; }
.footer p { font-size:11px; color:#aaa; letter-spacing:1px; }
@media print { body{background:#fff} .page{margin:0;border:none} }
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <div class="brand">AppCheck<br><span style="font-size:10px;font-weight:400;color:#888;letter-spacing:2px;">Consultoria Digital</span></div>
    <div class="title">
      <p>Dashboard de Auditoria &nbsp;·&nbsp; Abril de 2026</p>
      <h2>Sabor do Sul Pizzas</h2>
    </div>
  </div>
  <div class="dash">

    <div class="row1">
      <div class="nota-box">
        <div class="nota-label">Nota Geral</div>
        <div class="nota-num">4.3<span class="nota-den">/10</span></div>
        <div class="nota-selo">Parcialmente Conforme</div>
      </div>
      <div class="blocos-col">
        <div class="bloco-item">
          <div class="bloco-name">Experiência</div>
          <div class="bloco-bar-wrap"><div class="bloco-bar-track"><div class="bloco-bar-fill" style="width:50%"></div></div></div>
          <div class="bloco-val">5.0</div>
        </div>
        <div class="bloco-item">
          <div class="bloco-name">LGPD</div>
          <div class="bloco-bar-wrap"><div class="bloco-bar-track"><div class="bloco-bar-fill" style="width:34%"></div></div></div>
          <div class="bloco-val">3.4</div>
        </div>
        <div class="bloco-item">
          <div class="bloco-name">Segurança</div>
          <div class="bloco-bar-wrap"><div class="bloco-bar-track"><div class="bloco-bar-fill" style="width:42%"></div></div></div>
          <div class="bloco-val">4.2</div>
        </div>
      </div>
    </div>

    <div class="row2">
      <div class="achados-box">
        <h4>Top 3 Acertos</h4>
        <div class="achado-item"><div class="achado-num">01</div><div class="achado-text"><strong>App gratuito e acessível</strong>Disponível em iOS e Android. Nota 4.4/5 — puxada pela qualidade da pizza, não pelo app.</div></div>
        <div class="achado-item"><div class="achado-num">02</div><div class="achado-text"><strong>Rede física consolidada</strong>8 unidades em 3 estados. Estrutura real que poderia, mas ainda não, se conectar ao digital.</div></div>
        <div class="achado-item"><div class="achado-num">03</div><div class="achado-text"><strong>Pedido digital funciona</strong>Fluxo de pedido, pagamento e confirmação por e-mail operando na maioria dos casos.</div></div>
      </div>
      <div class="achados-box">
        <h4>Top 3 Problemas</h4>
        <div class="achado-item"><div class="achado-num">01</div><div class="achado-text"><strong>Contradição grave de dados</strong>App Store: "nenhum dado coletado". Política: nome, e-mail, endereço, Facebook Pixel, Google Analytics. Risco de sanção ANPD.</div></div>
        <div class="achado-item"><div class="achado-num">02</div><div class="achado-text"><strong>Política de privacidade de 2020</strong>Mais de 5 anos sem revisão. Sem cláusula para menores — app classificado como A16.</div></div>
        <div class="achado-item"><div class="achado-num">03</div><div class="achado-text"><strong>DPO via Gmail pessoal</strong>Canal do encarregado de dados é sabordosulpizzas@gmail.com. Sem prazo, sem protocolo, sem identidade corporativa.</div></div>
      </div>
    </div>

    <div class="row3">
      <h4>Achados LGPD — Classificação de Risco</h4>
      <div class="lgpd-grid">
        <div class="lgpd-item"><span class="lgpd-badge critico">Crítico</span><span class="lgpd-txt">Contradição App Store vs. Política de Privacidade</span></div>
        <div class="lgpd-item"><span class="lgpd-badge critico">Crítico</span><span class="lgpd-txt">Sem proteção para dados de menores (art. 14 LGPD)</span></div>
        <div class="lgpd-item"><span class="lgpd-badge alto">Alto</span><span class="lgpd-txt">Política desatualizada — última revisão: out/2020</span></div>
        <div class="lgpd-item"><span class="lgpd-badge alto">Alto</span><span class="lgpd-txt">DPO via Gmail sem canal corporativo estruturado</span></div>
        <div class="lgpd-item"><span class="lgpd-badge alto">Alto</span><span class="lgpd-txt">Retenção de dados por tempo indefinido</span></div>
        <div class="lgpd-item"><span class="lgpd-badge medio">Médio</span><span class="lgpd-txt">Cookies sem opção real de recusa granular</span></div>
      </div>
    </div>

  </div>
  <div class="frase-box">
    <p>"Um app que entrega pizza,<br>mas não entrega privacidade."</p>
    <small>AppCheck Consultoria Digital &nbsp;·&nbsp; Auditoria Sabor do Sul Pizzas &nbsp;·&nbsp; Abril de 2026</small>
  </div>
  <div class="footer">
    <p>Guilherme Argollo &nbsp;·&nbsp; João Pedro Menezes &nbsp;·&nbsp; Elô</p>
    <p>AppCheck Consultoria Digital &nbsp;·&nbsp; Abril de 2026</p>
  </div>
</div>
</body></html>"""

# ============================================================
# PECA 4 - SLIDES
# ============================================================
slides = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Apresentação — Auditoria Sabor do Sul Pizzas</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Segoe UI',Arial,sans-serif; background:#ccc; color:#111; }
.slide { width:960px; min-height:540px; margin:28px auto; background:#fff; position:relative; box-shadow:0 4px 20px rgba(0,0,0,0.2); display:flex; flex-direction:column; border:1px solid #bbb; }
.slide-dark { background:#111; color:#fff; }
.slide-num { position:absolute; bottom:16px; right:22px; font-size:10px; font-weight:700; letter-spacing:2px; opacity:0.3; color:#111; }
.slide-dark .slide-num { color:#fff; }
.slide-header { background:#111; padding:24px 48px; flex-shrink:0; }
.slide-header .label { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:3px; color:#888; margin-bottom:4px; }
.slide-header h2 { font-size:20px; font-weight:800; color:#fff; line-height:1.2; }
.slide-content { flex:1; padding:28px 48px 50px; }

/* CAPA */
.s1-inner { flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:60px; }
.s1-inner .logo { font-size:16px; font-weight:900; letter-spacing:4px; text-transform:uppercase; color:#fff; margin-bottom:4px; }
.s1-inner .logo-sub { font-size:10px; color:#888; letter-spacing:3px; text-transform:uppercase; margin-bottom:48px; }
.s1-inner h1 { font-size:36px; font-weight:900; line-height:1.15; color:#fff; margin-bottom:8px; }
.s1-inner .empresa { font-size:18px; color:#aaa; font-weight:300; margin-bottom:48px; letter-spacing:1px; }
.s1-inner .line { width:40px; height:1px; background:#555; margin:16px auto; }
.s1-inner .team { font-size:12px; color:#777; line-height:2.2; letter-spacing:1px; }

/* GRIDS */
.info-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:8px; }
.info-card { background:#f7f7f7; padding:14px; border-left:2px solid #111; }
.info-card .ic-label { font-size:9px; text-transform:uppercase; letter-spacing:2px; color:#999; font-weight:700; margin-bottom:4px; }
.info-card .ic-val { font-size:16px; font-weight:800; }
.info-card .ic-sub { font-size:11px; color:#888; margin-top:2px; }
.facts { margin-top:14px; display:flex; flex-direction:column; gap:8px; }
.fact-row { display:flex; align-items:flex-start; gap:12px; padding:9px 12px; background:#f7f7f7; font-size:13px; color:#444; line-height:1.4; }
.fact-dot { min-width:6px; height:6px; background:#111; border-radius:50%; margin-top:5px; }

/* TABELA */
table.slide-table { width:100%; border-collapse:collapse; font-size:12px; margin-top:10px; }
.slide-table thead { background:#111; color:#fff; }
.slide-table thead th { padding:9px 12px; text-align:left; font-size:10px; text-transform:uppercase; letter-spacing:1px; font-weight:700; }
.slide-table tbody td { padding:9px 12px; border-bottom:1px solid #eee; color:#444; vertical-align:top; line-height:1.4; }
.slide-table tbody tr:nth-child(even) { background:#fafafa; }
.nota-m { font-weight:800; color:#555; }
.nota-b { font-weight:800; color:#111; }

/* 2 COLS */
.two-cols { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:8px; }
.col-box { border:1px solid #ddd; border-top:2px solid #111; padding:16px; }
.col-box h4 { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:2px; margin-bottom:12px; color:#111; }
.col-item { display:flex; gap:8px; margin-bottom:8px; font-size:12px; color:#444; align-items:flex-start; line-height:1.4; }
.col-dot { min-width:6px; height:6px; background:#111; border-radius:50%; margin-top:4px; flex-shrink:0; }

/* ALERT */
.alert-box { border-left:2px solid #111; background:#f7f7f7; padding:11px 14px; margin-top:12px; font-size:12px; color:#555; line-height:1.6; }

/* MATRIZ */
.matrix-mini { border-collapse:collapse; width:100%; font-size:11px; margin-top:8px; }
.matrix-mini th,.matrix-mini td { border:1px solid #ccc; padding:7px; text-align:center; vertical-align:middle; }
.matrix-mini th { background:#111; color:#fff; font-size:10px; text-transform:uppercase; letter-spacing:1px; }
.risk-c { background:#111; color:#fff; padding:2px 6px; font-size:9px; font-weight:700; display:inline-block; margin:2px; letter-spacing:1px; }
.risk-a { background:#555; color:#fff; padding:2px 6px; font-size:9px; font-weight:700; display:inline-block; margin:2px; letter-spacing:1px; }
.risk-m { background:#ccc; color:#111; padding:2px 6px; font-size:9px; font-weight:700; display:inline-block; margin:2px; letter-spacing:1px; }

/* RECOMENDACOES */
.rec-list { margin-top:8px; display:flex; flex-direction:column; gap:7px; }
.rec-slide { border-left:2px solid #111; padding:10px 14px; background:#f7f7f7; }
.rec-slide .rn { font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#999; margin-bottom:2px; }
.rec-slide .rp { font-size:13px; font-weight:700; margin-bottom:2px; }
.rec-slide .rs { font-size:11px; color:#555; line-height:1.4; }
.rec-slide .rt { font-size:10px; font-weight:700; letter-spacing:1px; color:#111; margin-top:3px; text-transform:uppercase; }

/* 3 COLS FORTES */
.tres-cols { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; margin-top:12px; }
.forte-card { border:1px solid #ddd; border-top:2px solid #111; padding:22px 18px; text-align:center; }
.forte-num { font-size:28px; font-weight:900; color:#eee; margin-bottom:8px; }
.forte-titulo { font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }
.forte-texto { font-size:12px; color:#555; line-height:1.5; }

/* NOTA FINAL */
.final-inner { flex:1; display:flex; align-items:center; gap:60px; padding:40px 60px; }
.final-score-box { text-align:center; flex-shrink:0; }
.final-num { font-size:90px; font-weight:900; line-height:1; color:#fff; }
.final-den { font-size:28px; color:#555; font-weight:300; }
.final-label { font-size:10px; color:#888; text-transform:uppercase; letter-spacing:2px; margin-top:8px; }
.final-selo { display:inline-block; margin-top:14px; border:1px solid #555; color:#ccc; font-size:10px; font-weight:700; padding:5px 14px; letter-spacing:2px; text-transform:uppercase; }
.final-bars { flex:1; }
.bar-big-row { margin-bottom:20px; }
.bar-big-label { font-size:13px; font-weight:700; color:#fff; margin-bottom:7px; display:flex; justify-content:space-between; }
.bar-big-track { background:#333; height:6px; }
.bar-big-fill { height:6px; background:#fff; }
.final-risks { margin-top:24px; font-size:12px; color:#888; line-height:2.2; letter-spacing:1px; }

/* REFLEXAO */
.reflexao-inner { flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:48px 64px; gap:20px; }
.reflexao-inner .question { font-size:20px; font-weight:800; line-height:1.4; max-width:700px; }
.reflexao-inner .answer { font-size:13px; color:#555; max-width:650px; line-height:1.9; }
.reflexao-inner .frase-final { font-size:16px; font-weight:800; border-top:2px solid #111; border-bottom:2px solid #111; padding:14px 0; width:100%; }
.reflexao-inner .creditos { font-size:11px; color:#aaa; letter-spacing:1px; }

@media print { body{background:#fff} .slide{page-break-after:always;margin:0;width:100%;box-shadow:none;border:none} }
</style>
</head>
<body>

<!-- SLIDE 1 CAPA -->
<div class="slide slide-dark">
  <div class="s1-inner">
    <div class="logo">AppCheck</div>
    <div class="logo-sub">Consultoria Digital</div>
    <h1>Auditoria Digital<br>Sabor do Sul Pizzas</h1>
    <div class="line"></div>
    <div class="empresa">Omnichannel · LGPD · Segurança e Desempenho</div>
    <div class="team">Guilherme Argollo — Experiência e Integração Omnichannel<br>João Pedro Menezes — Privacidade e LGPD<br>Elô — Segurança e Desempenho Técnico<br>Abril de 2026</div>
  </div>
  <div class="slide-num">01 / 10</div>
</div>

<!-- SLIDE 2 CONTEXTO -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 02 — Contexto</div><h2>Quem é a Sabor do Sul Pizzas — e por que a escolhemos</h2></div>
  <div class="slide-content">
    <div class="info-grid">
      <div class="info-card"><div class="ic-label">Segmento</div><div class="ic-val">Pizzaria</div><div class="ic-sub">Rede regional de gastronomia</div></div>
      <div class="info-card"><div class="ic-label">Lojas Físicas</div><div class="ic-val">8 unidades</div><div class="ic-sub">Bahia, Alagoas e Rio Grande do Sul</div></div>
      <div class="info-card"><div class="ic-label">App — Versão</div><div class="ic-val">10.9.8</div><div class="ic-sub">iOS 4.4/5 · 78 avaliações · Plataforma Neemo</div></div>
    </div>
    <div class="facts">
      <div class="fact-row"><div class="fact-dot"></div>Atende os três critérios da atividade: loja física acessível, app oficial nas lojas de aplicativos e trata dados pessoais de clientes</div>
      <div class="fact-row"><div class="fact-dot"></div>Escolhemos a empresa por ser uma rede regional em crescimento — um segmento que costuma ter o digital ainda em desenvolvimento, tornando a auditoria mais rica em achados</div>
      <div class="fact-row"><div class="fact-dot"></div>Persona utilizada na visita: jovem de 22 anos fazendo o primeiro pedido pelo app, sem experiência prévia com a marca</div>
    </div>
  </div>
  <div class="slide-num">02 / 10</div>
</div>

<!-- SLIDE 3 METODOLOGIA -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 03 — Metodologia</div><h2>Como conduzimos a auditoria</h2></div>
  <div class="slide-content">
    <div class="two-cols">
      <div class="col-box">
        <h4>O que fizemos</h4>
        <div class="col-item"><div class="col-dot"></div>Instalamos o app em dispositivos iOS e Android</div>
        <div class="col-item"><div class="col-dot"></div>Lemos 78 avaliações na App Store e 20 no Google Play</div>
        <div class="col-item"><div class="col-dot"></div>Analisamos a política de privacidade do site oficial</div>
        <div class="col-item"><div class="col-dot"></div>Pesquisamos histórico de incidentes no Google e na ANPD</div>
        <div class="col-item"><div class="col-dot"></div>Fizemos visita de campo como mystery shoppers</div>
        <div class="col-item"><div class="col-dot"></div>Cronometramos o cadastro e simulamos um pedido completo</div>
        <div class="col-item"><div class="col-dot"></div>Conversamos com um funcionário da loja durante a visita</div>
      </div>
      <div class="col-box">
        <h4>O que nos surpreendeu</h4>
        <div class="col-item"><div class="col-dot"></div>O funcionário que abordamos não sabia que o app existia</div>
        <div class="col-item"><div class="col-dot"></div>Nenhum QR Code ou comunicação sobre o app na loja</div>
        <div class="col-item"><div class="col-dot"></div>O WhatsApp exibido no app não respondeu nossas mensagens</div>
        <div class="col-item"><div class="col-dot"></div>Classificação A16 (álcool/drogas) em um app de pizzaria</div>
        <div class="col-item"><div class="col-dot"></div>Política de privacidade hospedada em link do Google Docs, sem atualização desde 2020</div>
      </div>
    </div>
  </div>
  <div class="slide-num">03 / 10</div>
</div>

<!-- SLIDE 4 BLOCO A -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 04 — Bloco A · Guilherme Argollo</div><h2>Experiência e Integração Omnichannel · Nota: 5.0/10</h2></div>
  <div class="slide-content">
    <table class="slide-table">
      <thead><tr><th>Critério</th><th>O que observamos na prática</th><th>Nota</th></tr></thead>
      <tbody>
        <tr><td>Download e instalação</td><td>Fácil de encontrar e instalar. Nota 4.4/5 — elogios são para a pizza, não para o app.</td><td class="nota-m">7/10</td></tr>
        <tr><td>Integração com a loja física</td><td>Nenhum QR Code, banner ou cupom exclusivo. O funcionário não sabia que o app existia.</td><td class="nota-b">3/10</td></tr>
        <tr><td>Usabilidade e design</td><td>Interface funcional, mas básica. Travou duas vezes durante nosso teste.</td><td class="nota-m">5/10</td></tr>
        <tr><td>Funcionalidades exclusivas</td><td>Só pedido e notificação por e-mail. Sem fidelidade, rastreio em tempo real ou chat.</td><td class="nota-b">4/10</td></tr>
        <tr><td>Custo-benefício</td><td>Gratuito, mas o WhatsApp listado no app não respondeu. Relatos de pedidos errados nas avaliações.</td><td class="nota-m">6/10</td></tr>
      </tbody>
    </table>
    <div class="alert-box"><strong>Principal achado:</strong> O digital e o físico funcionam como dois mundos separados. Não existe nenhuma ponte entre o app e a experiência dentro da loja — o omnichannel, na prática, não existe.</div>
  </div>
  <div class="slide-num">04 / 10</div>
</div>

<!-- SLIDE 5 BLOCO B -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 05 — Bloco B · João Pedro Menezes</div><h2>LGPD e Privacidade · Nota: 3.4/10 · Matriz de Risco</h2></div>
  <div class="slide-content" style="padding-top:20px;">
    <div class="two-cols">
      <div>
        <table class="slide-table">
          <thead><tr><th>Critério</th><th>Nota</th></tr></thead>
          <tbody>
            <tr><td>Política de privacidade</td><td class="nota-b">4/10</td></tr>
            <tr><td>Encarregado (DPO)</td><td class="nota-b">3/10</td></tr>
            <tr><td>Minimização de dados</td><td class="nota-b">4/10</td></tr>
            <tr><td>Consentimento</td><td class="nota-b">4/10</td></tr>
            <tr><td><strong>Permissões do app</strong></td><td class="nota-b"><strong>2/10</strong></td></tr>
            <tr><td>Direitos do titular</td><td class="nota-m">5/10</td></tr>
            <tr><td>Cookies e rastreadores</td><td class="nota-b">3/10</td></tr>
            <tr><td>Bases legais</td><td class="nota-b">3/10</td></tr>
            <tr><td><strong>Dados de menores</strong></td><td class="nota-b"><strong>2/10</strong></td></tr>
            <tr><td>Transparência compart.</td><td class="nota-b">4/10</td></tr>
          </tbody>
        </table>
      </div>
      <div>
        <table class="matrix-mini">
          <thead><tr><th></th><th>Baixo</th><th>Médio</th><th>Alto</th></tr></thead>
          <tbody>
            <tr><td><strong>Alta</strong></td><td><span class="risk-m">Cookies</span></td><td><span class="risk-a">Política 2020</span><br><span class="risk-a">DPO Gmail</span><br><span class="risk-a">Bases vagas</span></td><td><span class="risk-c">App Store vs. Política</span></td></tr>
            <tr><td><strong>Média</strong></td><td></td><td></td><td><span class="risk-c">Sem proteção menores</span></td></tr>
            <tr><td><strong>Baixa</strong></td><td></td><td><span class="risk-m">Transfer. internac.</span></td><td></td></tr>
          </tbody>
        </table>
        <div style="margin-top:10px;font-size:10px;color:#777;line-height:2.2;letter-spacing:1px;">
          <span class="risk-c">CRÍTICO</span> Risco de sanção ANPD<br>
          <span class="risk-a">ALTO</span> Correção imediata<br>
          <span class="risk-m">MÉDIO</span> Melhoria recomendada
        </div>
      </div>
    </div>
  </div>
  <div class="slide-num">05 / 10</div>
</div>

<!-- SLIDE 6 BLOCO C -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 06 — Bloco C · Elô</div><h2>Segurança e Desempenho Técnico · Nota: 4.2/10</h2></div>
  <div class="slide-content">
    <table class="slide-table">
      <thead><tr><th>Critério</th><th>O que observamos</th><th>Nota</th></tr></thead>
      <tbody>
        <tr><td>Autenticação</td><td>Login com e-mail e senha. Sem 2FA, sem login via Google ou Apple. Sem política de força de senha.</td><td class="nota-m">5/10</td></tr>
        <tr><td>Estabilidade</td><td>App travou uma vez durante o teste. Nas avaliações, fechamentos inesperados reportados em iOS e Android.</td><td class="nota-b">4/10</td></tr>
        <tr><td>Desempenho</td><td>Cardápio demora para carregar. Relatos de travamento na hora de finalizar o pedido — o pior momento.</td><td class="nota-b">4/10</td></tr>
        <tr><td>Atualizações</td><td>Última nota de versão: "Correção de push!" — sem descrição do que foi alterado ou corrigido.</td><td class="nota-b">4/10</td></tr>
        <tr><td>Avaliações técnicas</td><td>Problemas recorrentes: WhatsApp sem resposta, pedidos com sabores errados, espera acima de 2h sem atualização.</td><td class="nota-b">4/10</td></tr>
      </tbody>
    </table>
    <div class="alert-box"><strong>Contexto importante:</strong> O app é desenvolvido pela plataforma terceirizada Neemo. A empresa não tem controle direto sobre o código — cada correção depende de um fornecedor externo.</div>
  </div>
  <div class="slide-num">06 / 10</div>
</div>

<!-- SLIDE 7 PONTOS FORTES -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 07 — Pontos Fortes</div><h2>O que a empresa acerta — e pode usar como base para melhorar</h2></div>
  <div class="slide-content" style="display:flex;align-items:center;">
    <div class="tres-cols" style="width:100%;">
      <div class="forte-card"><div class="forte-num">01</div><div class="forte-titulo">App Gratuito e Acessível</div><div class="forte-texto">Fácil de instalar em iOS e Android. Nota 4.4/5 — o produto agrada. O desafio é fazer o app agradar tanto quanto a pizza.</div></div>
      <div class="forte-card"><div class="forte-num">02</div><div class="forte-titulo">Rede Física Consolidada</div><div class="forte-texto">8 unidades em 3 estados mostram que a empresa tem estrutura real — um ativo que o app ainda não sabe aproveitar.</div></div>
      <div class="forte-card"><div class="forte-num">03</div><div class="forte-titulo">Pedido Digital Funciona</div><div class="forte-texto">O fluxo básico de pedir, pagar e receber confirmação por e-mail está de pé. É o ponto de partida para evoluir.</div></div>
    </div>
  </div>
  <div class="slide-num">07 / 10</div>
</div>

<!-- SLIDE 8 RECOMENDACOES -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 08 — Recomendações</div><h2>O que precisa mudar — com prazo definido</h2></div>
  <div class="slide-content">
    <div class="rec-list">
      <div class="rec-slide"><div class="rn">Crítico 01 — LGPD</div><div class="rp">App Store diz "nenhum dado coletado" — política do site diz o contrário</div><div class="rs">Atualizar a ficha nas duas lojas imediatamente. Contratar DPO para revisão completa da política.</div><div class="rt">Prazo: Imediato — até 30 dias</div></div>
      <div class="rec-slide"><div class="rn">Crítico 02 — LGPD</div><div class="rp">Política de 2020 sem revisão e sem cláusula para menores (app classificado como A16)</div><div class="rs">Republicar política com bases legais específicas, prazo de retenção definido e proteção para menores.</div><div class="rt">Prazo: Até 60 dias</div></div>
      <div class="rec-slide"><div class="rn">Alto 03 — LGPD</div><div class="rp">DPO via Gmail pessoal — sem estrutura, sem prazo, sem protocolo</div><div class="rs">Criar canal corporativo com formulário e confirmação automática de recebimento de solicitações.</div><div class="rt">Prazo: Até 60 dias</div></div>
      <div class="rec-slide"><div class="rn">Alto 04 — Omnichannel</div><div class="rp">App e lojas físicas não se comunicam</div><div class="rs">Implementar retirada na loja, QR Codes nas unidades e ao menos um benefício exclusivo para usuários do app.</div><div class="rt">Prazo: Até 6 meses</div></div>
      <div class="rec-slide"><div class="rn">Médio 05 — Técnico</div><div class="rp">Instabilidade, WhatsApp não funcional e autenticação básica</div><div class="rs">Abrir chamado com a Neemo para correção dos bugs e do canal de contato. Avaliar login via Google/Apple e 2FA.</div><div class="rt">Prazo: Até 45 dias</div></div>
    </div>
  </div>
  <div class="slide-num">08 / 10</div>
</div>

<!-- SLIDE 9 NOTA FINAL -->
<div class="slide slide-dark">
  <div class="slide-header" style="background:rgba(255,255,255,0.05);border-bottom:1px solid #333;">
    <div class="label">Slide 09 — Resultado</div>
    <h2>Nota Final Consolidada da Auditoria</h2>
  </div>
  <div class="final-inner">
    <div class="final-score-box">
      <div class="final-num">4.3<span class="final-den">/10</span></div>
      <div class="final-label">Nota Geral</div>
      <div class="final-selo">Parcialmente Conforme</div>
    </div>
    <div class="final-bars">
      <div class="bar-big-row"><div class="bar-big-label"><span>Experiência e Omnichannel</span><span>5.0</span></div><div class="bar-big-track"><div class="bar-big-fill" style="width:50%"></div></div></div>
      <div class="bar-big-row"><div class="bar-big-label"><span>Privacidade e LGPD</span><span>3.4</span></div><div class="bar-big-track"><div class="bar-big-fill" style="width:34%"></div></div></div>
      <div class="bar-big-row"><div class="bar-big-label"><span>Segurança e Desempenho</span><span>4.2</span></div><div class="bar-big-track"><div class="bar-big-fill" style="width:42%"></div></div></div>
      <div class="final-risks">2 riscos CRÍTICOS identificados<br>3 riscos ALTOS identificados<br>2 riscos MÉDIOS identificados</div>
    </div>
  </div>
  <div class="slide-num">09 / 10</div>
</div>

<!-- SLIDE 10 REFLEXAO -->
<div class="slide">
  <div class="slide-header"><div class="label">Slide 10 — Reflexão Final</div><h2>Esta empresa respeita o cliente digital de 2026?</h2></div>
  <div class="reflexao-inner">
    <div class="question">O app realmente aproxima o físico do digital<br>sem atropelar a privacidade do usuário?</div>
    <div class="answer">A Sabor do Sul Pizzas tem algo valioso: um produto que as pessoas gostam. A nota 4.4 existe por causa da pizza, não do app. O funcionário que abordamos na loja nem sabia que o app existia — isso resume bem onde a empresa está hoje.<br><br>Do ponto de vista da privacidade, a situação é mais urgente: declarar que nenhum dado é coletado enquanto a política diz o contrário não é um erro pequeno. É exatamente o tipo de contradição que pode chamar a atenção de um fiscal da ANPD. A empresa tem estrutura para corrigir isso — falta apenas prioridade.</div>
    <div class="frase-final">"Um app que entrega pizza, mas não entrega privacidade."</div>
    <div class="creditos">AppCheck Consultoria Digital &nbsp;·&nbsp; Guilherme Argollo · João Pedro Menezes · Elô &nbsp;·&nbsp; Abril de 2026</div>
  </div>
  <div class="slide-num">10 / 10</div>
</div>

</body></html>"""

files = {
    'C:/Users/guilherme/auditoria-peca1-sumario.html': sumario,
    'C:/Users/guilherme/auditoria-peca2-relatorio.html': relatorio,
    'C:/Users/guilherme/auditoria-peca3-infografico.html': dashboard,
    'C:/Users/guilherme/auditoria-peca4-slides.html': slides,
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"OK: {path}")

print("Todos os 4 arquivos gerados com sucesso.")
