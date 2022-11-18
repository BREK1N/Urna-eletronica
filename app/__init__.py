from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'naruto'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'urna'

mysql = MySQL(app)



from app.controllers import defaults
