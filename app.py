import streamlit as st
from groq import Groq

st.set_page_config(page_title="Didi Final")
st.title("Didi: Salchipapa")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error(f"Error de configuracion: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if p := st.chat_input("Dime algo, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.write(p)

    with st.chat_message("assistant"):
        try:
            # USAMOS EL MODELO NUEVO (Llama 3.1)
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": p}]
            )
            r_text = response.choices[0].message.content
            st.write(r_text)
            st.session_state.messages.append({"role": "assistant", "content": r_text})
        except Exception as e:
            st.error(f"Fallo tecnico: {e}")
            
