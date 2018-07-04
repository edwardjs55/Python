from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="DontLookHere"  # must set secter key for SESSIONs to Work
# our index route will handle rendering our form
@app.route('/')
def index():
    session["counter"] += 1
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/reset', methods=["POST"])
def reset():
    print "RESET Called "
    session["counter"] = 0
    #return render_template("index.html")
    return redirect('/')

@app.route('/double_Inc', methods=['POST'])
def double():
    print "double Increment "
    session["counter"] +=1 # / adds one already
    #return render_template("index.html")
    return redirect('/')       

app.run(debug=True) # run our server
