# !pip install sentence_transformers
import json
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance
from remove_stop_words import remove

def get_similarity(model, source, target):
    sentences = [remove(source), remove(target)]
    embeddings = model.encode(sentences)
    return 1 - distance.cosine(embeddings[0], embeddings[1])/2

def get_similarities(source, targets):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    similarities = []

    for i in range(len(targets)):
        similarity = get_similarity(model, source, targets[i])
        similarities.append(similarity)

    return { 'similarities': similarities, 'source': source }