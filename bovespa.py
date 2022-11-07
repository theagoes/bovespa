from pandas_datareader import data as web
import pandas as pd
import plotly.express as px
import streamlit as st
import openpyxl
from style import hide_st_style

tabela_empresas =  pd.read_excel("Empresas.xlsx")

st.set_page_config(page_title="Cotações B3 Web",page_icon=":bar_chart:")
st.sidebar.header("Filtros")
st.markdown(hide_st_style, unsafe_allow_html=True)

empresa = st.sidebar.selectbox('Empresas', tabela_empresas)

st.title(":bar_chart:  Cotação  das Ações")
st.markdown("##")
cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo',  start="01/01/2021", end = "12/31/2022")
cotacao_red = cotacao.drop(cotacao.columns[[0,1,4]], axis = 1)

fig_bar = px.line(cotacao_red)
st.plotly_chart(fig_bar)
st.write(cotacao)
    
