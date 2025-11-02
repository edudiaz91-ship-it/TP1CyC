import streamlit as st
import pandas as pd
import altair as alt
import requests
import io

st.title("Análisis de Ataques Cibernéticos 2024")

# Pone aquí la URL que tengas en GitHub (puede ser la que termina en /blob/... o la raw)
csv_url = "https://github.com/edudiaz91-ship-it/TP1CyC/blob/main/cybersecurity_attacks.csv"

def to_raw_github(url: str) -> str:
    """
    Convierte una URL de GitHub tipo 'github.com/.../blob/main/file.csv'
    a la URL raw 'raw.githubusercontent.com/.../main/file.csv'.
    Si la URL ya es raw, la devuelve tal cual.
    """
    if "raw.githubusercontent.com" in url:
        return url
    if "github.com" in url:
        # Ejemplo:
        # https://github.com/user/repo/blob/main/path/file.csv
        # -> https://raw.githubusercontent.com/user/repo/main/path/file.csv
        return url.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")
    return url

raw_url = to_raw_github(csv_url)

# Intento directo con pandas (funciona si la URL es accesible)
df = None
try:
    df = pd.read_csv(raw_url)
except Exception:
    # Fallback: descargar con requests y leer desde buffer
    try:
        resp = requests.get(raw_url, timeout=15)
        resp.raise_for_status()
        data = io.StringIO(resp.text)
        df = pd.read_csv(data)
    except Exception as e:
        st.error(f"No se pudo leer el CSV desde GitHub: {e}")
        st.stop()

# Verificar columnas
if 'year' not in df.columns or 'attack_type' not in df.columns:
    st.error("El CSV debe tener las columnas 'year' y 'attack_type'.")
else:
    # Filtrar solo el año 2024
    df_2024 = df[df['year'] == 2024]

    # Contar cantidad por tipo de ataque
    attack_counts = df_2024['attack_type'].value_counts().reset_index()
    attack_counts.columns = ['attack_type', 'count']

    # Mostrar tipo de ataque más frecuente
    if not attack_counts.empty:
        top_attack = attack_counts.iloc[0]['attack_type']
        st.header(f"Tipo de ataque más frecuente en 2024: {top_attack}")

    # Mostrar tabla resumida
    st.subheader("Cantidad de ataques por tipo")
    st.dataframe(attack_counts)

    # Crear gráfico de barras con Altair
    chart = alt.Chart(attack_counts).mark_bar().encode(
        x=alt.X('attack_type', sort='-y', title='Tipo de Ataque'),
        y=alt.Y('count', title='Cantidad'),
        tooltip=['attack_type', 'count']
    ).properties(
        title='Ataques por Tipo en 2024'
    )

    st.altair_chart(chart, use_container_width=True)
