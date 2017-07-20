from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'assc')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
	
	return render_template('index.html')



@app.route('/emailvalidate', methods=['POST'])
def emailvalidate():

	x = "SELECT email FROM associates WHERE `email` = :emailtxgrnhtf"
	print x
	mail = {
			'emailtxgrnhtf': request.form['emailform']
			}
	print mail
	emailList = mysql.query_db(x, mail)
	print emailList

	if emailList:
		flash("Its in here!")
	# else if email doesn't match regular expression display an "invalid email address" message
	else:
		flash("No email in database!")

	return redirect('/')


app.run(debug=True)
