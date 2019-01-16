from flask import Flask, jsonify, request
from text_classifier import TextClassifier
import json
import sys
import os

clf = None
print("Reading data...")
try:
  filename = os.path.join(os.path.dirname(__file__), 'data/dictionary-small.json')
  with open(filename) as f:
    print ("Parsing data...")
    data = json.load(f)
    print ("Creating classifier...")
    clf = TextClassifier(data)
except EnvironmentError as e:
  print ('ERROR reading data: {}'.format(e), file=sys.stderr)
print("Launching web app...")
app.run()

app = Flask(__name__)

@app.route('/')
def hello():
  return  "Hello!"

@app.route('/api/classify')
def classify():
    if 'text' in request.args:
      prediction = clf.classify(request.args['text'])
      return jsonify({
        'message': {'prediction': prediction},
        })
    else:
      resp = jsonify({'message': "'text' was not found in request arguments."})
      resp.status_code = 400
      return resp

# if __name__ == '__main__':