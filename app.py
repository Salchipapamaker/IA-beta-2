import streamlit as st
from groq import Groq

# Titulo de la app
st.title("Didi: El Regreso")

# Conexion con la llave
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Entrada de texto
if p := st.chat_input("Habla, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.write(p)
    
    try:
        # Estructura limpia para evitar el BadRequestError
        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "Eres Didi, el mejor amigo de Edward (Salchipapa). Habla con mucha calle pero sin tildes."},
                {"role": "user", "content": p}
            ]
        )
        
        respuesta = chat_completion.choices[0].message.content
        
        with st.chat_message("assistant"):
            st.write(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})
        
    except Exception as e:
        st.error("Hubo un pequeno cruce de cables, intenta de nuevo.")
        
