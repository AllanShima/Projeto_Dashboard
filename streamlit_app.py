# Bibliotecas para montagem do dashboard:
import streamlit as st       # Biblioteca de Dashboard
import pandas as pd          # Biblioteca de manipulação de dados
import plotly.express as px  # Biblioteca para criar tabelas e graficos

# Principais objetivos:
# criar um mapa de calor

st.set_page_config(layout="wide", page_title="Dashboard das Áreas de Risco", page_icon="🚗")

lista_de_nomes = ["Fatais e Não Fatais", "Fatais", "Não Fatais"]
 
df1 = pd.read_csv("ambos.csv", sep=";", decimal=",")
df2 = pd.read_csv("fatais_marilia.csv", sep=";", decimal=",")
df3 = pd.read_csv("nfatais_marilia.csv", sep=";", decimal=",")

# Remover linhas com valores NaN nas colunas de latitude e longitude
df1 = df1.dropna(subset=['latitude', 'longitude'])
df2 = df2.dropna(subset=['latitude', 'longitude'])
df3 = df3.dropna(subset=['latitude', 'longitude'])

df_dict = {
    "Fatais e Não Fatais": df1,
    "Fatais": df2,
    "Não Fatais": df3
}

# Utilizar a lista de dataframes para os selectboxes
nomes_selecionados = st.sidebar.selectbox("Acidentes", lista_de_nomes)

df_selecionado = df_dict[nomes_selecionados]

col1, col2 = st.columns(2)

with col1:
    subcol1, subcol2 = st.columns(2)

    with subcol1:
        df_selecionado["Ano/Mes do Sinistro"] = pd.to_datetime(df_selecionado["Ano/Mes do Sinistro"])
        df_selecionado["Ano do Sinistro"] = df_selecionado["Ano/Mes do Sinistro"].apply(lambda x: str(x.year))

        col_anos = df_selecionado["Ano do Sinistro"].sort_values(ascending=False).unique()
        col_count_anos = df_selecionado["Ano do Sinistro"].value_counts()

        df_anos_filtrado = pd.DataFrame({
            'Anos': col_anos,
            'Total de acidentes': col_count_anos
        })

        fig_anos = px.line(df_anos_filtrado, x="Anos", y="Total de acidentes", title='Total por Ano')

        st.write(fig_anos)

        # Total de diferentes tipos de veículos envolvidos

        col_veiculos = ["Automóvel", "Bicicleta", "Motocicleta", "Caminhão", "Ônibus", "Outros veículos", "Pedestres"]
        col_quant_veiculos = [df_selecionado["Automovel envolvido"].sum(), df_selecionado["Bicicleta envolvida"].sum(), df_selecionado["Motocicleta envolvida"].sum(), df_selecionado["Caminhao envolvido"].sum(), df_selecionado["Onibus envolvido"].sum(), df_selecionado["Outros veiculos envolvidos"].sum(), df_selecionado["Pedestre envolvido"].sum()]

        df_veiculos_filtrados = pd.DataFrame({
            'Veículos': col_veiculos,
            'Total de veículos': col_quant_veiculos
        })

        fig_veiculos = px.pie(df_veiculos_filtrados, names='Veículos', values='Total de veículos', title="Total por Tipo de Veículo")

        st.write(fig_veiculos)
        
    with subcol2:

        col_meses = pd.to_datetime(df1["Ano/Mes do Sinistro"])
        col_meses = df_selecionado["Mes do Sinistro"].sort_values(ascending=True).unique()
        col_count_meses = df_selecionado["Mes do Sinistro"].value_counts()

        df1_meses_filtrado = pd.DataFrame({
            'Meses': col_meses,
            'Total': col_count_meses
        })

        fig_prod = px.bar(df1_meses_filtrado, x="Meses", y="Total", title="Total por Mês", orientation="v")
        st.write(fig_prod)

        # Total por tipo de acidente

        col_acidentes = ['Atropelamento', 'Capotamento', 'Choque', 'Colisao frontal', 'Colisao lateral', 'Colisao transversal', 'Colisao traseira', 'Outras colisoes', 'Engavetamento', 'Tombamento']
        col_total_acidentes = [df_selecionado['Atropelamento'].sum(), df_selecionado['Capotamento'].sum(), df_selecionado['Choque'].sum(), df_selecionado['Colisao frontal'].sum(), df_selecionado['Colisao lateral'].sum(), df_selecionado['Colisao transversal'].sum(), df_selecionado['Colisao traseira'].sum(), df_selecionado['Outras colisoes'].sum(), df_selecionado['Engavetamento'].sum(), df_selecionado['Tombamento'].sum()]

        df_total_acidentes = pd.DataFrame({
            'Acidentes': col_acidentes,
            'Total': col_total_acidentes
        })

        fig_tipo_acidente = px.bar(df_total_acidentes, x='Acidentes', y='Total', title='Total por Tipo de Acidente', orientation='v')

        st.write(fig_tipo_acidente)
# Mapa de calor da área de risco
with col2:
    st.header("Áreas de Risco em Marília")
    fig_map = px.density_mapbox(
        df_selecionado,
        "latitude",
        "longitude", 
        None, 
        "Logradouro", 
        radius=8, 
        zoom=9, 
        mapbox_style='open-street-map', 
        height=800, 
        width=400,
        color_continuous_scale="thermal",
        opacity=0.8
    )
    st.plotly_chart(fig_map, use_container_width=True)