import os
from googletrans import Translator
from .model.predictor import Predictor


class LanguageManager:
    def __init__(self):
        self.translator = Translator()
        os.chdir('model')

    def Suggestion(self, word):
        preditorObject = Predictor()
        return preditorObject.textGenerator(word)

    def Trans(self, word):
        translatedWord = self.translator.translate(word, dest='kn')
        return translatedWord.text
