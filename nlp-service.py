from flask import Flask
from flask_cors import CORS
from flask import request
import json
import os
# from similarity import get_similarities
# from hugginface_summarize import get_summaries
from speech_recognition import recognize

app = Flask(__name__)
CORS(app)

# @app.route('/nlp-service/similarity', methods=['POST'])
# def get_similarity():
#     body = json.loads(request.data)

#     data = get_similarities(body["source"], body["targets"])
#     return { 'data': data }

# @app.route('/nlp-service/summary', methods=['POST'])
# def get_summary():
#     body = json.loads(request.data)

#     data = get_summaries(body["sources"])
#     return { 'data': data }


@app.route("/nlp-service/transcript", methods=['POST'])
def get_transcript():
    content = request.files['sample'].read()

    with open(os.path.abspath(f'backend/audios/filename.wav'), 'wb') as f:
        f.write(content)

    file_path = os.path.abspath(f'backend/audios/filename.wav')
    data = recognize([file_path])

    return {'data': data}


print("NLP service started 🟣")
