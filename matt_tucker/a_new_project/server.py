from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, '')

@app.route('/')
def index():
    print "Inside the index method."

    return render_template('index.html')

app.run(debug=True)