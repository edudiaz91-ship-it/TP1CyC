import streamlit as st
import pandas as pd
import altair as alt

st.title("Análisis de Ataques Cibernéticos 2024")

# URL del CSV raw en GitHub

csv_url = "[https://raw.githubusercontent.com/edudiaz91-ship-it/TP1CyC/main/cybersecurity_attacks.csv](https://raw.githubusercontent.com/edudiaz91-ship-it/TP1CyC/main/cybersecurity_attacks.csv)"

# Leer CSV directamente desde GitHub

df = pd.read_csv(csv_url)

# Verificar que existan las columnas necesarias

if 'year' not in df.columns or 'attack_type' not in df.columns:
st.error("El CSV debe tener las columnas 'year' y 'attack_type'.")
else:
# Filtrar solo el año 2024
df_2024 = df[df['year'] == 2024]

```
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
chart = alt.Chart(attack_counts).mark_bar(color='skyblue').encode(
    x=alt.X('attack_type', sort='-y', title='Tipo de Ataque'),
    y=alt.Y('count', title='Cantidad'),
    tooltip=['attack_type', 'count']
).properties(
    title='Ataques por Tipo en 2024'
)

st.altair_chart(chart, use_container_width=True)
```
