# Bibliotecas para montagem do dashboard:

import streamlit as sl       #Biblioteca de Dashboard
import pandas as pd          #Biblioteca de manipulação de dados
import plotly.express as px  #Biblioteca para criar tabelas e tals

df = pd.read_csv("ambos.csv", sep=";", decimal=",")
df