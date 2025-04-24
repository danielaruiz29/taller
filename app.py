import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("datos.csv")
st.title("taller")


fig, ax = plt.subplots(1,4,figsize=(10,4))

#política monetaria
ax[0].hist(df["Tasa de política monetaria(Dato fin de año)"])

#PIB
ax[1].hist(df["Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)"])

#desempleo
ax[2].hist(df["Tasa de desempleo - total nacional(Dato fin de mes)"])

#inflación
ax[3].hist(df["Inflación total, anual(Dato fin de año)"])


st.pyplot(fig)