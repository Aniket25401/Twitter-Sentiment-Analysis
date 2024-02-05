from flask import Flask, render_template, request
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

app = Flask(__name__)

# Load the pre-trained model and vectorizer
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Define Porter Stemmer
port_stem = PorterStemmer()

def preprocess_tweet(tweet, port_stem):
    # Perform the same preprocessing steps as in your training code
    stemmed_content = re.sub('[^a-zA-Z]',' ',tweet)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)

    return stemmed_content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        tweet = request.form['tweet']

        # Preprocess the input tweet
        processed_tweet = preprocess_tweet(tweet, port_stem)

        # Vectorize the tweet using the pre-trained vectorizer
        input_data = loaded_vectorizer.transform([processed_tweet])

        # Make prediction using the loaded model
        prediction = loaded_model.predict(input_data)

        # Determine the sentiment
        sentiment = 'Positive' if prediction[0] == 1 else 'Negative'

        return render_template('result.html', tweet=tweet, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
