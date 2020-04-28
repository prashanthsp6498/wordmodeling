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
    num = ['who', 'am', 'i', 'and', 'for', 'do']
    number = [0, 1, 2, 3, 4, 5, 6]
    num = WordSuggestion('hello')
    return render_template('word_predictor.html', num=num, number=number)
