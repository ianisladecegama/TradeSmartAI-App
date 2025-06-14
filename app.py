import streamlit as st

st.title("TradeAI – Asistente Educativo de Inversión")
st.write("Escribe tu pregunta sobre inversiones:")

pregunta = st.text_input("¿Qué quieres saber?")
if st.button("Enviar"):
    st.write("🔄 Analizando tu pregunta...")
    st.success("🧠 (Aquí iría la respuesta generada por la IA)")
