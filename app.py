import streamlit as st
from groq import Groq

st.title("Didi: Activo")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if p := st.chat_input("Habla, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.write(p)
    
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    c = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": p}]
    )
    r = c.choices[0].message.content
    with st.chat_message("assistant"):
        st.write(r)
    st.session_state.messages.append({"role": "assistant", "content": r})
    
