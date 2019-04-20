import numpy as np

from core.cleaner import Cleaner


class Corpus:
    def __init__(self, corpus=None, path_to_corpus=None):

        self.corpus = corpus
        self.path_to_corpus = path_to_corpus

        if self.path_to_corpus:
            with open(file=self.path_to_corpus, encoding="utf-8") as file:
                self.corpus = file.read()

        self.bi_ph_fre = self.calc_bi_ph_freq()
        self.freq_result = np.array(list(self.bi_ph_fre.values()))

    def calc_bi_ph_freq(self):
        # Clean the corpus
        self.corpus = Cleaner.keep_only_arabic(self.corpus)
        self.corpus = Cleaner.remove_diacritics(self.corpus)
        self.corpus = Cleaner.remove_punctuations(self.corpus)
        self.corpus = Cleaner.normalize_arabic(self.corpus)

        arabic_alphabet = 'ابجدهوزحطيكلمنسعفصقرشتثخذضظغ'
        bi_ph_arr = {''.join([l1, l2]): 0.0 for l1 in arabic_alphabet for l2 in arabic_alphabet}

        word_list = self.corpus.split()
        bi_phonemes_from_corpus = []

        for word in word_list:
            for i in range(1, len(word)):
                bi_ph = ''.join([word[i - 1], word[i]])
                if bi_ph in bi_ph_arr:
                    bi_ph_arr[bi_ph] += 1
                bi_phonemes_from_corpus.append(bi_ph)

        bi_ph_freq = {bi_ph: (val / len(bi_phonemes_from_corpus)) for bi_ph, val in
                      bi_ph_arr.items()}
        return bi_ph_freq
