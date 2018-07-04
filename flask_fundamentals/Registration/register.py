from flask import Flask, render_template, request, redirect, flash, session

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DIGITS_REGEX = re.compile(r'[A-Z0-9]')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

def init():
    pass

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   err = False
   if not request.form['fname'].isalpha():                  # len(request.form['fname']) < 1:
     flash("First Name cannot be Empty or contain numbers !")
     err = True
   if not request.form['lname'].isalpha():                   # len(request.form['lname']) < 1:
     flash("Last Name cannot be Empty or contain numbers !")
     err = True
   if ( 1 > len(request.form['password']) < 8):
     flash("Password cannot be Empty & Must be at least 8 chars long !")
     err = True
   if request.form['password'] != request.form['confirm']:
     flash("Confirm Password does not match Password !")
     err = True
   if len(request.form['email']) < 1:
     flash("Email cannot be empty !")
     err = True 
   if not EMAIL_REGEX.match(request.form['email']):
     flash("Invalid Email entered !")
     err = True  
   if not DIGITS_REGEX.match(request.form['password']):
       flash('Password must contain one upper case and a Number')
       err = True

   if err: return redirect('/')       
   else:
       return render_template("success.html")
       #return redirect('/') # OR to a confirmation page or something

app.run(debug=True) # run our server
