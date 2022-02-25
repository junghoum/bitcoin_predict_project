import pyupbit
from fbprophet import Prophet


def coin_value(coinname, interval_time, periods_time):
  #BTC 최근 interval시간의 데이터 불러옴
  df1 = pyupbit.get_ohlcv(coinname, interval=interval_time)
  df1
  #시간(ds)와 종가(y)값만 남김
  df1 = df1.reset_index()
  df1['ds'] = df1['index']
  df1['y'] = df1['close']
  data = df1[['ds','y']]
  data

  #학습
  model = Prophet()
  model.fit(data)
  #periods시간 미래 예측
  future = model.make_future_dataframe(periods=periods_time, freq='H')
  forecast = model.predict(future)
  # #그래프1
  # fig1 = model.plot(forecast)
  # #그래프2
  # fig2 = model.plot_components(forecast)

# def coinasd():

#매수 시점의 가격
  nowValue = pyupbit.get_current_price(coinname)
  nowValue

  
#종가의 가격을 구함

#현재 시간이 자정 이전
  closeDf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]

#현재 시간이 자정 이후
  if len(closeDf) == 0:
    closeDf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]

#당일 종가
  closeValue = closeDf['yhat'].values[0]
  closeValue


#상승률 또는 하락률(%)
  rise_or_fall = (closeValue-nowValue)/(nowValue*0.01)
  return rise_or_fall

