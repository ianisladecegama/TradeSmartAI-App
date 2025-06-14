import os
import streamlit as st
from openai import OpenAI

st.title("TradeAI - Asistente de inversión")

# Define la API key en variable de entorno para OpenAI
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Crea el cliente OpenAI
client = OpenAI()

# Entrada de usuario
pregunta = st.text_input("¿Con qué puedo ayudarte?")

if st.button("Consultar"):
    if pregunta:
        try:
            # Llamada a la API usando la nueva interfaz
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente que ayuda a elegir acciones."},
                    {"role": "user", "content": pregunta}
                ]
            )
            # Mostrar resultado
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error al contactar con OpenAI: {e}")
    else:
        st.warning("Por favor, escribe una pregunta.")
