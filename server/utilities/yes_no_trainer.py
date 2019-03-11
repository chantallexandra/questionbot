""""
    Building a Text Classification System using TextBlob
    https://textblob.readthedocs.io/en/dev/classifiers.html
"""

from textblob.classifiers import NaiveBayesClassifier

class PosOrNeg:
    def __init__(self):
        self.train = [
            ('y', 'pos'),
            ('yes','pos'),
            ('yea','pos'),
            ('i would love to', 'pos'),
            ('i would like to','pos'),
            ('that is correct', 'pos'),
            ('i want that', 'pos'),
            ('positive','pos'),
            ('true', 'pos'),
            ('i do', 'pos'),
            ('i did', 'pos'),
            ('i did mean that', 'pos'),
            ('yes, that is correct', 'pos'),
            ('n', 'neg'),
            ('no','neg'),
            ('negative', 'neg'),
            ('that is incorrect', 'neg'),
            ('i dont want to do that', 'neg'),
            ('no, that is not correct', 'neg'),
            ('i don\' want to do that', 'neg'),
            ('don\'t use that', 'neg'),
            ('dont use that', 'neg'),
            ('that is wrong', 'neg'),
            ('that is not right', 'neg'),
            ('false', 'neg'),
            ('i would not like to use those words', 'neg'),
            ('i didn\'t mean that', 'neg'),
            ('i didn\'t', 'neg'),
            ('i don\'t like that one', 'neg'),
        ]
        self.cl = NaiveBayesClassifier(self.train)

    def classify(self, sentence):
        return self.cl.classify(sentence)

test = [
    ('i do', 'pos'),
    ('i did', 'pos'),
    ('i didn\'t', 'neg'),
    ('i don\'t like that one', 'neg'),
    ('yes, that is correct', 'pos'),
    ('i didn\'t mean that' , 'neg')
]

