from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    num = ['who', 'am', 'i', 'and', 'for', 'do']
    number = [0, 1, 2, 3, 4, 5, 6]
    return render_template('word_predictor.html', num=num, number=number)