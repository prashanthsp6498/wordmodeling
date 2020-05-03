import os
from googletrans import Translator
from model.predictor import Predictor


class LanguageManager:
    def __init__(self):
        self.translator = Translator()
        # os.chdir('model')

    def Suggestion(self, word):
        preditorObject = Predictor(model='model/checkpoints/kannada/model.h5',
                                   tokenizer='model/pickle_objects/kannada/tokenizer_model4')
        return preditorObject.textGenerator(word)

    def Trans(self, word):
        translatedWord = self.translator.translate(word, dest='kn')
        return translatedWord.text
