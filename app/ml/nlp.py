import spacy
from collections import Counter, defaultdict
import multiprocessing as mp
import numpy as np

class WordCloud(object):
    def __init__(self, docs, ratings):
        # Word cloud count 
        self.docs = docs
        self.ratings = ratings
        self.disablelayers = ['parser', 'ner', 'textcat']
        self.pos = ['NOUN', 'PROPN']
        self.nlp = spacy.load('en', disable=self.disablelayers)
        self.color_range = ['#c70039', '#c70039', '#ffd800', '#6fb98f', '#6fb98f', '#2b580c']
 
    def getCounter(self):
        word_count = Counter()
        word_rating = defaultdict(list)
        docs = self.nlp.pipe(self.docs, n_process=mp.cpu_count(), disable=self.disablelayers)
        
        for index, doc in enumerate(docs):
            for token in doc:
                if not token.is_stop and not token.is_punct and token.pos_ in self.pos:
                    word_count[token.lemma_] += 1
                    word_rating[token.lemma_].append(self.ratings[index])

        word_color = {word: self.getColor(ratings) for word, ratings in word_rating.items()}
        return word_count, word_color
    
    def getColor(self, ratings):
        mean_rating = int(round(np.mean(ratings)))
        return self.color_range[mean_rating]