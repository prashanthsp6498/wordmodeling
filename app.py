import os
from flask import Flask, render_template, request, jsonify
from .languagemanager import LanguageManager

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


langManager = LanguageManager()


@app.route('/')
def index():
    number = [0, 1, 2, 3, 4, 5, 6]
    return render_template('word_predictor.html', number=number)


@app.route('/api/wordpredict', methods=['GET'])
def wordpredict():
    global langManager
    text = request.args['word']
    text = text.split()[-1]
    suggestions = langManager.Suggestion(text)
    return jsonify(result=suggestions)


@app.route('/api/translator', methods=['GET'])
def getWord():
    global langManager
    word = request.args['word']
    word = langManager.Trans(word)
    return jsonify({"word": word})


# @app.errorhandler(404)
# def not_found(error):
#     return "<h1>Ooooooooooppppppppssssssssssssss</h1>"
