import streamlit as st
from groq import Groq

st.title("Didi: Tu Amigo Digital")

# Intentamos conectar con la llave
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Falta la llave en Secrets")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if p := st.chat_input("Que pasa Salchipapa?"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.write(p)

    with st.chat_message("assistant"):
        try:
            # Usamos el modelo mas rapido y sencillo
            c = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "system", "content": "Eres Didi, amigo de Edward (Salchipapa). No uses tildes."},
                          {"role": "user", "content": p}]
            )
            r = c.choices[0].message.content
            st.write(r)
            st.session_state.messages.append({"role": "assistant", "content": r})
        except:
            st.error("Error de conexion. Revisa tu llave de Groq.")
            
