from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route("/")
def myForm():
	return render_template("form.html")

@app.route("/", methods=['POST'])
def myFormPost():
	text = request.form['text'].split('\r\n')
	words = [processed.split(" ") for processed in text]
	return render_template("form.html", words = words)

if __name__ == '__main__':
	app.run(debug=True)

