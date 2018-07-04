from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninjas')
def ninja():
  return render_template("ninja.html")

@app.route('/dojo/news')
def dojoNews():
  return render_template("dojos.html")

# @app.route('/dojo/news', methods=['POST'])
# def create_user():
#    print "Got Post Info"
#    # we'll talk about the following two lines after we learn a little more
#    # about forms
#    name = request.form['name']
#    email = request.form['email'] 
#    # redirects back to the '/' route
#    return redirect('/')

app.run(debug=True) # run our server
