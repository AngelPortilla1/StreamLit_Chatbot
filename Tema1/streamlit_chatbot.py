from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

import streamlit as st
load_dotenv()

#configurar la pagina de la aplicacion

st.set_page_config(page_title = "Chatbot Básico", page_icon = "🤖")
st.title("Chatbot Básico con LangChain y Streamlit")
st.markdown("Este es un chatbot básico creado con LangChain y Streamlit.")


chat_model = ChatOpenAI(model="deepseek-chat",
    base_url="https://api.deepseek.com",
    temperature=0.7,)


#Inicializar el historial de mensajes

if "mensajes" not in st.session_state:
    st.session_state.mensajes = [SystemMessage(content="Eres un asistente útil.")]