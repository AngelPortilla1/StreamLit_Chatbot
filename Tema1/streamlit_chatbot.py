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
    st.session_state.mensajes = []


#Mostrar mensajes previos en la interfaz
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        #no muestro el mensaje por pantalla
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"


    with st.chat_message(role):
        st.markdown(msg.content)


#cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje")

if pregunta:
    #mostrar inmediatamente el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)

    #Almacenamos el mensaje en la memoria streamlit
    st.session_state.mensajes.append(HumanMessage(content=pregunta))
