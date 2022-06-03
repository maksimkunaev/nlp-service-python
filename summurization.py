import json
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    # tokens = [token.text for token in doc]
    word_frequencies = {}

    for word in doc:       
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text.lower() not in word_frequencies.keys():
                    word_frequencies[word.text.lower()] = 1
                else:
                    word_frequencies[word.text.lower()] += 1

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word.lower()]=word_frequencies[word.lower()]/max_frequency
    tokens_with_frequencies = []
    for word in doc:

        if word.text.lower() in word_frequencies.keys():
            # print(word_frequencies[word.text.lower()])
            tokens_with_frequencies.append({'token': word.text, 'score':  word_frequencies[word.text.lower()]})
        else:
            tokens_with_frequencies.append({'token': word.text, 'score': 0 })

    word_frequencies.pop('\n\n', None)
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    sentence_with_scores = []

    for sent in sentence_tokens:
        word_count = 0

        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                word_count += 1

                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
        if word_count > 0:
            sentence_scores[sent] += sentence_scores[sent]/word_count
        sentence_with_scores.append({'token': sent.text, 'score': sentence_scores[sent]})

    select_length = int(len(sentence_tokens)*per)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    # print(select_length)
    summary=''.join(final_summary)
    
    return sentence_with_scores