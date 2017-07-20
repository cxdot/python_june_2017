from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'assc')

@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM associates")

	return render_template('index.html', all_friends=friends)


@app.route('/addfriend', methods=['POST'])
def addfriend():
    query = "INSERT INTO associates (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"

    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
           }
    mysql.query_db(query, data)
    return redirect('/')












app.run(debug=True)

