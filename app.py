from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

##### Code here ######
@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/team')
def teampage():
	return render_template("team.html")

@app.route('/family')
def familypage():
	return render_template("family.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)