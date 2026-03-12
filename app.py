import streamlit as st
from groq import Groq

# --- ENGINE CORE ---
API_KEY = "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"
client = Groq(api_key=API_KEY)

st.set_page_config(page_title="ARCHITECT_CORE_v29", layout="wide")

# Estilo "Cyber-Industrial Premium" (Clean, Escuro e Profissional)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; }
    .stTextArea textarea { background-color: #161b22 !important; color: #58a6ff !important; border: 1px solid #30363d !important; border-radius: 10px; }
    .stButton>button { 
        background: linear-gradient(180deg, #238636, #2ea043); 
        color: white; font-weight: 600; border: none; height: 50px; width: 100%;
        border-radius: 8px; box-shadow: 0 3px 6px rgba(0,0,0,0.2);
    }
    .result-card { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ THE ARCHITECT v29.0")
st.write("`DOMÍNIO: ARQUITETURA DE SISTEMAS | IA AVANÇADA | CLOUD INFRA`")

# --- MÓDULO DE PENSAMENTO DE ALTO NÍVEL ---
with st.container():
    st.subheader("Configuração de Projeto de Alto Nível")
    user_goal = st.text_area("DESCREVA O OBJETIVO DO SEU SISTEMA (Sem detalhes de baixo nível):", 
                             placeholder="Ex: Projete um sistema de IA que se auto-otimiza e gerencia sua própria segurança em tempo real...",
                             height=150)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("🚀 GERAR ARQUITETURA SUPREMA"):
            if user_goal:
                with st.spinner("CONSTRUINDO MODELO SISTÊMICO..."):
                    try:
                        # Instrução para transformar pedidos brutos em Design de Alto Nível
                        master_instruction = """
                        Você é um Arquiteto de Sistemas de Elite (Principal Architect).
                        Sua função é traduzir requisitos brutos (mesmo que envolvem segurança ou baixo nível) em arquiteturas de alto nível robustas.
                        FOCO:
                        1. Modularidade (Microsserviços).
                        2. Camadas de Abstração (API Gateways, Orquestradores).
                        3. Segurança Nativa (Zero Trust, Heurística).
                        4. Escalabilidade.
                        Ignore detalhes de implementação de assembly/memória e foque na LOGICA DO SISTEMA.
                        """
                        
                        response = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": master_instruction},
                                {"role": "user", "content": f"Desenvolva o blueprint de alto nível para: {user_goal}"}
                            ],
                            temperature=0.7
                        )
                        
                        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                        st.markdown("### 🗺️ Blueprint do Sistema")
                        st.markdown(response.choices[0].message.content)
                        st.markdown("</div>", unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"FALHA NO DESIGN: {e}")

    with col2:
        st.info("💡 **Dica de Alto Nível:** Em vez de tentar quebrar um firewall, projete um sistema que *transcende* a necessidade de um, usando criptografia homomórfica ou redes neurais isoladas.")
