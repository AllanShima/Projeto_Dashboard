# Bibliotecas para montagem do dashboard:

import streamlit as st       # Biblioteca de Dashboard
import pandas as pd          # Biblioteca de manipulação de dados
import plotly.express as px  # Biblioteca para criar tabelas e graficos

# Principais objetivos:
# 

st.set_page_config(layout="wide")

list_of_names = ["ambos.csv", "fatais_marilia.csv", "nfatais_marilia.csv"]
text_list = ["Fatais e Não Fatais", "Fatais", "Não Fatais"]
 
df1 = pd.read_csv("ambos.csv", sep=";", decimal=",")
df2 = pd.read_csv("fatais_marilia.csv", sep=";", decimal=",")


# Use the list of names for the selectbox
selected_name = st.sidebar.selectbox("Acidentes", text_list)

# Get the corresponding DataFrame based on the selected name
