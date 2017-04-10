from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/', defaults={'ninja': 'all'})
@app.route('/ninja/<ninja>')
def ninjas(ninja):
    ninjas = {
        'all': 'images/tmnt.png',
        'red': 'images/raphael.jpg',
        'orange': 'images/michelangelo.jpg',
        'blue': 'images/leonardo.jpg',
        'purple': 'images/donatello.jpg',
    }
    if ninja in ninjas:
        image = ninjas[ninja]
    else:
        image = 'images/notapril.jpg'

    return render_template('ninjas.html', img = image)

app.run(debug=True)
