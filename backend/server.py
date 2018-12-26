from flask import Flask
from flask import render_template
from decorator import requires_auth
app = Flask(__name__)

@app.route("/")
@requires_auth
def index_page():
	return render_template('index.html')

@app.route("/bsignup")
def bsignup_page():
	return decorator.hello()

@app.route("/bsignin")
def bsignin_page():
	return render_template('bsignin.html')

@app.route("/jsignup")
def jsignup_page():
	return render_template('jsignup.html')

@app.route("/jsignin")
def jsignin_page():
	return render_template('jsignin.html')

@app.route("/employeelist")
def employeelist_page():
	return render_template('employeelist.html')

@app.route("/feedback")
def feedback_page():
	return render_template('feedback.html')