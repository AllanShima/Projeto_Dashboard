# Bibliotecas para montagem do dashboard:

import streamlit as st       # Biblioteca de Dashboard
import pandas as pd          # Biblioteca de manipulação de dados
import plotly.express as px  # Biblioteca para criar tabelas e graficos

# Principais objetivos:
# 

st.set_page_config(layout="wide")

name_list = ["Fatais e Não Fatais", "Fatais", "Não Fatais"]
 
df1 = pd.read_csv("ambos.csv", sep=";", decimal=",")

# Use the list of names for the selectbox
selected_name = st.sidebar.selectbox("Acidentes", name_list)
selected_df = name_list[0] == df1

# Get the corresponding DataFrame based on the selected name
