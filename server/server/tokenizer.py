from textblob import TextBlob, Word


class Tokenizer:

    # Returns a tagged version of the tokens
    @classmethod
    def tag(cls, tokens):
        sentence = TextBlob(tokens)
        print(sentence.tags)
        return sentence.tags

    # Returns the extracted noun phrase from the tokens
    @classmethod
    def noun_phrase(cls, tokens):
        sentence = TextBlob(tokens)
        return sentence.noun_phrases

    # Returns a tagged version of the lemmatized tokens
    @classmethod
    def lemmatize(cls, tokens):
        sentence = TextBlob(tokens)
        words = sentence.words
        lemmatized = ""
        for word in words:
            lemmatized += Word(word).lemmatize() + " "
        return lemmatized[:-1]

    # Returns a list of the noun-phrases, nouns, and adjectives
    @classmethod
    def noun_adj_extractor(cls, sentence):
        noun_adj = []
        tagged = Tokenizer.tag(sentence)
        noun_p = Tokenizer.noun_phrase(sentence)
        for np in noun_p:
            noun_adj.append(np)

        for word,pos in tagged:
            # check if the word is a noun or adjective
            if pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS" or pos =="JJ" or pos == "JJR" or pos == "JJS":
                noun_adj.append(word)
        # print(noun_adj)
        return noun_adj