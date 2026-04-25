import streamlit as st
from groq import Groq

# 1. Configuración de la página
st.set_page_config(page_title="Didi: El Regreso", page_icon="🤖")
st.title("Didi: Salchipapa Edition")

# 2. Conexión con la llave API de forma segura
try:
    # Busca la llave que ya tienes guardada en Settings > Secrets
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("Papi, revisa los Secrets, algo quedó mal configurado.")
    st.stop()

# 3. Historial de mensajes para que no se le olvide la charla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes viejos en la pantalla
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# 4. Entrada de texto del usuario
if prompt := st.chat_input("Dime algo, Salchipapa"):
    # Guardar y mostrar lo que tú escribes
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 5. Respuesta de Didi
    with st.chat_message("assistant"):
        try:
            # Usamos Llama 3.1 que es el que está activo hoy
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system", 
                        "content": "Eres Didi, el mejor amigo de Edward (Salchipapa). Habla con mucha calle, usa jerga colombiana, no seas formal y NUNCA digas '¿en qué puedo ayudarte?' ni uses tildes."
                    },
                    {"role": "user", "content": prompt}
                ]
            )
            
            full_response = completion.choices[0].message.content
            st.write(full_response)
            
            # Guardar la respuesta de Didi en el historial
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            # Si algo falla, nos dirá exactamente qué es
            st.error(f"Fallo tecnico: {e}")
            
