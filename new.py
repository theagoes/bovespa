import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import plotly.graph_objs  as go
import datetime as dt
from plotly.subplots import make_subplots

end = dt.datetime.now()
start = dt.datetime(2020,1,1,0,0)
stock = ['USIM5.SA']

df = pdr.get_data_yahoo(stock, start, end)

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

df['MA50'] = df['Close'].rolling(window=50, min_periods=0).mean()
df['MA200'] = df['Close'].rolling(window=200, min_periods=0).mean()

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.10, subplot_titles=('USIM5', 'Volume'),
                    row_width=[0.2, 0.7])
fig.add_trace(
    go.Candlestick(
        x = df.index,
        open = df['Open'],
        high = df['High'],
        low = df['Low'],
        close = df['Close'],
        name = 'Market Prices'), row=1, col=1
)
fig.add_trace(go.Scatter(x=df.index, y=df["MA50"], marker_color='grey',name="MA50"), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df["MA200"], marker_color='lightgrey',name="MA200"), row=1, col=1)
fig.add_trace(go.Bar(x=df.index, y=df['Volume'], marker_color='red', showlegend=False), row=2, col=1)

fig.update_layout(
    title='CBA historical price chart',
    xaxis_tickfont_size=12,
    yaxis=dict(
        title='Price ($/share)',
        titlefont_size=14,
        tickfont_size=12,
    ),
    autosize=False,
    width=900,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    paper_bgcolor='LightSteelBlue'
)
fig.update(layout_xaxis_rangeslider_visible=True)
fig.show()