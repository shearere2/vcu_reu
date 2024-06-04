import pandas as pd
import nltk
from nltk.sentiment import sentiment_analyzer
from nltk import classify
from nltk.tokenize.api import StringTokenizer

def analyze_sentiment(sentence:str):
    nltk.download('sentiwordnet')
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    from nltk.corpus import wordnet as wn
    from nltk.corpus import sentiwordnet as swn
    list(swn.senti_synsets('slow'))
    sentence=sentence
    from nltk.tag import pos_tag
    token = nltk.word_tokenize(sentence)
    after_tagging = nltk.pos_tag(token)
    print (token)
    print (after_tagging)
    def penn_to_wn(tag):
        """
        Convert between the PennTreebank tags to simple Wordnet tags
        """
        if tag.startswith('J'):
            return wn.ADJ
        elif tag.startswith('N'):
            return wn.NOUN
        elif tag.startswith('R'):
            return wn.ADV
        elif tag.startswith('V'):
            return wn.VERB
        return None
    sentiment = 0.0
    tokens_count = 0
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    for word, tag in after_tagging:
                wn_tag = penn_to_wn(tag)
                if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                    continue
    
                lemma = lemmatizer.lemmatize(word, pos=wn_tag)
                if not lemma:
                    continue
    
                synsets = wn.synsets(lemma, pos=wn_tag)
                if not synsets:
                    continue
    
                # Take the first sense, the most common
                synset = synsets[0]
                swn_synset = swn.senti_synset(synset.name())
                print(swn_synset)
    
                sentiment += swn_synset.pos_score() - swn_synset.neg_score()
                tokens_count += 1
    print (sentiment)

if __name__ == "__main__":
    sentence = '''It is hard to think how it is NOT affecting my mental health. Overall 
            I find myself feeling more anxiety, depression, and grief. I worry about
            pretty much everything, but especially my family and friends, as well as
            potential financial collapse & what that means for all of us, and my own
            job prospects for academia this fall & how that impacts our dream to start
            a family. As a grad student I often base my self-worth and how I feel about
            myself on my productivity (I know, not healthy!), and I'm not being as
            "productive" anymore, so I struggle with living up to high expectations as
            a grad student. And I'm not sure I should care, because my health and our
            world is more important. So also just confused and making it day by day.'''
    analyze_sentiment(sentence=sentence)