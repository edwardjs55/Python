# Dev: Michael G.
# Date 3/16/2018
# Build with: python, flask, mySQL, html, css
# Description:  Basic message posting application that demonstrates user login and registration
# application allows registered/logged in users to post messages and comments on community wall
 
#------------------------------------- IMPORTS --------------------------------------
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import md5
import re
import datetime
#------------------------------------------------------------------------------------



app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key='keepItSecret'
mysql = MySQLConnector(app, 'the_wall')


@app.route('/')
def index():
    init()
    return render_template("index.html")


def init():
    # if 'user_id' not in session: 
    #     session['user'] = []
    if 'data' not in session:
        session['data'] = []


@app.route('/validate', methods=['POST'])
def validate():

    notValid = False
    # get first name and last name from form
    firstName = request.form['firstName']
    lastName = request.form['lastName']
     # get email from form
    email = request.form['email']
      # get 1st password entry
    p1 = request.form['password']
    # get 2nd passworkd entry
    p2 = request.form['confirmPass']
     # get date of birth
    # dob = request.form['dob']
    # print dob

    # validate first name and last name fields are not empty
    if len(firstName) < 1 or len(lastName) < 1:
        flash('first name or last name can not be empty!')
        notValid = True
    
    # validate there are no numbers in name
    if hasNum(firstName) or hasNum(lastName):
        flash('first name or last name must not contain numbers!')
        notValid = True
        
    # validate that email is not empty
    if len(email) < 1:
        flash('email must not be empty!')
        notValid = True
        
    # validate email is valid
    if not matchEmail(email):
        flash('email is not valid!')
        notValid = True
        
    # validate password fields are not empty
    if len(p1) < 1 or len(p2) < 1:
        flash('password fields can not be empty')
        notValid = True

    # validate password fields are not empty
    if len(p1) < 9 or len(p2) < 9:
        flash('passwords must be greater than 8 characters')
        notValid = True

    # validate password entries are the same
    if p1 != p2:
        flash('password entries do not match!')
        notValid = True

    # validate password has at least one uppercase and numeric value
    if hasNum(p1) == False or hasUpper(p1) == False:
        flash('password must have at least one uppercase character and one numeric character!')
        notValid = True 

    if notValid:
        return redirect('/')
    else:
        # if data is valid then insert data into database
        hashpass = md5.new(p1).hexdigest()    # get hash of password            
        query = "INSERT INTO users (first_name, last_name,  email, password, created_at, updated_at) VALUES(:user_first_name, :user_last_name, :user_email, :user_pass, NOW(), NOW())"
        data = {
            'user_first_name': firstName,
            'user_last_name': lastName,
            'user_email': email,
            'user_pass': hashpass
        }
        val = mysql.query_db(query, data)

        query ="select * from users where email='{}' and password='{}'".format(email,  hashpass)    
        session['user'] = mysql.query_db(query)[0]
        print session['user']
        return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    user_email = request.form['email']
    user_pass = request.form['pass']

    hashed_pass = md5.new(user_pass).hexdigest()    # get hash of password

    query ="select * from users where email='{}' and password='{}'".format(user_email, hashed_pass)    
    result = mysql.query_db(query)
    # print result
    if result:  
        # if 'user' not in session:
        session['user'] = result[0]
        print session['user']
        # message = 'hello ' + session['user']['first_name'] + ' ' + session['user']['last_name']
        # flash(message)
        return redirect('/success')
    else:
        message = 'Incorrect email/password combination'
        flash (message)
        redirect('/')

@app.route('/success')
def ShowUserWall():
    ## need to  query for user info
    # query = "select messages.message, concat_ws(\' \', first_name, last_name) as name, date_format(messages.updated_at, \'%b %d %Y\') as date, comments.comments from users left\
    # join messages on users.id = messages.user_id left join comments on messages.id = comments.message_id order by messages.updated_at desc;"
    # result = mysql.query_db(query)

    query = "select comments, comments.id as comment_id, message, concat_ws(\' \', first_name, last_name) as name, messages.id as msg_id,\
    date_format(messages.updated_at, \'%b %d %Y\') as date, users.id as users_id from messages left join comments\
    on comments.message_id = messages.id left join users on messages.user_id = users.id;"
    result = mysql.query_db(query)
    
    # for n in  range(0, )
    print(result)

    session['data'] = result
    # print session['data'] 
    session['ordered_data'] = []
    ordered_data = []
    temp_message_ids = []
    temp_comment_ids = []

    index = 0
    for n in ( session['data']) :
        if n['msg_id'] not in temp_message_ids:
            temp_message_ids.append( n['msg_id'] )
            msg_tuple = ( n['message'], n['name'], n['date'], n['msg_id'])
            ordered_data.append( (msg_tuple, []) )

        # if session['data']['comment_id'] not in  temp_comment_ids:
            q = "select concat_ws(\' \', first_name, last_name) as name, comments, date_format(comments.created_at, \'%b %d %Y\') as date from users left join messages\
            on users.id = messages.user_id left join comments on messages.id = comments.message_id where message_id =" + str(n['msg_id']) + ";"
            tempComments = mysql.query_db(q)
            # print q
            for j in tempComments:
                temp_comment_ids.append( n['comment_id'] )
                com_tuple = ( j['comments'], j['name'], j['date'] )
                ordered_data[index][1].append(com_tuple)
            if tempComments:
                index += 1
                
    # ordered_data = []
    temp_message_ids = []
    temp_comment_ids = []
    session['ordered_data'] = ordered_data
    return render_template('wall.html')

@app.route('/postMessage', methods=['POST'])
def postMessage():
    if 'user' in session:
        user_id = session['user']['id']
        m = request.form['message']
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES(:id, :mesg, NOW(), NOW() )"
        data = {
            'id': user_id,
            'mesg': m
        }
        val = mysql.query_db(query, data)
    else:
        print "session does not exist"
    return redirect('/success')

@app.route('/postComment', methods=['POST'])
def postComment():
    msg_id = request.form['msgid']
    us_id = session['user']['id']
    msg = request.form['comment']

    query = "INSERT INTO comments (user_id,  comments,  message_id, created_at, updated_at) VALUES(:u_id, :comm, :m_id, NOW(), NOW() )"
    data = {
        'u_id': us_id,
        'm_id': msg_id,
        'comm': msg
    }
    val = mysql.query_db(query, data)
    return redirect('/success')

def hasNum(someStr):
    return any(char.isdigit() for char in someStr)

def matchEmail(e):
    return bool(re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', e))

def hasUpper(p):
    return ( any(x.isupper() for x in p) )

app.run(debug=True)
