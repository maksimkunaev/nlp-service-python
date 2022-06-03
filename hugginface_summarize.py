from transformers import pipeline
import sys
import json

def summarize(classifier, text):
    return classifier(text)[0]['summary_text']

def get_summaries(sources):
    classifier = pipeline("summarization")
    summaries = []

    for i in range(len(sources)):
        summary = summarize(classifier, sources[i])
        summaries.append(summary)

    return summaries