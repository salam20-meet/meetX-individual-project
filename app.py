from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

##### Code here ######
@app.route('/')
def homepage():
	all_comments=get_all_comments()
	print(all_comments,"!!!!!!!!!!!!!!!!!!!")
	return render_template("home.html")


@app.route('/team')
def teampage():
	return render_template("team.html")

@app.route('/family')
def familypage():
	return render_template("family.html")

@app.route('/contact')
def contactpage():
	return render_template("contact.html")

@app.route('/send', methods=['POST'])
def sendpage():
	subject = request.form['subject']
	print(subject,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	return render_template("send.html",all_comments=get_all_comments())



#####################


if __name__ == '__main__':
    app.run(debug=True)