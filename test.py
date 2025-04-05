# test_clima_streamlit.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Test de Clima Laboral", layout="centered")

# -------------------------------
# Preguntas organizadas por secciones
secciones = {
    "Liderazgo y Dirección": [
        "Los líderes promueven un ambiente abierto al diálogo.",
        "Las decisiones de los líderes son claras.",
        "Puedo confiar en quienes ocupan cargos de autoridad."
    ],
    "Valores Compartidos": [
        "Existe un conjunto claro de valores compartidos.",
        "Me identifico con la misión y visión.",
        "Se promueve la ética y el respeto."
    ],
    "Trabajo en Equipo": [
        "Hay colaboración entre grupos y áreas.",
        "Formo parte de un equipo cooperativo.",
        "Se valoran todas las opiniones."
    ],
    "Reconocimiento y Desarrollo": [
        "El esfuerzo individual es reconocido.",
        "Hay oportunidades de aprendizaje.",
        "Mis logros son valorados."
    ],
    "Bienestar y Ambiente Físico": [
        "El entorno físico es cómodo.",
        "Se promueve el bienestar emocional.",
        "Las condiciones favorecen la productividad."
    ],
    "Innovación y Cambio": [
        "La organización acepta nuevas ideas.",
        "Se promueve la innovación.",
        "Los cambios son bien gestionados."
    ]
}

# -------------------------------
# Título
st.title("🧭 Test de Clima Laboral")
st.markdown("Responde cada afirmación del 1 (Totalmente en desacuerdo) al 5 (Totalmente de acuerdo).")

# -------------------------------
# Recolección de respuestas
resultados = {}
for seccion, preguntas in secciones.items():
    st.subheader(f"📌 {seccion}")
    respuestas = []
    for i, pregunta in enumerate(preguntas, start=1):
        respuesta = st.slider(f"{pregunta}", 1, 5, 3, key=f"{seccion}_{i}")
        respuestas.append(respuesta)
    resultados[seccion] = respuestas

# -------------------------------
# Botón para mostrar resultados
if st.button("📊 Ver resultados del test"):
    promedios = {sec: sum(res)/len(res) for sec, res in resultados.items()}
    df = pd.Series(promedios)

    st.subheader("🔍 Resultados por dimensión:")
    for sec, val in promedios.items():
        st.write(f"**{sec}:** {round(val, 2)}")

    # Gráfico
    st.subheader("📈 Visualización gráfica:")
    fig, ax = plt.subplots()
    df.plot(kind='bar', ax=ax, color='skyblue')
    ax.axhline(3, color='red', linestyle='--', label="Nivel crítico (3)")
    ax.set_ylabel("Promedio (1-5)")
    ax.set_title("Promedios del Clima Laboral")
    ax.set_ylim(1, 5)
    ax.legend()
    st.pyplot(fig)
