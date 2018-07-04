from flask import Flask, request, redirect, render_template,session, flash
import re # import REGEX libraries
import md5 # import md5 Hashing
import os, binascii # import salt stuff

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation string
NAME_REGEX = re.compile(r'^[a-zA-Z]+$') #first name/last name validation string
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key="MindYourownbusiness"
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'registration')

def init():
    # session.pop('id')
    pass

@app.route('/users')
def index():
    init()    
    return render_template('index.html')

@app.route('/users/new')
def new():
      
    return render_template('newuser.html')

@app.route('/users/<id>/edit')
def edit():
      
    return render_template('edituser.html')

@app.route('/users/<id>')
def show():
      
    return render_template('showuser.html')

@app.route('/users/create', methods=['POST'])
def create():
      
    return render_template('createuser.html')

@app.route('/users/<id>/delete')
def delete():
      
    return render_template('deleteuser.html')

@app.route('/users/<id>', methods=['POST'])
def update():
      
    return render_template('updateuser.html')

    
    







@app.route('/register', methods=['POST'])
def register():
    # verify input via Flash Error messages
    # save data
    # display success page W message render W/ flash message
    first = request.form['firstname']
    last = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']

    # VERIFICATION
    err = False
    if len(first) < 2 :
        flash("First Name cannot be blank or less than 2 Chars",category='registration')
        err = True
    if not NAME_REGEX.match(first) :
        flash("First Name must contain Letters Only",category='registration')
        err = True
    if len(last) < 2 :
        flash("Last Name cannot be blank or less than 2 Chars",category='registration')
        err = True
    if not NAME_REGEX.match(last) :
        flash("Last Name must contain Letters Only",category='registration')
        err = True   
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email address Entered, Try again',category='registration')
        err = True
    if not password == confirm  or len(password) < 8 :
        flash('Password must be at least 8 Chars and Match Confirm Password',category='registration')
        err = True

        if err:
            return redirect('/')
        # Save data to Database
        # Generate Salted/Hashed Password
    salt_str = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt_str).hexdigest()
    print salt_str
        # to Read this Hashed/salted for LOGIN
        #  same algorithim & Compare
        #  encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        #  if user[0]['password'] == encrypted_password:
    query = "INSERT INTO users (first_name, last_name, email, salt, password, created_at, \
         updated_at, real_password) VALUES (:first_name, :last_name, :email, :salt, :password, NOW(), NOW(), :real)"
    data = {
             'first_name': first,
             'last_name':  last,
             'email': email,
             'password': hashed_pw,
             'salt': salt_str,
             'real': password
           }
    result = mysql.query_db(query, data)
    #print result
    message = "Registration was Successful"
    return render_template('success.html',message = message)


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    err = False
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        print 'Encrpto Psswd = ',encrypted_password
        print 'User Password = ',user[0]['password']
        print 'salt          = ',user[0]['salt']

        if user[0]['password'] == encrypted_password:  # this means we have a successful login!
            print 'Sucess, Yea'
        else:   # invalid password!
            flash('Invalid Password Entered, Try Again.',category='login')
            err = True           
    else:  # invalid email!
        flash('That Email was not found, try again or Register.',category='login')
        err = True 

    if err: # Process the Flash messages/Errors
        return redirect('/')
    else:
        session['id'] = user[0]
        print session['id']
        print session['id']['first_name']
        
        result = "Successful Login Completed for " + session['id']['first_name']
        return render_template('success.html',message=result)
    # if EMAIL_REGEX.match(request.form['email']):
    #     session['email'] = request.form['email']
    #     print session['email']         
    #     return redirect('/email_success')
    # else:
    #     flash("Invalid Email entered, Please try Again ")
    #     return redirect('/')

    # 
    #print 'Verify this thing',session['email']
    #query = "SELECT * FROM emails where email = :Qemail limit 1"
    #data = {'Qemail': session['email']}
    #result = mysql.query_db(query,data)
    # select/Query search /Sanitized
    # print result
    # if result:
    #     print 'id = ',result[0]['id'], 'the email = ', result[0]['email'] 



app.run(debug=True)
