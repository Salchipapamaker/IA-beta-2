import streamlit as st
from groq import Groq

# Configuración de la página
st.set_page_config(page_title="Didi AI", page_icon="🤖")
st.title("🤖 Didi: Mi Compañero Digital")

# Aquí va tu llave (API KEY)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Qué pasa, Gerson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # USAMOS EL MODELO NUEVO: llama-3.3-70b-versatile
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Eres Didi, una IA con mucha calle, amigable, hablas de tú a tú y eres el mejor amigo de Gerson."},
                {"role": "user", "content": prompt}
            ],
        )
        response = completion.choices[0].message.content
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
  
