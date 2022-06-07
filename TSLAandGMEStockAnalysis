!pip install yfinance==0.1.67
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
#!pip install plotly==5.3.1

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# takes a dataframe with stock data (dataframe must contain Date and Close columns),
# a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

# Question 1 Use yfinance to Extract Stock Data TSLA
tsla = yf.Ticker("TSLA")
tslaDF = pd.DataFrame(tsla.history(period="max"))
tslaDF.reset_index(inplace=True)
print('\n' + 'Question 1' + '\n')
print(tslaDF.head(5))

# Question 2 Use Webscraping to Extract Tesla Revenue Data TSLA
tslaUrl = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tslaData = requests.get(tslaUrl).text
tslaSoup = BeautifulSoup(tslaData, 'html5lib')
tslaRev = pd.DataFrame(columns=["Date", "Revenue"])
for row in tslaSoup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    rev = col[1].text
    tslaRev = tslaRev.append({"Date":date, "Revenue":rev,}, ignore_index=True)
tslaRev["Revenue"] = tslaRev['Revenue'].str.replace(',|\$',"")
tslaRev.dropna(inplace=True)
tslaRev = tslaRev[tslaRev['Revenue'] != ""]
print('\n' + 'Question 2' + '\n')
print(tslaRev.tail(5))

# Question 3 Use yfinance to Extract Stock Data GME
gme = yf.Ticker("GME")
gmeDF = pd.DataFrame(gme.history(period="max"))
gmeDF.reset_index(inplace=True)
print('\n' + 'Question 3' + '\n')
print(gmeDF.head(5))

# Question 4 Use Webscraping to Extract Tesla Revenue Data GME
gmeUrl = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
gmeData = requests.get(gmeUrl).text
gmeSoup = BeautifulSoup(gmeData, 'html5lib')
gmeRev = pd.DataFrame(columns=["Date", "Revenue"])
for row in gmeSoup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    rev = col[1].text
    gmeRev = gmeRev.append({"Date":date, "Revenue":rev,}, ignore_index=True)
gmeRev["Revenue"] = gmeRev['Revenue'].str.replace(',|\$',"")
gmeRev.dropna(inplace=True)
gmeRev = gmeRev[gmeRev['Revenue'] != ""]
print('\n' + 'Question 4' + '\n')
print(tslaRev.tail(5))

# Question 5 Plot TSLA Stock Graph

print('\n' + 'Question 5' + '\n')
make_graph(tslaDF, tslaRev, 'Tesla')

# Question 6 Plot GME Stock Graph

print('\n' + 'Question 6' + '\n')
make_graph(gmeDF, gmeRev, 'GameStop')
