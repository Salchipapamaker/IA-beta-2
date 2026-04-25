import streamlit as st
from groq import Groq

st.set_page_config(page_title="Didi AI")
st.title("Didi: holaaa")

# Cargamos la llave
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Revisa los Secrets en Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if p := st.chat_input("Habla, Salchipapa"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.write(p)

    with st.chat_message("assistant"):
        try:
            # Si falla uno, intenta con el otro
            modelos = ["mixtral-8x7b-32768", "llama3-8b-8192"]
            for modelo in modelos:
                try:
                    c = client.chat.completions.create(
                        model=modelo,
                        messages=[{"role": "system", "content": "Eres Didi, amigo de Edward (Salchipapa). Habla sin tildes."},
                                  {"role": "user", "content": p}]
                    )
                    r = c.choices[0].message.content
                    st.write(r)
                    st.session_state.messages.append({"role": "assistant", "content": r})
                    break 
                except:
                    continue
        except:
            st.error("Didi sigue con los cables cruzados. Revisa tu llave en Groq.")
            
