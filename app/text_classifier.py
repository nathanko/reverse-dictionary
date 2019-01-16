import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

def LemmatizeTokenizer(text):
  punctTranslateDict = dict((ord(punc), None) for punc in string.punctuation)
  text = text.lower().translate(punctTranslateDict)
  tokens = nltk.word_tokenize(text)
  lemmer = nltk.stem.WordNetLemmatizer()
  return [lemmer.lemmatize(token) for token in tokens]

class TextClassifier:

  entries = []
  values = []

  def __init__(self, data):
    dataX = []
    dataY = []
    for entry, definition in data.items():
      # print(dataX, dataY)
      dataX = dataX + [definition]
      dataY = dataY + [entry]
    self.entries = dataY
    self.values = dataX

  def classify(self, question):
    tfidfVec = TfidfVectorizer(tokenizer=LemmatizeTokenizer, stop_words=None)
    tfidf = tfidfVec.fit_transform(self.values + [question])
    vals = cosine_similarity(tfidf[-1], tfidf)
    # print(self.values + [question])
    # print(vals)
    # print(vals.argsort()[0])
    # return top numResults results in desc order
    numResults = 4
    numResults = min(numResults, len(self.entries))
    indices = vals.argsort()[0][-numResults-2:-2][::-1]
    return [{
      "entry" : self.entries[idx],
      "definition": self.values[idx],
      "cosine": vals[0][idx]
    } for idx in indices]