import os
from flask import Flask, render_template, request, jsonify
from .model.predictor import Predictor

app = Flask(__name__)

os.chdir('model')


def WordSuggestion(word):
    preditorObject = Predictor()
    return preditorObject.textGenerator(word)


@app.route('/')
def index():
    number = [0, 1, 2, 3, 4, 5, 6]
    return render_template('word_predictor.html', number=number)


@app.route('/wordpredict', methods=['POST'])
def wordpredict():
    if request.method == 'POST':
        text = request.form['textbox']
        suggestions = WordSuggestion(text)
        return jsonify(result=suggestions)
