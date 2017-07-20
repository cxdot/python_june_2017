from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	print "index method"

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	print "Im processed"

	yourname = request.form['yourname']
	locate = request.form['location']
	lang = request.form['language']
	cmts = request.form['comment']

	print yourname
	print lang
	print locate
	print cmts

	return render_template('submit.html', name=yourname, location=locate, language=lang, comments=cmts)

app.run(debug=True)


