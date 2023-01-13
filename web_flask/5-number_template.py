#!/usr/bin/python3

""" a script thet starts Flask web app """

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    # Return Hello HBNB
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBHB():
    # Return HBNB
    return 'HBNB'


@app.route('/c/<string:text>')
def C(text):
    # Return C + text
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<string:text>')
def python(text='is cool'):
    # Return Python + text
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>/')
def number(n):
    # Return number
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>/')
# Return number
def number_template(n):
    return render_template('number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
