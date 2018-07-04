from flask import Flask, request, redirect, render_template,session, flash
import re # import REGEX libraries
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation string
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key="MindYourownbusiness"
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'emailverification')

@app.route('/')
def index():
    session.pop('email',None)
    # friends = mysql.query_db("select concat_ws(' ',first_name,last_name) as name,age, \
    #  Date_Format(friends_since,'%b %d') as since, year(friends_since) as year from friends;")    
    return render_template('index.html')

@app.route('/email_verify', methods=['POST'])
def verify():       
    if EMAIL_REGEX.match(request.form['email']):
        session['email'] = request.form['email']
        print session['email']         
        return redirect('/email_success')
    else:
        flash("Invalid Email entered, Please try Again ")
        return redirect('/')

    # 
    #print 'Verify this thing',session['email']
    #query = "SELECT * FROM emails where email = :Qemail limit 1"
    #data = {'Qemail': session['email']}
    #result = mysql.query_db(query,data)
    # select/Query search /Sanitized
    # print result
    # if result:
    #     print 'id = ',result[0]['id'], 'the email = ', result[0]['email'] 

@app.route('/email_success')
def success():
# def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': session['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    # GET all data & redisplay in HTML
    query = "SELECT * FROM emails limit 6 "                           # define your query
    friends = mysql.query_db(query)                          # run query with query_db()
                                                             # pass data to our template
    # print friends
    return render_template('success.html',data=friends)
    # return redirect('/')

app.run(debug=True)
