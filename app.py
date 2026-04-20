import streamlit as st
from groq import Groq

# Configuracion de la pagina (sin tildes para evitar errores)
st.set_page_config(page_title="Didi AI", page_icon="🤖")
st.title("🤖 Didi: Mi Companero Digital")

# Aqui va tu llave (API KEY)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Dime algo, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Usamos el modelo mas potente y nuevo
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Eres Didi, una IA con mucha calle, amigable y hablas de tu a tu. Tu creador y mejor amigo es Edward, pero siempre le dices Salchipapa de carino. No uses tildes ni enies en tus respuestas para evitar errores de sistema por ahora."},
                {"role": "user", "content": prompt}
            ],
        )
        response = completion.choices[0].message.content
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

