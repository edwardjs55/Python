from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/ninjas')
def ninjas():
  return render_template("ninjas.html")

@app.route('/ninja/<color>')
def ninja(color):
  src = "notapril.jpg"
  if color =="blue": src= "Leonardo.jpg"
  if color =="orange": src= "Michelangelo.jpg"
  if color =="red": src= "Raphael.jpg"
  if color =="purple": src= "Donatello.jpg"
  x = "/static/img/" + src
  src = x
  #   src = "/static/img/tmnt.png"
  return render_template("ninja.html",imgsrc = src)
app.run(debug=True) # run our server
