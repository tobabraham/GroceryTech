from flask import Flask , render_template
from flask import request


app = Flask(__name__) 


"""Temporary usernames, add SQL queris later"""
def validBuyer(uname, passwd):
	if uname == buyer & passwd == passwordb:
		return true
	else:
		return false
	
def validDeliverer(uname, passwd):
	if uname == deliverer & passwd == passwordd:
		return true
	else:
		return false
	
def validManager(uname, passwd):
	if uname == manager & passwd == passwordm:
		return true
	else:
		return false


@app.route('/', methods=['GET','POST']) 
def index():
	return render_template('login1.html')


@app.route('/registrationType', methods=['GET','POST'])
def registrationType():
	return render_template('registrationType2.html')

@app.route('/buyerFunctionality', methods=['GET','POST'])
def buyerFunctionlity():
	if request.method == 'POST':
		if validLogin(request.form['username'], request.form['password']):
			return render_template('buyerfunctionality3.html')
		else:
			error="Invalid Username/Password"
		
	return render_template('login1.html', error=error)























if __name__ == '__main__' :
	app.run(debug=True, host='0.0.0.0') 
