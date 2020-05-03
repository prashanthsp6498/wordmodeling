import os
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


class Predictor:
    def __init__(self, model=None, tokenizer=None, seq_len=6, num_gen_words=6):
        if model:
            self.model = load_model(model)
        else:
            self.model = load_model(os.path.join(
                'checkpoints', 'kannada', 'model.h5'))

        if tokenizer:
            self.tokenizer = load(open(tokenizer, 'rb'))
        else:
            self.tokenizer = load(
                open(os.path.join('pickle_objects', 'kannada', 'tokenizer_model4'), 'rb'))

        self.seq_len = seq_len
        self.num_gen_words = num_gen_words

    def textGenerator(self, seed_text):
        output_text = []
        input_text = seed_text
        for i in range(self.num_gen_words):
            encoded_text = self.tokenizer.texts_to_sequences([input_text])[0]
            pad_encoded = pad_sequences(
                [encoded_text], maxlen=100, truncating='pre')
            pred_word_ind = self.model.predict_classes(
                pad_encoded, verbose=0)[0]

            pre_word = self.tokenizer.index_word[pred_word_ind]
            input_text += ' ' + pre_word
            output_text.append(pre_word)
        # return ' '.join(output_text)
        return output_text


if __name__ == "__main__":
    predictor = Predictor()
    print("\n\n===>Enter --exit to exit from the program")
    while True:
        num_gen_words = 3
        seed_text = input("Enter String: ")
        if seed_text.lower() == '--exit':
            break
        else:
            seed_text = seed_text.split()[-1]
            out = predictor.textGenerator(seed_text)
            print('output: ' + seed_text)
            print(out)
            print('\n')
