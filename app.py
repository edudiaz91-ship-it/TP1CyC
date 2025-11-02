import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app

st.title("Gráfico de Tipos de Ataque 2024")

# URL del CSV raw en GitHub

csv_url = "[https://raw.githubusercontent.com/edudiaz91-ship-it/TP1CyC/main/cybersecurity_attacks.csv](https://raw.githubusercontent.com/edudiaz91-ship-it/TP1CyC/main/cybersecurity_attacks.csv)"

# Leer CSV directamente desde GitHub

df = pd.read_csv(csv_url)

# Filtrar solo el año 2024 (asumiendo columna 'year')

df_2024 = df[df['year'] == 2024]

# Contar cantidad por tipo de ataque (asumiendo columna 'attack_type')

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

# Mostrar gráfico en Streamlit

st.pyplot(fig)
