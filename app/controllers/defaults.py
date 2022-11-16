from flask import Flask, render_template,request, redirect, url_for, session
from app import app

andre = []
lukas = []


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/votacao', methods=['GET', 'POST'])
def votacao():

    global andre
    global lukas

    urna = request.form.get('urna')
    if urna == "76":
        andre.append(1)
    if urna == "12":
        lukas.append(1)

    return render_template('votacao.html', urna=urna)

@app.route('/resultado')
def resultado():
    return render_template('resultado.html', lukas=len(lukas), andre=len(andre))

@app.route('/mesario')
def mesario():
    return render_template('mesario.html')



