import yfinance
import plotly.graph_objects as go
amazon = yfinance.Ticker('AMZN')
print("AMAZON Business Summary")
print(amazon.info['longBusinessSummary'])