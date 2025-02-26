import streamlit as st
import time

def main():
    # Configuração da página
    st.set_page_config(
        page_title="whatasppIA",
        page_icon="💬",
        layout="wide",
    )

    # Título da aplicação
    st.title("💬 whatasppIA")

    # Abas para navegação
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Dashboard", "Configuração", "Simulação", "Instruções"]
    )

    # Aba 1: Dashboard
    with tab1:
        st.header("Dashboard")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Status do Serviço")
            status = st.selectbox("Status", ["Offline", "Conectando...", "Online"])
            if status == "Online":
                st.success("Serviço online e funcionando!")
            elif status == "Conectando...":
                st.warning("Conectando ao WhatsApp...")
            else:
                st.error("Serviço offline.")

        with col2:
            st.subheader("Estatísticas")
            st.metric("Mensagens Recebidas", 0)
            st.metric("Respostas Automáticas", 0)
            st.metric("Grupos Ativos", 0)
            st.metric("Contatos Ativos", 0)

        with col3:
            st.subheader("Modelo IA")
            modelo = st.selectbox(
                "Modelo Selecionado",
                ["Claude-3.7-Sonnet", "GPT-4o", "Modelo Local"],
            )
            st.text_area("Template de Prompt", value="Você é um assistente útil...")
            if st.button("Testar Modelo"):
                st.info("Testando o modelo...")

    # Aba 2: Configuração
    with tab2:
        st.header("Configuração")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Configuração Geral")
            metodo_instalacao = st.selectbox(
                "Método de Instalação",
                ["Local (WhatsApp Web + Automação)", "API WhatsApp Business"],
            )
            auto_inicio = st.checkbox("Iniciar automaticamente com o sistema")
            tempo_sessao = st.number_input(
                "Tempo Limite de Sessão (minutos)", min_value=1, max_value=1440, value=60
            )
            atraso_mensagem = st.number_input(
                "Atraso entre Mensagens (segundos)", min_value=0, max_value=60, value=2
            )
            som_notificacao = st.checkbox("Ativar sons de notificação", value=True)

        with col2:
            st.subheader("Configuração de Resposta")
            modo_resposta = st.selectbox(
                "Modo de Resposta",
                [
                    "Responder a todas as mensagens",
                    "Responder apenas quando mencionado",
                    "Responder baseado em palavras-chave",
                ],
            )
            palavras_gatilho = st.text_area(
                "Palavras/Frases Gatilho (uma por linha)",
                value="bot\nassistente\najuda\n/start",
            )
            usuarios_ignorados = st.text_area(
                "Ignorar Usuários (um por linha)", value="+5511987654321"
            )
            template_resposta = st.text_area(
                "Template de Resposta", value="[Nome], [Resposta IA]"
            )

        if st.button("Salvar Configurações"):
            st.success("Configurações salvas com sucesso!")

    # Aba 3: Simulação
    with tab3:
        st.header("Simulação de Chat")
        modo_chat = st.radio("Tipo de Chat", ["Chat Individual", "Chat em Grupo"])
        nome_usuario = st.text_input("Seu Nome", value="Você")
        nome_bot = st.text_input("Nome do Bot", value="Assistente")

        # Área de mensagens
        if "mensagens" not in st.session_state:
            st.session_state.mensagens = []

        for mensagem in st.session_state.mensagens:
            st.markdown(
                f"""
                <div class="chat-bubble {'message-out' if mensagem['tipo'] == 'out' else 'message-in'}">
                    <strong>{mensagem['remetente']}:</strong> {mensagem['texto']}
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Input de mensagem
        mensagem = st.text_input("Digite uma mensagem...", key="input_mensagem")
        if st.button("Enviar"):
            if mensagem.strip():
                # Adicionar mensagem do usuário
                st.session_state.mensagens.append(
                    {"remetente": nome_usuario, "texto": mensagem, "tipo": "out"}
                )
                # Simular resposta do bot
                with st.spinner("Digitando..."):
                    time.sleep(1)
                    resposta = responder_mensagem(mensagem, modo_chat == "Chat em Grupo", nome_bot)
                    st.session_state.mensagens.append(
                        {"remetente": nome_bot, "texto": resposta, "tipo": "in"}
                    )
                st.experimental_rerun()

    # Aba 4: Instruções
    with tab4:
        st.header("Instruções")
        st.markdown(
            """
            ### Como Configurar seu Bot WhatsApp com IA Local
            1. **Instale o Node.js** no seu computador.
            2. **Clone o repositório** do bot e instale as dependências.
            3. **Configure o modelo de IA** no arquivo `config.json`.
            4. **Execute o bot** usando o comando `node index.js`.
            5. **Escaneie o QR Code** no WhatsApp Web para conectar.
            """
        )
        st.warning(
            "⚠️ Aviso: O uso de automação no WhatsApp pode violar os Termos de Serviço. Use por sua conta e risco."
        )

# Função para simular resposta da IA
def responder_mensagem(mensagem, modo_grupo, nome_bot):
    if "olá" in mensagem.lower():
        return f"Olá! Eu sou {nome_bot}. Como posso ajudar?"
    elif "ajuda" in mensagem.lower():
        return "Claro! Estou aqui para ajudar."
    else:
        return "Desculpe, não entendi. Pode reformular?"
