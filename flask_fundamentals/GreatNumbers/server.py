from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key ="DontLookHere"  # must set secter key for SESSIONs to Work
# our index route will handle rendering our form

def init():
    if 'number' in session:
        pass
    else:
        session['number'] = random.randrange(0,101)


@app.route('/')
def index():
    init()
    print 'Secret #:', session['number']
    # session["result"] = ""
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/submit', methods=["POST"])
def submit():
    init()    
    if request.form['guess'] == '':
        session['result'] = "empty"
        #return render_template("index.html",result=session["result"])
        return redirect('/')
    print "Submitted"
    guess = request.form['guess']
    mynumb = session["number"]
    print guess
    if int(guess) == mynumb:
        session["result"] = "win"
        print "You Won!!"
        #session.pop('number')        
    elif int(guess) > mynumb:
        session["result"] = "high"
    elif int(guess) < mynumb:
        session["result"] = "low"

    #return render_template("index.html",result=session["result"])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if 'number' in session: session.pop('number')
    #session.pop('guess')
    if 'result' in session: session.pop('result')
    print "RESET entered"
    return redirect('/')


app.run(debug=True) # run our server

