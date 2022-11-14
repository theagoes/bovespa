import datetime
import pandas_datareader as pdr
import pandas as pd
import plotly.express as px
import plotly.graph_objs  as go
import streamlit as st
import cufflinks as cf
import yfinance as yf
from style import hide_st_style

TICKERS = ['USIM3','USIM5','VALE3','PETR3','PETR4','BBDC4']

st.set_page_config(page_title="Cotações B3 Web",page_icon=":bar_chart:")
st.sidebar.header("Filtros")
st.markdown(hide_st_style, unsafe_allow_html=True)

ticker = st.sidebar.selectbox('Empresas', sorted(TICKERS), index=0)
start_date = st.sidebar.date_input('Start date', datetime.datetime(2022, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.datetime.now().date())

st.title(":bar_chart:  Cotação  das Ações")
st.markdown("##")

df_ticker = pdr.DataReader(f"{ticker}.SA", 'yahoo', start_date, end_date)

st.header(f'{ticker} Stock Price')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df_ticker)
    
qf = cf.QuantFig(df_ticker, legend='top', name=ticker)
qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
qf.add_volume()
figs = qf.iplot(asFigure=True, dimensions=(800, 600))
st.plotly_chart(figs)

layout = go.Layout(
		title= "Teste",
	    paper_bgcolor='rgb(255,255,255)',
	    plot_bgcolor='rgb(229,229,229)',
        legend_title_text = "Test1",
	
	    xaxis=dict(
	        gridcolor='rgb(255,255,255)',
	        showgrid=True,
	        showline=False,
	        showticklabels=True,
	        tickcolor='rgb(127,127,127)',
	        ticks='outside',
	        zeroline=False,
	        title="Teste"
	    ),
        yaxis=dict(
	        gridcolor='rgb(255,255,255)',
	        # range = rangeY,
	        showgrid=True,
	        showline=False,
	        showticklabels=True,
	        tickcolor='rgb(127,127,127)',
	        ticks='outside',
	        zeroline=False,
	        title="Teste2"
	    ),
)
fig = go.Figure()
fig.add_trace(
    go.Candlestick(
        x = df_ticker.index,
        open = df_ticker['Open'],
        high = df_ticker['High'],
        low = df_ticker['Low'],
        close = df_ticker['Close'],
        name = 'Market Prices')
)
fig.update_layout(layout)
fig.update_xaxes(title_text="Período")
fig.update_yaxes(title_text="Volume")
st.plotly_chart(fig)
st.markdown("##")
st.write(df_ticker)


tc = 'AAPL'
dt = yf.Ticker(tc)
tcdt = dt.history(period='1d',start='2021-11-11', end='2022-11-11')

st.line_chart(tcdt.Close)
st.line_chart(tcdt.Volume)
st.write(tcdt)
    
