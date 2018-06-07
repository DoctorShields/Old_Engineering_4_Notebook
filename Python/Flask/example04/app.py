# my Flask web app
# flask is the web server
# jinja2 is the template engine

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index:
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
