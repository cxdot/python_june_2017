from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def mynameis():
	name = request.form['full_name']
	print name
	
	return redirect('/')

app.run(debug=True)