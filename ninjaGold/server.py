from flask import Flask, render_template, request, redirect, session, flash
import random
# for creating current time
import arrow
utc = arrow.utcnow()
local = utc.to('US/Pacific')

app = Flask(__name__)
# app.secret_key is only needed when using session
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def buildings():
    buildings = {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-50,20),
    }
    current_activity = {}
    if request.form['building'] in buildings:
        print request.form['building']
        print buildings[request.form['building']]
        if buildings[request.form['building']] < 0:
            current_activity['class'] = 'lost'
            current_activity['log'] = 'Entered a {} and lost {} golds..... Ouch... ({})'.format(request.form['building'], abs(buildings[request.form['building']]), arrow.now().format('YYYY/MM/DD hh:mm a'))
        else:
            current_activity['class'] = 'gained'
            current_activity['log'] = 'Earned {} golds from the {}! ({})'.format(buildings[request.form['building']], request.form['building'], arrow.now().format('YYYY/MM/DD hh:mm a'))

        session['activities'].append(current_activity)
        session['total_gold'] += buildings[request.form['building']]

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug = True)
