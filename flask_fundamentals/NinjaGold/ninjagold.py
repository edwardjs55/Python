from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key ="DontLookHere"

def init():
    if 'log' in session:
        pass
    else:
        session['log'] = []
        session['gold'] = 0

@app.route('/')
def index():
    init()
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])    
def process():
    place = request.form["building"]
    if place == 'farm':
        winnings = random.randrange(10, 20)
    elif place == 'cave':
        winnings = random.randrange(5, 10)
    elif place == 'house':
        winnings = random.randrange(2, 5)
    elif place == 'casino':
        winnings = random.randrange(-50, 50)
    session['gold'] += winnings

    # Create Log Entries
    from time import gmtime, strftime
    now = strftime("%a, %d %b %Y %H:%M", gmtime())    #gmtime()
    print now
    if winnings > 0 and place != 'casino':
        session['log'].append((" Earned {} golds at the {}.  ({})".format(winnings,place,now),'green'))        
    elif winnings >= 0 and place == 'casino':
        session['log'].append((" Entered a Casino and WON {} golds Yippee.. {}.  ({})".format(winnings,place,now),'green'))
    elif winnings < 0 and place == 'casino':
        session['log'].append((" Entered a Casino and LOST {} golds... Ouch.. {}.  ({})".format(winnings,place,now),'red'))

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('log')
    return redirect('/')

app.run(debug=True) # run our server

