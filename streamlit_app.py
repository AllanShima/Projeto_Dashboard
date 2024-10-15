# Bibliotecas para montagem do dashboard:

import streamlit as st       # Biblioteca de Dashboard
import pandas as pd          # Biblioteca de manipulação de dados
import plotly.express as px  # Biblioteca para criar tabelas e graficos

# Objetivos do dashboard:

# Faturamento por unidade;
# Tipo de produto mais vendido, contribuição por filial;
# Desempenho das formas de pagamento;
# Como estão as avaliações das filiais?
# = COM UMA VISÃO MENSAL

# Setando o layout da pagina
st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date" ] = pd.to_datetime(df["Date"]) # transformando o tipo de dado da info para data (originalmente está como object)
df = df.sort_values("Date") # Ordenando o conjunto de datas (organizando)

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
# df["Month"] pegando todos os meses em conjunto dos anos na coluna de datas
month = st.sidebar.selectbox("Mês", df["Month"].unique()) # Criando um sidebar com os meses
# df("Month").unique() Selecionando somente meses diferentes

df_filtered = df[df["Month"] == month]
df_filtered # Filtrando os meses

# CRIANDO OS GRAFICOS:

# dividindo a tela em 2
col1, col2 = st.columns(2)
# dividindo a tela em 3
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", title="Faturamento por dia") # criando o grafico
col1.plotly_chart(fig_date) # colocando o grafico de barras na coluna 1 do streamlit
