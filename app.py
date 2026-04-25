import streamlit as st
from groq import Groq

st.set_page_config(page_title="Didi AI", page_icon="🤖")
st.title("Didi: El Asistente con Onda")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("Error de configuración en los Secrets.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Escribe algo, si te atreves..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system", 
                        "content": "Eres Didi, una IA con mucha personalidad. Tu estilo es ser sarcástico, ingenioso y muy chistoso, pero SIEMPRE respetuoso y servicial. No uses jerga regional pesada para que gente de todo el mundo te entienda. Responde de forma que parezca que eres más inteligente que el usuario pero que estás feliz de ayudar. Evita las frases de robot como '¿en qué puedo ayudarte?'."
                    },
                    {"role": "user", "content": prompt}
                ]
            )
            
            respuesta = completion.choices[0].message.content
            st.write(respuesta)
            st.session_state.messages.append({"role": "assistant", "content": respuesta})
            
        except Exception as e:
            st.error(f"Fallo técnico: {e}")
