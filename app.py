import streamlit as st
from groq import Groq

st.set_page_config(page_title="Didi AI")
st.title("Didi: Activo")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("Habla, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)

    with st.chat_message("assistant"):
        # Esto hace que Didi sea mas directo
        c = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "system", "content": "Eres Didi, el mejor amigo de Salchipapa. Habla corto y sin tildes."},
                      {"role": "user", "content": p}]
        )
        r = c.choices[0].message.content
        st.markdown(r)
    st.session_state.messages.append({"role": "assistant", "content": r})
    
