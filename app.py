from flask import Flask, redirect, url_for, request, render_template
import re
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

NB0 = joblib.load("static/model/NB0.pkl")
vectorizer0 = joblib.load("static/model/vectorizer0.pkl")

NB1 = joblib.load("static/model/NB1.pkl")
vectorizer1 = joblib.load("static/model/vectorizer1.pkl")

NB2 = joblib.load("static/model/NB2.pkl")
vectorizer2 = joblib.load("static/model/vectorizer2.pkl")


@app.route('/', methods=['POST', 'GET'])
def predicted():
    if request.method == 'POST':
        sentence = request.form['sentence']
    else:
        sentence = request.args.get('sentence')
    rating = ' '
    probability = ''
    if sentence:
        sentence1 = vectorizer1.transform([sentence])
        rating = NB1.predict(sentence1)
    else:
        sentence = ''

    print(sentence)
    return render_template('web.html', rating=rating[0], sentence=sentence)


if __name__ == '__main__':
    app.run()
