from flask import Flask, render_template,request, redirect, url_for, session
from app import app
from app import mysql
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

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

@app.route('/mesario', methods=['GET', 'POST'])
def mesario():

    msg = '' 
    if request.method == 'POST' and 'nome' in request.form and 'sobrenome' in request.form and 'turma' in request.form:
        nome = request.form.get('nome') 
        sobrenome = request.form.get('sobrenome') 
        turma = request.form.get('turma')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('INSERT INTO mesario VALUES (NULL, % s, % s, % s)', (nome, sobrenome, turma)) 
        mysql.connection.commit() 
        msg = 'Registrador com sucesso'
    elif request.method == 'POST': 
        msg = 'Por favor, preencha o formulário !'
    return render_template('mesario.html', msg=msg)

@app.route('/plano_comk')
def plano_comk():
    return render_template('plano_gorv_comk.html')
    
@app.route('/plano_andre')
def plano_andre():
    return render_template('plano_andre.html')
    





