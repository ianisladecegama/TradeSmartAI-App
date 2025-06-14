import streamlit as st
import openai

st.set_page_config(page_title="TradeSmartAI", page_icon="📈")

st.title("📊 TradeSmartAI – Asistente Educativo de Inversión")
st.markdown("""
Escribe tu pregunta sobre inversiones:
- ¿Qué acción es óptima comprar hoy para venderla dentro de 1 mes y sacar el máximo beneficio?
- ¿Cuándo vendo mis acciones de Tesla?
""")

# Input del usuario
user_question = st.text_area("Tu pregunta:")

if st.button("Enviar pregunta"):
    if user_question.strip() == "":
        st.warning("Por favor, escribe una pregunta.")
    else:
        with st.spinner("Analizando con IA..."):
            try:
                openai.api_key = st.secrets["OPENAI_API_KEY"]
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un asistente financiero educativo que ayuda a jóvenes a entender el mercado de acciones. No das consejos financieros reales, solo explicaciones educativas."},
                        {"role": "user", "content": user_question}
                    ]
                )
                answer = response.choices[0].message.content
                st.success("Respuesta de TradeAI:")
                st.markdown(answer)
            except Exception as e:
                st.error("Error al contactar con OpenAI.")
                st.text(str(e))
