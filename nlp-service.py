from flask import Flask
from flask_cors import CORS
from flask import request
import json
from similarity import get_similarities
from hugginface_summarize import get_summaries

app = Flask(__name__)
CORS(app)

@app.route('/nlp-service/similarity', methods=['POST'])
def get_similarity():
    body = json.loads(request.data)

    data = get_similarities(body["source"], body["targets"])
    return { 'data': data }

@app.route('/nlp-service/summary', methods=['POST'])
def get_summary():
    body = json.loads(request.data)

    data = get_summaries(body["sources"])
    return { 'data': data }

print("NLP service started 🟣")