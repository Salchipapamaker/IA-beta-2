import streamlit as st
from groq import Groq

# 1. Configuracion de la pagina
st.set_page_config(page_title="Didi AI", page_icon="🤖")
st.title("Didi: El Regreso")

# 2. Conexion con la llave de forma segura
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Falta la llave en los Secrets de Streamlit")
    st.stop()

# 3. Historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 4. Chat
if prompt := st.chat_input("Habla, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Usamos el modelo Llama 3 que es super rapido
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "Eres Didi, el mejor amigo de Edward (Salchipapa). Habla corto y sin tildes."},
                    {"role": "user", "content": prompt}
                ]
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error("Didi se distrajo, intenta preguntar de nuevo.")
            
