from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = "s3cr3tk3y"

@app.route('/')
def index():
    if 'gold' in session:
        pass
    else:
        session['gold'] = 0
    if 'messages' in session:
        pass
    else:
        session['messages'] = []

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        string = "You have earned " + str(gold) + " gold."
        session['messages'].append(string)
        session['gold'] += gold
    if request.form['building'] == 'cave':
        gold = random.randrange(5,11)
        string = "You have earned " + str(gold) + " gold."
        session['messages'].append(string)
        session['gold'] += gold
    if request.form['building'] == 'house':
        gold = random.randrange(2,6)
        string = "You have earned " + str(gold) + " gold."
        session['messages'].append(string)
        session['gold'] += gold
    if request.form['building'] == 'casino':
        gold = random.randrange(-50,51)
        if gold < 0:
            string = "You have lost " + str(gold) + " gold."
            session['messages'].append(string)
        else:
            string = "You have earned " + str(gold) + " gold."
            session['messages'].append(string)
        session['gold'] += gold

    if request.form['building'] == 'reset':
        session.clear()

    return redirect('/')




app.run(debug=True)
