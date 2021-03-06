from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove(source):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(source)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    return " ".join(filtered_sentence)