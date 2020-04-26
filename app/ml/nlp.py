import spacy
from collections import Counter, defaultdict
import multiprocessing as mp
import numpy as np


class WordCloud():
    def __init__(self, docs, ratings):
        """Initialize word cloud

        Arguments:
            docs {list[str]} -- list of document strings
            ratings {list[float]} -- list of ratings float
        """
        self.docs = docs
        self.ratings = ratings
        self.disablelayers = ['parser', 'ner', 'textcat']
        self.pos = ['PROPN']
        self.nlp = spacy.load('en', disable=self.disablelayers)
        self.color_range = ['#c70039', '#c70039',
                            '#ffd800', '#6fb98f', '#2b580c']

    def getCounter(self):
        """Generates Counter of words with their sentiment colors

        Returns:
            tuple -- (list of word count dicts, list of word color dicts)
        """
        word_count = Counter()
        word_rating = defaultdict(list)
        docs = self.nlp.pipe(
            self.docs, n_process=1, disable=self.disablelayers)

        for index, doc in enumerate(docs):
            for token in doc:
                if not token.is_stop and not token.is_punct and token.pos_ in self.pos:
                    word_count[token.lemma_] += 1
                    word_rating[token.lemma_].append(self.ratings[index])

        word_color = {word: self.getColor(
            ratings)[1] for word, ratings in word_rating.items()}
        word_sentiment = {word: self.getColor(
            ratings)[0] for word, ratings in word_rating.items()}

        return word_count, word_color, word_sentiment

    def getColor(self, ratings):
        """Generates sentiment color from the mean of ratings in which the word exists

        Arguments:
            ratings {list[float]} -- list of ratings in which the word exists

        Returns:
            str -- hex color of rating
        """
        float_rating = np.around(np.mean(ratings), 2)
        mean_rating = int(float_rating)
        return float_rating, self.color_range[mean_rating - 1]
