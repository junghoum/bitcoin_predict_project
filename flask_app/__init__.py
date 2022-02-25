from flask import Flask, render_template, request
from bitcoin_value_predict import coin_value

import requests
from bs4 import BeautifulSoup



app = Flask(__name__)



@app.route('/') 
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['coinname']
    data2 = request.form['interval_time']
    data3 = request.form['periods_time']

    pred = coin_value(data1, data2, int(data3))
    pred = round(pred,2)

    message = ""

    if pred > 0:
        message =  str(pred)+'%' + " 만큼 상승할 수도 있습니다."
    elif pred < 0:
        message =  str(pred)+"%" + " 만큼 하락할 수도 있습니다."
    else:
        message = "변동 없음"
    return render_template('predict.html', predict_value=message)


@app.route('/coinlist')
def coin_list():
    return render_template('coinlist.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
    

