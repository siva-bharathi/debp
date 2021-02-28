import pyrebase
from flask import *
app=Flask(__name__)
config = {
    "apiKey": "AIzaSyA_njnZN_0xGvxAItO2yLUpQc9rVJhTeSo",
    "authDomain": "debp-ae31f.firebaseapp.com",
    "databaseURL":"https://debp-ae31f-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "debp-ae31f",
    "storageBucket": "debp-ae31f.appspot.com",
    "messagingSenderId": "176970321404",
    "appId": "1:176970321404:web:463a05ea1d3b7e4d687679"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()
db1=firebase.database()
@app.route('/',methods=['GET','POST'])
def basic():

    return render_template('index.html')

@app.route('/debtors_apply_page',methods=['GET','POST'])
def debtors_apply_page():
    if request.method=='POST':
        email='-'
        Self_emp='-'
        Single_Marr='-'

        Full_name=request.form['Full_name']
        Phone_number=request.form['Phone_number']
        Aadhar_num=request.form['Aadhar_num']
        Salary=request.form['Salary']
        Ammount_needed=request.form['Ammount_needed']

        email=request.form['email']
        Self_emp=request.form['Self_emp']
        Single_Marr=request.form['Single_Marr']


        datas={'Full_name':Full_name,'Phone_number':Phone_number,'Aadhar_num':Aadhar_num,
        'Salary':Salary,'Ammount_needed':Ammount_needed,
        
        'email':email,'Self_emp':Self_emp,'Single_Marr':Single_Marr,
        }

        print(datas)
        db.push(datas)
        return render_template('success_message.html')
    return render_template('debtors_apply_page.html')
#########################################
# bankers_offering_page
#########################################
@app.route('/bankers_offering_page',methods=['GET','POST'])
def bankers_offering_page():
    Bank_name='-'
    Bank_email='-'
    Bank_phone_num='-'
    if request.method=='POST':
        Full_name=request.form['Full_name']
        Person_email=request.form['Person_email']
        Person_Phone_num=request.form['Person_Phone_num']

        Bank_name=request.form['Bank_name']
        Bank_email=request.form['Bank_email']
        Bank_phone_num=request.form['Bank_phone_num']

        Bank_invest_amount=request.form['Bank_invest_amount']
        Bank_expect_interest=request.form['Bank_expect_interest']


        datas={'Full_name':Full_name,'Person_email':Person_email,'Person_Phone_num':Person_Phone_num,
        
        'Bank_name':Bank_name,'Bank_email':Bank_email,'Bank_phone_num':Bank_phone_num,
        

        'Bank_invest_amount':Bank_invest_amount,'Bank_expect_interest':Bank_expect_interest,
        }

        print(datas)
        db1.push(datas)
        return render_template('success_message.html')
    return render_template('bankers_offering_page.html')
@app.route('/user_login_page',methods=['GET','POST'])
def user_login_page():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('index.html', s=successful)
		except:
			return render_template('user_login_page.html', us=unsuccessful)

	return render_template('user_login_page.html')


if __name__=='__main__':
    app.run()