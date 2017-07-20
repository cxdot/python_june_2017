from flask import Flask, render_template    # Import Flask to allow us to create our app.
app = Flask(__name__)    					# Global variable __name__ tells Flask whether or not we are running the file
                         					# directly, or importing it as a module.
@app.route('/')          					# The "@" symbol designates a "decorator" which attaches the following
                         					# function to the '/' route. This means that whenever we send a reques   to
@app.route('/index')
def indexhtml():
  return render_template('index.html')  
                         					# localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return render_template('index.html', name="Christian")  # Return the string 'Hello World!' as a response.
app.run(debug=True)      # Run the app in debug mode.



# @app.route('/success')
# def success():
#   return render_template('success.html')