from flask import Flask, render_template, redirect, request

app = Flask(__name__)
colors = ['blue', 'red', 'purple', 'orange']
img_path = 'imgs/'

@app.route('/')
def index():
	print "no ninjas here"
	return render_template('index.html')


@app.route('/ninjas')
def ninjaturtles():
	image = "{}tmnt.png".format(img_path)
	return render_template('ninjas.html', image=image)

@app.route('/ninjas/<color>')
def thisninja(color):
	nt = "{}{}.jpg".format(img_path, color)
	april = "{}notapril.jpg".format(img_path)

	image = nt if color in colors else april

	return render_template('thisninja.html', image=image)

app.run(debug=True)