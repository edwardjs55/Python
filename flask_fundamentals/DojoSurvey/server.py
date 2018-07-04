from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form

def init():
  session.pop('*')

@app.route('/')
def index():
  return render_template("DojoInfo.html")


@app.route('/process', methods=['POST'])
def create_user():
   print "Got Post Info  Name:", request.form['name'],'len:', len(request.form['comments'])
   # we'll talk about the following two lines after we learn a little more
   # about forms
   comsize = len(request.form['comments'])
   err = False
   if len(request.form['name']) < 1:
     flash("Name field cannot be Empty !")
     err = True
     # return redirect('/')
   if ( comsize < 1 or comsize > 120 ):
     flash("Comments({}) cannot be Empty or more than 130 chars".format(comsize))
     err = True
   if err: return redirect('/')
     # flash("Sucess, name entry is correct !")
   
   name = request.form['name']     
   email = request.form['email']
   loc = request.form['location']
   favlang = request.form['favLang']
   comments = request.form['comments']
   #print request.form["name"] 
   # redirects back to the '/' route
   return render_template("SurveySays.html", thename = name,email=email,location = loc, fav=favlang,comments=comments)
   #return redirect('/')

app.run(debug=True) # run our server
