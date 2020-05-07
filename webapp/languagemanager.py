import os
import webapp
from googletrans import Translator
from webapp.model.predictor import Predictor
# from webapp import module_dir


class LanguageManager:
    def __init__(self):
        self.translator = Translator()
        # os.chdir('model')

    def Suggestion(self, word):
        model_path = os.path.join(
            webapp.module_dir, 'model/checkpoints/kannada/model.h5')
        tokenizer_path = os.path.join(
            webapp.module_dir, 'model/pickle_objects/kannada/tokenizer_model4')
        preditorObject = Predictor(model=model_path,
                                   tokenizer=tokenizer_path)
        return preditorObject.textGenerator(word)

    def Trans(self, word):
        translatedWord = self.translator.translate(word, dest='kn')
        return translatedWord.text
