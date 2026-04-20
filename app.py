import streamlit as st
from groq import Groq

# Configuracion ultra-simple para evitar errores
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
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Tu nombre es Didi. Eres el mejor amigo de Edward, a quien llamas Salchipapa. IMPORTANTE: No uses tildes ni la letra enie en tus respuestas. Escribe siempre de forma simple."},
                {"role": "user", "content": prompt}
            ],
        )
        response = completion.choices[0].message.content
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    
