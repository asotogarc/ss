import streamlit as st

# Ocultar el menú principal, botones superiores y otros elementos
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        header {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden !important;}
    </style>
""", unsafe_allow_html=True)

# Título de la aplicación
st.title("Mi Aplicación Streamlit")

# Agregar algún contenido de ejemplo
st.write("Bienvenido a mi aplicación Streamlit con el menú principal y botones superiores ocultos.")

# Agregar un widget de ejemplo
nombre = st.text_input("Ingresa tu nombre")
if nombre:
    st.write(f"Hola, {nombre}!")

# Agregar un botón de ejemplo
if st.button("Haz clic aquí"):
    st.write("¡Has hecho clic en el botón!")

# Agregar un gráfico de ejemplo
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])

st.line_chart(chart_data)
