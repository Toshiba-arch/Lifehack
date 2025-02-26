<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WhatsApp IA Responder</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/flowbite@1.6.5/dist/flowbite.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/flowbite@1.6.5/dist/flowbite.min.js"></script>
  <style>
    :root {
      --primary-color: #5D5CDE;
      --whatsapp-color: #25D366;
      --whatsapp-dark: #128C7E;
    }
    
    .dark {
      --bg-main: #181818;
      --text-main: #f3f4f6;
      --card-bg: #262626;
    }
    
    .light {
      --bg-main: #ffffff;
      --text-main: #1f2937;
      --card-bg: #f9fafb;
    }
    
    @media (prefers-color-scheme: dark) {
      :root {
        --bg-main: #181818;
        --text-main: #f3f4f6;
        --card-bg: #262626;
      }
    }
    
    @media (prefers-color-scheme: light) {
      :root {
        --bg-main: #ffffff;
        --text-main: #1f2937;
        --card-bg: #f9fafb;
      }
    }
    
    body {
      background-color: var(--bg-main);
      color: var(--text-main);
      transition: background-color 0.3s, color 0.3s;
    }
    
    .card {
      background-color: var(--card-bg);
      border-radius: 0.5rem;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .tab-content {
      display: none;
    }
    
    .tab-content.active {
      display: block;
    }
    
    .whatsapp-bg {
      background-color: var(--whatsapp-color);
    }
    
    .whatsapp-text {
      color: var(--whatsapp-color);
    }
    
    .whatsapp-btn {
      background-color: var(--whatsapp-color);
      transition: background-color 0.3s;
    }
    
    .whatsapp-btn:hover {
      background-color: var(--whatsapp-dark);
    }
    
    .chat-bubble {
      max-width: 80%;
      padding: 8px 12px;
      border-radius: 8px;
      margin-bottom: 8px;
      position: relative;
    }
    
    .message-in {
      background-color: #dcf8c6;
      color: #000;
      align-self: flex-start;
    }
    
    .message-out {
      background-color: #f0f0f0;
      color: #000;
      align-self: flex-end;
    }
    
    .toggle-checkbox:checked {
      right: 0;
      border-color: var(--whatsapp-color);
    }
    
    .toggle-checkbox:checked + .toggle-label {
      background-color: var(--whatsapp-color);
    }
    
    .bot-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background-color: #5D5CDE;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: bold;
    }
    
    .typing-indicator {
      display: inline-flex;
      align-items: center;
      margin-right: 5px;
      transition: opacity 0.3s;
    }
    
    .typing-indicator span {
      height: 8px;
      width: 8px;
      background-color: #555;
      border-radius: 50%;
      display: block;
      margin: 0 2px;
      opacity: 0.5;
    }
    
    .typing-indicator span:nth-child(1) {
      animation: bounce 1s infinite;
    }
    
    .typing-indicator span:nth-child(2) {
      animation: bounce 1s infinite 0.2s;
    }
    
    .typing-indicator span:nth-child(3) {
      animation: bounce 1s infinite 0.4s;
    }
    
    @keyframes bounce {
      0%, 60%, 100% {
        transform: translateY(0);
      }
      30% {
        transform: translateY(-4px);
      }
    }
    
    .loading-spinner {
      border: 3px solid #f3f3f3;
      border-top: 3px solid var(--whatsapp-color);
      border-radius: 50%;
      width: 20px;
      height: 20px;
      animation: spin 1s linear infinite;
      display: inline-block;
      margin-right: 10px;
    }
    
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    
    .notification-badge {
      position: absolute;
      top: -5px;
      right: -5px;
      background-color: #ef4444;
      color: white;
      border-radius: 50%;
      width: 18px;
      height: 18px;
      font-size: 11px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  </style>
</head>
<body class="min-h-screen p-4">
  <div class="container mx-auto max-w-6xl">
    <header class="flex flex-col md:flex-row items-center justify-between mb-6 p-4 rounded-lg card">
      <div class="flex items-center mb-4 md:mb-0">
        <div class="text-3xl mr-3 whatsapp-text">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
          </svg>
        </div>
        <h1 class="text-2xl font-bold">WhatsApp IA Responder</h1>
      </div>
      <div class="flex space-x-3">
        <a href="#configuracao" class="whatsapp-btn hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105">
          Configurar
        </a>
        <a href="#simulacao" class="whatsapp-btn hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105">
          Testar
        </a>
      </div>
    </header>

    <div class="flex flex-wrap mb-4">
      <div class="w-full">
        <ul class="flex flex-wrap text-sm font-medium text-center border-b border-gray-300" id="tabs">
          <li class="mr-2">
            <a href="#" class="tab-link inline-block p-4 rounded-t-lg active" data-tab="dashboard">Dashboard</a>
          </li>
          <li class="mr-2">
            <a href="#" class="tab-link inline-block p-4 rounded-t-lg" data-tab="configuracao">Configuração</a>
          </li>
          <li class="mr-2">
            <a href="#" class="tab-link inline-block p-4 rounded-t-lg" data-tab="simulacao">Simulação</a>
          </li>
          <li class="mr-2">
            <a href="#" class="tab-link inline-block p-4 rounded-t-lg" data-tab="instrucoes">Instruções</a>
          </li>
        </ul>
      </div>
    </div>

    <div id="dashboard" class="tab-content active">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="card p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-xl font-semibold">Status</h3>
            <span class="px-3 py-1 text-xs font-medium rounded-full bg-red-100 text-red-800" id="status-badge">Offline</span>
          </div>
          <div class="flex items-center justify-between mb-2">
            <span>Serviço Local:</span>
            <div class="relative inline-block w-10 mr-2 align-middle select-none">
              <input type="checkbox" id="toggle-service" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer"/>
              <label for="toggle-service" class="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer"></label>
            </div>
          </div>
          <div class="flex items-center justify-between mb-4">
            <span>Resposta Automática:</span>
            <div class="relative inline-block w-10 mr-2 align-middle select-none">
              <input type="checkbox" id="toggle-auto" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer"/>
              <label for="toggle-auto" class="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer"></label>
            </div>
          </div>
          <div class="mt-4">
            <button id="start-service" class="w-full whatsapp-btn text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105">
              Iniciar Serviço
            </button>
          </div>
        </div>

        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Estatísticas</h3>
          <div class="grid grid-cols-2 gap-4">
            <div class="text-center p-3 bg-gray-100 dark:bg-gray-700 rounded-lg">
              <span class="block text-2xl font-bold">0</span>
              <span class="text-sm">Mensagens Recebidas</span>
            </div>
            <div class="text-center p-3 bg-gray-100 dark:bg-gray-700 rounded-lg">
              <span class="block text-2xl font-bold">0</span>
              <span class="text-sm">Respostas Automáticas</span>
            </div>
            <div class="text-center p-3 bg-gray-100 dark:bg-gray-700 rounded-lg">
              <span class="block text-2xl font-bold">0</span>
              <span class="text-sm">Grupos Ativos</span>
            </div>
            <div class="text-center p-3 bg-gray-100 dark:bg-gray-700 rounded-lg">
              <span class="block text-2xl font-bold">0</span>
              <span class="text-sm">Contatos Ativos</span>
            </div>
          </div>
        </div>

        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Modelo IA</h3>
          <div class="mb-4">
            <label for="ia-model" class="block mb-2 text-sm font-medium">Modelo Selecionado:</label>
            <select id="ia-model" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="claude" selected>Claude-3.7-Sonnet</option>
              <option value="gpt4">GPT-4o</option>
              <option value="local">Modelo Local</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="prompt-template" class="block mb-2 text-sm font-medium">Template de Prompt:</label>
            <textarea id="prompt-template" rows="3" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Responda como um assistente amigável...">Você é um assistente útil respondendo em um chat do WhatsApp. Seja conciso, cordial e forneça informações precisas.</textarea>
          </div>
          <div>
            <button id="test-ai" class="w-full whatsapp-btn text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105">
              Testar Modelo
            </button>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Conversas Recentes</h3>
          <div class="divide-y divide-gray-200 dark:divide-gray-700">
            <div class="flex items-center justify-between py-3">
              <div class="flex items-center">
                <div class="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold mr-3">
                  F
                </div>
                <div>
                  <p class="font-medium">Família (Grupo)</p>
                  <p class="text-sm text-gray-500 dark:text-gray-400 truncate">João: Quando vamos nos encontrar?</p>
                </div>
              </div>
              <span class="text-xs text-gray-500">12:30</span>
            </div>
            <div class="flex items-center justify-between py-3">
              <div class="flex items-center">
                <div class="w-10 h-10 rounded-full bg-purple-500 flex items-center justify-center text-white font-bold mr-3">
                  M
                </div>
                <div>
                  <p class="font-medium">Maria Silva</p>
                  <p class="text-sm text-gray-500 dark:text-gray-400 truncate">Obrigado pela ajuda!</p>
                </div>
              </div>
              <span class="text-xs text-gray-500">09:45</span>
            </div>
            <div class="flex items-center justify-between py-3">
              <div class="flex items-center">
                <div class="w-10 h-10 rounded-full bg-green-500 flex items-center justify-center text-white font-bold mr-3">
                  T
                </div>
                <div>
                  <p class="font-medium">Trabalho (Grupo)</p>
                  <p class="text-sm text-gray-500 dark:text-gray-400 truncate">Ana: Reunião confirmada?</p>
                </div>
              </div>
              <span class="text-xs text-gray-500">Ontem</span>
            </div>
          </div>
        </div>

        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Registro de Atividades</h3>
          <div class="bg-gray-100 dark:bg-gray-700 p-3 rounded-lg h-64 overflow-y-auto font-mono text-sm">
            <p class="text-green-600 dark:text-green-400">[SISTEMA] Iniciando aplicação WhatsApp IA Responder...</p>
            <p class="text-yellow-600 dark:text-yellow-400">[AVISO] Serviço não configurado</p>
            <p class="text-gray-600 dark:text-gray-400">[INFO] Aguardando configuração do usuário</p>
            <p class="text-gray-600 dark:text-gray-400">[INFO] Modelo de IA selecionado: Claude-3.7-Sonnet</p>
          </div>
        </div>
      </div>
    </div>

    <div id="configuracao" class="tab-content">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Configuração Geral</h3>
          
          <div class="mb-4">
            <label for="installation-method" class="block mb-2 text-sm font-medium">Método de Instalação:</label>
            <select id="installation-method" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="local" selected>Local (WhatsApp Web + Automação)</option>
              <option value="unofficial" disabled>Biblioteca Não Oficial (whatsapp-web.js)</option>
              <option value="business" disabled>API WhatsApp Business (Requer Conta Empresarial)</option>
            </select>
          </div>
          
          <div class="mb-4">
            <label for="auto-start" class="flex items-center space-x-2 cursor-pointer">
              <input type="checkbox" id="auto-start" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
              <span class="text-sm font-medium">Iniciar automaticamente com o sistema</span>
            </label>
          </div>
          
          <div class="mb-4">
            <label for="session-timeout" class="block mb-2 text-sm font-medium">Tempo Limite de Sessão (minutos):</label>
            <input type="number" id="session-timeout" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" value="60" min="1" max="1440">
          </div>
          
          <div class="mb-4">
            <label for="message-delay" class="block mb-2 text-sm font-medium">Atraso entre mensagens (segundos):</label>
            <input type="number" id="message-delay" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" value="2" min="0" max="60">
          </div>
          
          <div class="mb-4">
            <label for="notification-sound" class="flex items-center space-x-2 cursor-pointer">
              <input type="checkbox" id="notification-sound" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" checked>
              <span class="text-sm font-medium">Ativar sons de notificação</span>
            </label>
          </div>
        </div>

        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Configuração de Resposta</h3>
          
          <div class="mb-4">
            <label for="response-mode" class="block mb-2 text-sm font-medium">Modo de Resposta:</label>
            <select id="response-mode" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="all">Responder a todas as mensagens</option>
              <option value="mentions" selected>Responder apenas quando mencionado</option>
              <option value="keywords">Responder baseado em palavras-chave</option>
              <option value="custom">Personalizado (Baseado em regras)</option>
            </select>
          </div>
          
          <div class="mb-4">
            <label for="trigger-words" class="block mb-2 text-sm font-medium">Palavras/Frases Gatilho (uma por linha):</label>
            <textarea id="trigger-words" rows="3" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="bot
assistente
ajuda
/start">bot
assistente
ajuda
/start</textarea>
          </div>
          
          <div class="mb-4">
            <label for="ignore-users" class="block mb-2 text-sm font-medium">Ignorar Usuários (um por linha):</label>
            <textarea id="ignore-users" rows="2" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="+5511987654321"></textarea>
          </div>
          
          <div class="mb-4">
            <label for="response-template" class="block mb-2 text-sm font-medium">Template de Resposta:</label>
            <textarea id="response-template" rows="2" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="[Nome], [Resposta IA]">[Nome], [Resposta IA]</textarea>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Configuração de Grupos</h3>
          
          <div class="mb-4">
            <label for="group-mode" class="block mb-2 text-sm font-medium">Modo de Resposta em Grupos:</label>
            <select id="group-mode" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="all">Responder em todos os grupos</option>
              <option value="whitelist" selected>Responder apenas em grupos permitidos</option>
              <option value="blacklist">Responder em todos exceto grupos bloqueados</option>
              <option value="none">Não responder em grupos</option>
            </select>
          </div>
          
          <div class="mb-4">
            <label for="allowed-groups" class="block mb-2 text-sm font-medium">Grupos Permitidos (um por linha):</label>
            <textarea id="allowed-groups" rows="3" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Família
Trabalho
Amigos">Família
Trabalho
Amigos</textarea>
          </div>
          
          <div class="mb-4">
            <label for="group-mention-required" class="flex items-center space-x-2 cursor-pointer">
              <input type="checkbox" id="group-mention-required" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" checked>
              <span class="text-sm font-medium">Exigir menção explícita nos grupos</span>
            </label>
          </div>
        </div>

        <div class="card p-6">
          <h3 class="text-xl font-semibold mb-4">Configuração de IA</h3>
          
          <div class="mb-4">
            <label for="ai-provider" class="block mb-2 text-sm font-medium">Provedor de IA:</label>
            <select id="ai-provider" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="poe" selected>Poe (Claude, GPT)</option>
              <option value="local">Modelo Local (Ollama, LM Studio)</option>
              <option value="openai">OpenAI (Requer API Key)</option>
              <option value="anthropic">Anthropic (Requer API Key)</option>
            </select>
          </div>
          
          <div class="mb-4">
            <label for="system-prompt" class="block mb-2 text-sm font-medium">Prompt do Sistema:</label>
            <textarea id="system-prompt" rows="5" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Você é um assistente útil...">Você é um assistente útil respondendo em um chat do WhatsApp. Mantenha suas respostas curtas, claras e amigáveis. Não use emojis em excesso. Evite respostas muito longas, pois estamos em um chat de mensagens. Se não souber a resposta, seja honesto e direto. Nunca mencione que é uma IA a menos que seja perguntado diretamente.</textarea>
          </div>
          
          <div class="mb-4">
            <label for="max-tokens" class="block mb-2 text-sm font-medium">Tamanho Máximo de Resposta:</label>
            <input type="number" id="max-tokens" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" value="300" min="50" max="2000">
          </div>
          
          <div class="mb-4">
            <label for="temperature" class="block mb-2 text-sm font-medium">Temperatura (Criatividade): <span id="temp-value">0.7</span></label>
            <input type="range" id="temperature" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700" min="0" max="1" step="0.1" value="0.7">
          </div>
        </div>
      </div>
      
      <div class="mt-6 flex justify-end space-x-4">
        <button id="reset-config" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded transition duration-300 ease-in-out">
          Restaurar Padrões
        </button>
        <button id="save-config" class="whatsapp-btn hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105">
          Salvar Configurações
        </button>
      </div>
    </div>

    <div id="simulacao" class="tab-content">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-1 card p-4">
          <h3 class="text-xl font-semibold mb-4">Configurações de Teste</h3>
          
          <div class="mb-4">
            <label for="test-chat-type" class="block mb-2 text-sm font-medium">Tipo de Chat:</label>
            <select id="test-chat-type" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="individual" selected>Chat Individual</option>
              <option value="group">Chat em Grupo</option>
            </select>
          </div>
          
          <div class="mb-4">
            <label for="test-user-name" class="block mb-2 text-sm font-medium">Seu Nome:</label>
            <input type="text" id="test-user-name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" value="Você" placeholder="Seu nome">
          </div>
          
          <div class="mb-4 group-chat-option hidden">
            <label for="test-group-name" class="block mb-2 text-sm font-medium">Nome do Grupo:</label>
            <input type="text" id="test-group-name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" value="Família" placeholder="Nome do grupo">
          </div>
          
          <div class="mb-4 group-chat-option hidden">
            <label for="test-bot-name" class="block mb-2 text-sm font-medium">Nome do Bot:</label>
            <input type="text" id="test-bot-name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" value="WhatsBot" placeholder="Nome do bot no grupo">
          </div>
          
          <div class="mb-4">
            <label for="test-mode" class="block mb-2 text-sm font-medium">Modo de Teste:</label>
            <select id="test-mode" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option value="live" selected>Teste ao Vivo (usando IA real)</option>
              <option value="simulated">Simulado (resposta pré-definida)</option>
            </select>
          </div>
          
          <div class="mt-6">
            <button id="clear-chat" class="w-full bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded transition duration-300 ease-in-out mb-4">
              Limpar Conversa
            </button>
          </div>
        </div>

        <div class="lg:col-span-2 card p-4 flex flex-col h-[600px]">
          <div class="flex items-center border-b pb-3">
            <div class="w-10 h-10 rounded-full bg-green-500 flex items-center justify-center text-white font-bold mr-3" id="chat-avatar">
              M
            </div>
            <div>
              <h3 class="font-semibold" id="chat-name">Maria Silva</h3>
              <p class="text-xs text-gray-500" id="chat-status">online</p>
            </div>
          </div>
          
          <div class="flex-1 overflow-y-auto p-4 space-y-2" id="chat-messages">
            <!-- As mensagens serão adicionadas aqui dinamicamente -->
          </div>
          
          <div class="border-t pt-3 mt-auto">
            <div class="flex items-center">
              <input type="text" id="message-input" class="flex-1 bg-gray-50 border border-gray-300 text-gray-900 text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Digite uma mensagem...">
              <button id="send-message" class="ml-2 whatsapp-btn text-white p-2.5 rounded-full">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="instrucoes" class="tab-content">
      <div class="card p-6">
        <h2 class="text-2xl font-bold mb-4">Como Configurar seu Bot WhatsApp com IA Local</h2>
        
        <div class="mb-6">
          <h3 class="text-xl font-semibold mb-2">Requisitos</h3>
          <ul class="list-disc pl-6 space-y-1">
            <li>Computador com Windows, Mac ou Linux para hospedar o bot</li>
            <li>Node.js instalado (versão 14 ou superior)</li>
            <li>WhatsApp Web acessível no navegador</li>
            <li>Conexão com internet</li>
          </ul>
        </div>
        
        <div class="mb-6">
          <h3 class="text-xl font-semibold mb-2">Opção 1: WhatsApp Web + Automação Local (Recomendado para Uso Pessoal)</h3>
          <p class="mb-3">Esta abordagem usa automação local para interagir com o WhatsApp Web sem precisar de uma conta Business ou API oficial.</p>
          
          <h4 class="font-semibold mt-4 mb-2">Passo 1: Instalar dependências</h4>
          <div class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg font-mono text-sm mb-4 overflow-x-auto">
            # Instalar Node.js do site oficial https://nodejs.org/
            
            # Criar pasta para o projeto
            mkdir whatsapp-ia-bot
            cd whatsapp-ia-bot
            
            # Inicializar projeto Node.js
            npm init -y
            
            # Instalar dependências necessárias
            npm install puppeteer puppeteer-extra puppeteer-extra-plugin-stealth
          </div>
          
          <h4 class="font-semibold mt-4 mb-2">Passo 2: Configurar conexão com modelo de IA</h4>
          <p class="mb-2">Você pode usar o Poe ou um modelo local:</p>
          <div class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg font-mono text-sm mb-4 overflow-x-auto">
            # Para usar modelos locais (Ollama)
            npm install ollama

            # OU para usar OpenAI API
            npm install openai
          </div>
          
          <h4 class="font-semibold mt-4 mb-2">Passo 3: Criar arquivo principal do bot</h4>
          <p class="mb-2">Criar arquivo <code>index.js</code> com o código a seguir:</p>
          <div class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg font-mono text-sm mb-4 overflow-x-auto">
            const puppeteer = require('puppeteer-extra');
            const StealthPlugin = require('puppeteer-extra-plugin-stealth');
            puppeteer.use(StealthPlugin());
            
            // Configurações do bot (substitua por configurações do banco de dados ou arquivo)
            const config = {
              responseMode: 'mentions',
              triggerWords: ['bot', 'assistente', 'ajuda', '/start'],
              groupMode: 'whitelist',
              allowedGroups: ['Família', 'Trabalho', 'Amigos'],
              requireMention: true,
              systemPrompt: 'Você é um assistente útil respondendo em um chat do WhatsApp...'
            };
            
            // Função para processar mensagens com IA
            async function processWithAI(message) {
              // Implementar conexão com a IA de sua escolha
              // Exemplo simples:
              return `Isso é uma resposta simulada para: "${message}"`;
            }
            
            async function startBot() {
              const browser = await puppeteer.launch({
                headless: false, // Deixe como false para ver o navegador e escanear QR
                args: ['--no-sandbox', '--disable-setuid-sandbox']
              });
              
              const page = await browser.newPage();
              await page.goto('https://web.whatsapp.com');
              
              console.log('Escaneie o código QR para entrar no WhatsApp Web');
              
              // Aguardar login
              await page.waitForSelector('._3WByx', { timeout: 60000 })
                .catch(() => console.log('Timeout aguardando login. Tente novamente.'));
              
              console.log('Login realizado com sucesso!');
              
              // Monitorar novas mensagens
              page.on('domcontentloaded', async () => {
                // Lógica para detectar e responder a novas mensagens
                // Implementação completa requer mais código
              });
              
              // Manter o bot rodando
              process.on('SIGINT', async () => {
                console.log('Encerrando bot...');
                await browser.close();
                process.exit();
              });
            }
            
            startBot().catch(console.error);
          </div>
          
          <h4 class="font-semibold mt-4 mb-2">Passo 4: Executar o bot</h4>
          <div class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg font-mono text-sm mb-4 overflow-x-auto">
            node index.js
          </div>
          <p class="mb-2">Um navegador será aberto com o WhatsApp Web. Escaneie o código QR com seu celular para fazer login.</p>
        </div>
        
        <div class="mb-6">
          <h3 class="text-xl font-semibold mb-2">Opção 2: Biblioteca Não Oficial (Para Desenvolvedores)</h3>
          <p class="mb-3">Use a biblioteca whatsapp-web.js para uma integração mais robusta (mas ainda não oficial).</p>
          
          <h4 class="font-semibold mt-4 mb-2">Passo 1: Instalar dependências</h4>
          <div class="bg-gray-100 dark:bg-gray-800 p-3 rounded-lg font-mono text-sm mb-2 overflow-x-auto">
            npm install whatsapp-web.js qrcode-terminal
          </div>
          
          <h4 class="font-semibold mt-4 mb-2">Documentação e tutoriais</h4>
          <p class="mb-2">Consulte a <a href="https://wwebjs.dev/" target="_blank" class="text-blue-600 hover:underline">documentação oficial</a> para implementação detalhada.</p>
        </div>
        
        <div class="mt-6 bg-yellow-100 dark:bg-yellow-900 p-4 rounded-lg">
          <h3 class="text-lg font-semibold mb-2">⚠️ Avisos Importantes</h3>
          <ul class="list-disc pl-6 space-y-1 text-sm">
            <li>O uso de bibliotecas não oficiais ou automação do WhatsApp pode violar os Termos de Serviço.</li>
            <li>O WhatsApp pode detectar e bloquear contas que usam clientes não oficiais.</li>
            <li>Recomendamos usar apenas para fins pessoais ou educacionais.</li>
            <li>Para uso comercial, considere a API oficial do WhatsApp Business.</li>
            <li>Esta aplicação é apenas um demonstrativo de como seria a interface de configuração.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Configurar funcionamento das tabs
    document.addEventListener('DOMContentLoaded', function() {
      const tabs = document.querySelectorAll('.tab-link');
      const tabContents = document.querySelectorAll('.tab-content');
      tabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
          e.preventDefault();
          
          // Remover classe active de todas as tabs
          tabs.forEach(t => t.classList.remove('active'));
          
          // Adicionar classe active na tab clicada
          tab.classList.add('active');
          
          // Esconder todos os conteúdos
          tabContents.forEach(content => {
            content.classList.remove('active');
          });
          
          // Mostrar o conteúdo correspondente
          const tabId = tab.getAttribute('data-tab');
          document.getElementById(tabId).classList.add('active');
        });
      });
      // Configurar links no header
      document.querySelectorAll('header a').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const targetId = link.getAttribute('href').substring(1);
          
          // Encontrar e clicar na tab correspondente
          const targetTab = document.querySelector(`.tab-link[data-tab="${targetId}"]`);
          if (targetTab) {
            targetTab.click();
          }
        });
      });
      // Configurar toggles do dashboard
      const toggleService = document.getElementById('toggle-service');
      const toggleAuto = document.getElementById('toggle-auto');
      const statusBadge = document.getElementById('status-badge');
      const startButton = document.getElementById('start-service');
      toggleService.addEventListener('change', function() {
        if (this.checked) {
          toggleAuto.disabled = false;
          startButton.textContent = 'Parar Serviço';
          statusBadge.textContent = 'Conectando...';
          statusBadge.className = 'px-3 py-1 text-xs font-medium rounded-full bg-yellow-100 text-yellow-800';
          
          setTimeout(() => {
            statusBadge.textContent = 'Online';
            statusBadge.className = 'px-3 py-1 text-xs font-medium rounded-full bg-green-100 text-green-800';
          }, 2000);
        } else {
          toggleAuto.checked = false;
          toggleAuto.disabled = true;
          startButton.textContent = 'Iniciar Serviço';
          statusBadge.textContent = 'Offline';
          statusBadge.className = 'px-3 py-1 text-xs font-medium rounded-full bg-red-100 text-red-800';
        }
      });
      startButton.addEventListener('click', function() {
        toggleService.checked = !toggleService.checked;
        const event = new Event('change');
        toggleService.dispatchEvent(event);
      });
      // Configurar temperatura na página de configuração
      const temperatureSlider = document.getElementById('temperature');
      const tempValue = document.getElementById('temp-value');
      
      temperatureSlider.addEventListener('input', function() {
        tempValue.textContent = this.value;
      });
      // Configurar botões na página de configuração
      const saveConfigBtn = document.getElementById('save-config');
      const resetConfigBtn = document.getElementById('reset-config');
      
      saveConfigBtn.addEventListener('click', function() {
        alert('Configurações salvas com sucesso!');
      });
      
      resetConfigBtn.addEventListener('click', function() {
        if (confirm('Deseja restaurar todas as configurações para os valores padrão?')) {
          // Reset form fields...
          document.getElementById('trigger-words').value = 'bot\nassistente\najuda\n/start';
          document.getElementById('system-prompt').value = 'Você é um assistente útil respondendo em um chat do WhatsApp. Mantenha suas respostas curtas, claras e amigáveis. Não use emojis em excesso. Evite respostas muito longas, pois estamos em um chat de mensagens. Se não souber a resposta, seja honesto e direto. Nunca mencione que é uma IA a menos que seja perguntado diretamente.';
          temperatureSlider.value = 0.7;
          tempValue.textContent = '0.7';
        }
      });
      // Configurar simulação de chat
      const chatType = document.getElementById('test-chat-type');
      const groupOptions = document.querySelectorAll('.group-chat-option');
      const chatName = document.getElementById('chat-name');
      const chatAvatar = document.getElementById('chat-avatar');
      const chatMessages = document.getElementById('chat-messages');
      const messageInput = document.getElementById('message-input');
      const sendButton = document.getElementById('send-message');
      const clearChatButton = document.getElementById('clear-chat');
      const testUserName = document.getElementById('test-user-name');
      const testGroupName = document.getElementById('test-group-name');
      const testBotName = document.getElementById('test-bot-name');
      const testMode = document.getElementById('test-mode');
      // Mostrar/esconder opções de grupo
      chatType.addEventListener('change', function() {
        if (this.value === 'group') {
          groupOptions.forEach(opt => opt.classList.remove('hidden'));
          chatName.textContent = testGroupName.value;
          chatAvatar.textContent = testGroupName.value.charAt(0);
          chatAvatar.classList.remove('bg-purple-500');
          chatAvatar.classList.add('bg-blue-500');
        } else {
          groupOptions.forEach(opt => opt.classList.add('hidden'));
          chatName.textContent = 'Chat Individual';
          chatAvatar.textContent = 'C';
          chatAvatar.classList.remove('bg-blue-500');
          chatAvatar.classList.add('bg-purple-500');
        }
      });
      testUserName.addEventListener('input', function() {
        // Atualizar nome do usuário na simulação
      });
      testGroupName.addEventListener('input', function() {
        if (chatType.value === 'group') {
          chatName.textContent = this.value;
          chatAvatar.textContent = this.value.charAt(0);
        }
      });
      // Enviar mensagem simulada
      function sendMessage() {
        const messageText = messageInput.value.trim();
        if (!messageText) return;
        const isGroup = chatType.value === 'group';
        const userName = testUserName.value;
        const botName = testBotName.value;
        // Adicionar mensagem do usuário
        addChatMessage(messageText, 'outgoing', userName);
        messageInput.value = '';
        // Verificar se a mensagem aciona o bot
        const shouldRespond = checkIfShouldRespond(messageText, isGroup, botName);
        
        if (shouldRespond) {
          // Mostrar indicador de digitação
          showTypingIndicator();
          
          // Responder após um pequeno delay
          setTimeout(() => {
            // Ocultar indicador de digitação
            hideTypingIndicator();
            
            if (testMode.value === 'live') {
              // Chamar IA real através do Poe
              callRealAI(messageText);
            } else {
              // Resposta simulada
              const response = generateSimulatedResponse(messageText);
              const respondentName = isGroup ? botName : 'Assistente';
              addChatMessage(response, 'incoming', respondentName);
            }
          }, 1500);
        }
      }
      // Funções de simulação
      function checkIfShouldRespond(message, isGroup, botName) {
        message = message.toLowerCase();
        
        if (isGroup) {
          // No grupo, responder apenas se mencionado ou usando palavras-chave
          return message.includes(`@${botName.toLowerCase()}`) || 
                 ['bot', 'assistente', 'ajuda', '/start'].some(word => message.includes(word));
        } else {
          // Em chat individual, responder a tudo
          return true;
        }
      }
      function generateSimulatedResponse(message) {
        const responses = [
          `Entendi sua mensagem. Como posso ajudar com "${message.substring(0, 30)}${message.length > 30 ? '...' : ''}"?`,
          "Vou verificar isso para você!",
          "Obrigado por sua mensagem. Posso fornecer mais informações se precisar.",
          "Ótima pergunta! A resposta depende de vários fatores.",
          "Compreendi sua solicitação e estou processando uma resposta adequada."
        ];
        
        return responses[Math.floor(Math.random() * responses.length)];
      }
      async function callRealAI(message) {
        try {
          // Registrar handler para resposta da IA
          window.Poe.registerHandler("ai-response-handler", (result) => {
            if (result.responses && result.responses.length > 0) {
              const response = result.responses[0];
              
              if (response.status === "complete") {
                const isGroup = chatType.value === 'group';
                const botName = isGroup ? testBotName.value : 'Assistente';
                addChatMessage(response.content, 'incoming', botName);
              } else if (response.status === "error") {
                addSystemMessage("Erro ao obter resposta da IA: " + (response.statusText || "Erro desconhecido"));
              }
            }
          });
          
          // Enviar mensagem para o Claude
          await window.Poe.sendUserMessage(
            "@Claude-3.7-Sonnet " + message,
            {
              handler: "ai-response-handler",
              stream: false,
              openChat: false
            }
          );
        } catch (err) {
          addSystemMessage("Erro ao chamar IA: " + err.message);
        }
      }
      function showTypingIndicator() {
        // Remover indicador existente se houver
        hideTypingIndicator();
        
        // Criar e adicionar novo indicador
        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.className = 'chat-bubble message-in flex items-center';
        typingDiv.innerHTML = `
          <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <span class="text-xs text-gray-500 ml-1">digitando...</span>
        `;
        
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
      function hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
          typingIndicator.remove();
        }
      }
      function addChatMessage(text, type, sender) {
        const msgDiv = document.createElement('div');
        const isOutgoing = type === 'outgoing';
        
        msgDiv.className = `flex ${isOutgoing ? 'justify-end' : 'items-start'}`;
        
        const avatarHtml = !isOutgoing ? `
          <div class="bot-avatar mr-2 text-sm">
            ${sender.charAt(0)}
          </div>
        ` : '';
        
        msgDiv.innerHTML = `
          ${avatarHtml}
          <div class="flex flex-col ${isOutgoing ? '' : 'max-w-[85%]'}">
            ${!isOutgoing ? `<span class="text-xs text-gray-600 dark:text-gray-400 mb-1">${sender}</span>` : ''}
            <div class="chat-bubble ${isOutgoing ? 'message-out' : 'message-in'}">
              ${text}
            </div>
          </div>
        `;
        
        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
      function addSystemMessage(text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'text-center my-2';
        msgDiv.innerHTML = `<span class="px-2 py-1 bg-gray-200 dark:bg-gray-700 rounded-lg text-xs">${text}</span>`;
        
        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
      // Eventos para enviar mensagem
      sendButton.addEventListener('click', sendMessage);
      messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          sendMessage();
        }
      });
      // Limpar chat
      clearChatButton.addEventListener('click', function() {
        chatMessages.innerHTML = '';
        addSystemMessage('Conversa limpa');
      });
      // Adicionar mensagem inicial ao chat
      addSystemMessage('Bem-vindo ao simulador de chat! Envie uma mensagem para testar.');
      // Botão de teste de IA no Dashboard
      const testAIButton = document.getElementById('test-ai');
      testAIButton.addEventListener('click', function() {
        const tabs = document.querySelectorAll('.tab-link');
        // Encontrar e clicar na tab de simulação
        const targetTab = document.querySelector('.tab-link[data-tab="simulacao"]');
        if (targetTab) {
          targetTab.click();
          // Focar no input de mensagem
          setTimeout(() => {
            messageInput.focus();
            messageInput.value = "Olá, quem é você?";
          }, 100);
        }
      });
    });
  </script>
</body>
</html>
