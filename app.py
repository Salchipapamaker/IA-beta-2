# -*- coding: utf-8 -*-
import streamlit as st
from groq import Groq

# Forzamos a que Streamlit no use caracteres raros en la interfaz
st.set_page_config(page_title="Didi AI")
st.title("Didi: Tu Amigo Digital")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Que pasa Salchipapa?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Tu nombre es Didi. Eres el mejor amigo de Edward, apodado Salchipapa. Habla siempre sin usar tildes ni enies."},
                    {"role": "user", "content": prompt}
                ],
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error("Didi esta descansando un momento, intenta de nuevo.")
