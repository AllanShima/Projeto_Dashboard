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

df["Date"] = pd.to_datetime(df["Date"]) # transformando o tipo de dado da info para data (originalmente está como object)
df = df.sort_values("Date") # Ordenando o conjunto de datas (organizando)

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
# df["Month"] pegando todos os meses em conjunto dos anos na coluna de datas

month = st.sidebar.selectbox("Mês", df["Month"].unique()) # Criando um sidebar com os meses
# df("Month").unique() Selecionando somente meses diferentes

df_filtered = df[df["Month"] == month]
#df_filtered Filtrando os meses

# CRIANDO OS GRAFICOS:

# dividindo a tela em 2 (primeira linha)
col1, col2 = st.columns(2)
# dividindo a tela em 3 (segunda linha)
col3, col4, col5 = st.columns(3)

# GRAFICO 1 da linha 1
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia") # criando o grafico
col1.plotly_chart(fig_date, use_container_width=True) # colocando o grafico de barras na coluna 1 do streamlit

# GRAFICO 2
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h") # criando o grafico
col2.plotly_chart(fig_prod, use_container_width=True)

# GRAFICO 1 da linha 2
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial") # criando o grafico
col3.plotly_chart(fig_city, use_container_width=True) 

# GRAFICO 2 da linha 2
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento") # criando o grafico
col4.plotly_chart(fig_kind, use_container_width=True) 

# GRAFICO 3 da linha 2
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_total, x="City", y="Rating", title="Avaliação") # criando o grafico
col5.plotly_chart(fig_rating, use_container_width=True) 