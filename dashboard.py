# dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configura o tamanho da página
st.set_page_config(page_title="Dashboard", layout="wide")

# Abre o arquivo como read
# df = dataframe
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Ordena pela Data
df = df.sort_values("Date")

# Modifica a coluna para DateTime
df["Date"] = pd.to_datetime(df["Date"])

# Separar Ano e Mes para a pesquisa
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "/" + str(x.month))
month = st.sidebar.multiselect("Month", df["Month"].unique(), default=df["Month"].unique() )
payment = st.sidebar.multiselect("Payment", df["Payment"].unique(), default=df["Payment"].unique() )
city = st.sidebar.multiselect("City", df["City"].unique(), default=df["City"].unique() )


# Cria o filtro para o Month
df_filtered = df[ (df['Month'].isin(month)) & (df['Payment'].isin(payment)) & (df['City'].isin(city)) ]
df_filtered

# Montando os Gráficos
# Dividindo a tela
col1, col2 = st.columns(2)

# Criando Gráficos
graph_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento")
col1.plotly_chart(graph_date)
