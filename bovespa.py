from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

tabela_empresas =  pd.read_excel("empresas.xlsx")

st.set_page_config(page_title="Cotações B3",page_icon=":bar_chart:")
st.sidebar.header("Filtros")

hide_st_style = """ 
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

empresa = st.sidebar.selectbox('Empresas', tabela_empresas)

st.title(":bar_chart:  Cotação  das Ações")
st.markdown("##")
cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo',  start="01/01/2021", end = "12/31/2022")
cotacao_red = cotacao.drop(cotacao.columns[[0,1,4]], axis = 1)

fig_bar = px.line(cotacao_red)
st.plotly_chart(fig_bar)
st.write(cotacao)
    