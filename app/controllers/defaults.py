from flask import Flask, render_template,request, redirect, url_for, session
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    urna = request.form.get('urna')
    return render_template('index.html', urna=urna)


