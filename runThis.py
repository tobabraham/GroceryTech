from flask import Flask , render_template
from flask import request
import db


app = Flask(__name__)
currentUser = ""
"""Temporary usernames, add SQL queries later"""
"""
def validBuyer(uname, passwd):
	if uname == 'buyer' and passwd == 'b':
		return True
	else:
		return False

def validDeliverer(uname, passwd):
	if uname == 'deliverer' and passwd == 'd':
		return True
	else:
		return False

def validManager(uname, passwd):
	if uname == 'manager' and passwd == 'm':
		return True
	else:
		return False
"""

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('login1.html')


"""Will have to change the name of this """
@app.route('/loginReq', methods=['GET','POST'])
def loginReq():
	if request.method == 'POST':
		_name = request.form['username']
		_password = request.form['password']
		num = db.login(_name, _password)
		global currentUser
		if num == 1:
			currentUser = _name
			return render_template('managerFunctionality22.html')
		elif num == 2:
			currentUser = _name
			return render_template('delivererFunctionality18.html')
		elif num == 3:
			currentUser = _name
			return render_template('buyerFunctionality6.html')
		else:
			return render_template("login1.html", error="Credentials Incorrect")

@app.route("/login")
def login():
	error="Invalid Username/Password"
	return render_template('login1.html', error=error)


@app.route('/buyerFunctionality', methods=['GET','POST'])
def buyerFunctionlity():
	return render_template('buyerFunctionality6.html')


@app.route('/registrationType', methods=['GET','POST'])
def registrationType():
	return render_template('registrationType2.html')


@app.route('/registerBuyer', methods=['GET','POST'])
def registerBuyer():

	if request.method == "POST":
		fname = request.form['fname']
		uname = request.form['uname']
		password = request.form['password']
		email = request.form['email']
		street = request.form['street']
		houseNo = request.form['houseNo']
		city = request.form['city']
		lname = request.form['lname']
		phone = request.form['phone']
		cpassword = request.form['cpassword']
		state = request.form['state']
		zipp = request.form['zip']

		error1 = "your password is messed up bro"
		error2 = "phone has incorrect number of digits"
		error3 = "zip code has incorrect number of digits"
		error4 = "email contains non-alphanumeric characters"
		a, b, c = email.rsplit('@', '.')
		if password != cpassword:
			return render_template("registerBuyer3.html", error=error1)
		elif (len(str(abs(phone)))) != 10:
			return render_template("registerBuyer3.html", error=error2)
		elif (len(str(abs(zip)))) != 5:
			return render_template("registerBuyer3.html", error=error3)
		elif a.isalnum() and b.isalnum() and c.isalnum():
			return render_template("registerBuyer3.html", error=error4)
		else:
			query = "SELECT MAX(id) FROM Address;"
			response = cursor.execute(query)
			cursor.fetchall()
			AddID = response + 1
			user_type = 'buyer'
			reg = db.insertUser(uname,password,user_type,email,fname,lname)
			if reg != 0:
				return render_template("registerBuyer3.html", error="Username is Taken.")

			reg = db.insertAddress(AddID,houseNo,street,city,zipp)
			reg = db.insertBuyer(uname,phone,AddID,'Visa',6)
			return render_template('login1.html')





	return render_template('registerBuyer3.html')

@app.route('/registerDeliverer', methods=['GET','POST'])
def registerDeliverer():
	return render_template('registerDeliverer4.html')

@app.route('/registerManager', methods=['GET','POST'])
def registerManager():
	return render_template('registerManager5.html')

@app.route('/listOfStores', methods=['GET','POST'])
def listOfStores():
	return render_template('listOfStores8.html' )

@app.route('/storeHomepage', methods=['GET','POST'])
def storeHomepage():
	return render_template('storeHomepage9.html')

"""
@app.route('/buyerAccountInfo', methods=['GET','POST'])
def buyerAccountInfo():
	return buyerAccInfo()
"""

@app.route('/buyerAccountInfo', methods=['GET','POST'])
def buyerAccountInfo():
	dictry = {}
	dictry['fname'] = 'Fred'
	return render_template("buyerAccountInfo7.html", dictry=dictry)


@app.route('/findItem', methods=['GET','POST'])
def findItem():
	return render_template('findItem10.html')

@app.route('/itemType', methods=['GET','POST'])
def litemType():
	if request.method == 'POST':
		Itype = request.form['value']
		itemType(Itype)
	

@app.route('/itemType/<Itype>', methods=['GET','POST'])
def itemTypeI(Itype):
	return render_template('itemType11.html', Itype=Itype)


@app.route('/cart', methods=['GET','POST'])
def cart():
	return render_template('cart12.html')

@app.route('/checkout', methods=['GET','POST'])
def checkout():
	return render_template('checkout13.html')


@app.route('/paymentMethods', methods=['GET','POST'])
def paymentMethods():
	return render_template('paymentMethods14.html')

@app.route('/newPayment', methods=['GET','POST'])
def newPayment():
	return render_template('newPayment15.html')

@app.route('/reciept', methods=['GET','POST'])
def reciept():
	return render_template('reciept16.html')

@app.route('/orderHistory', methods=['GET','POST'])
def orderHistory():
	return render_template('orderHistory17.html')





@app.route('/delivererFunctionality', methods=['GET','POST'])
def delivererFunctionality():
	return render_template('delivererFunctionality18.html')

@app.route('/delivererAccInfo', methods=['GET','POST'])
def delivererAccInfo():
	return render_template('delivererAccountInfo19.html')

@app.route('/assignments', methods=['GET','POST'])
def assignments():
	return render_template('assignments20.html')

@app.route('/assignment', methods=['GET','POST'])
def assignment():
	return render_template('assignment21.html')




@app.route('/managerFunctionality', methods=['GET','POST'])
def managerFunctionality():
	return render_template('managerFunctionality22.html')

@app.route('/managerAccInfo', methods=['GET','POST'])
def managerAccInfo():
	return render_template('managerAccountInfo23.html')

@app.route('/revenueReport', methods=['GET','POST'])
def revenueReport():
	return render_template('revenueReport24.html')

@app.route('/outstandingOrders', methods=['GET','POST'])
def outstnadingOrders():
	return render_template('outstandingOrders25.html')
@app.route('/inventory', methods=['GET','POST'])
def inventory():
	return render_template('inventory26.html')



if __name__ == '__main__' :
	app.run()
