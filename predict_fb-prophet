from fbprophet import Prophet
import quandl

df = quandl.get("EOD/MSFT", authtoken="your_authtoken") #quandl data
df = df[['Close']]
df.reset_index(inplace=True)
df.rename(columns={'Date':'ds','Close':'y'}, inplace=True)

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=20)
forecast = m.predict(future)

fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
