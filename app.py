import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

st.title("Gráfico de Tipos de Ataque 2024")

# URL del CSV raw en GitHub

csv_url = "https://raw.githubusercontent.com/edudiaz91-ship-it/TP1CyC/main/cybersecurity_attacks.csv"

# Descargar CSV usando requests

response = requests.get(csv_url)

if response.status_code != 200:
st.error("No se pudo descargar el CSV desde GitHub.")
else:
data = io.StringIO(response.text)
df = pd.read_csv(data)

```
# Filtrar solo el año 2024
if 'year' not in df.columns or 'attack_type' not in df.columns:
    st.error("El CSV debe tener las columnas 'year' y 'attack_type'.")
else:
    df_2024 = df[df['year'] == 2024]

    # Contar cantidad por tipo de ataque
    attack_counts = df_2024['attack_type'].value_counts()

    # Mostrar tabla resumida
    st.subheader("Cantidad de ataques por tipo")
    st.dataframe(attack_counts)

    # Crear gráfico de barras
    fig, ax = plt.subplots()
    attack_counts.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel("Tipo de Ataque")
    ax.set_ylabel("Cantidad")
    ax.set_title("Ataques por Tipo en 2024")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    st.pyplot(fig)
```
