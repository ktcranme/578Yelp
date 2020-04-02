import spacy
from collections import Counter
import multiprocessing as mp


class WordCloud(object):
    def __init__(self, docs):
        self.docs = docs
        self.disablelayers = ['parser', 'ner', 'textcat']
        self.pos = ['NOUN', 'PROPN']
        self.nlp = spacy.load('en', disable=self.disablelayers)
 
    def getCounter(self):
        word_count = Counter()
        docs = self.nlp.pipe(self.docs, n_process=mp.cpu_count(), disable=self.disablelayers)

        for doc in list(docs):
            for token in doc:
                if not token.is_stop and not token.is_punct and token.pos_ in self.pos:
                    word_count[token.lemma_] += 1
        
        return word_count