# Twitter Sentiment Analysis

Twitter Sentiment Analysis is a data analytics project that involves analyzing a 
dataset of tweets to determine the sentiment expressed in each tweet. 
It includes a Flask web application for sentiment prediction.


## Dataset
The dataset used for training the sentiment analysis model is available on Kaggle. You can download it from the following link:

[Kaggle Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

To use this dataset in your project:
1. Download the dataset from the provided Kaggle link.
2. Extract the compressed file (e.g., sentiment140.zip).

## Usage
1. Training the Model (Google Colab)
The model training code is available in the Twitter Sentiment Analysis.ipynb notebook.
To use Google Colab for training, open the notebook and follow the instructions.
Note: Ensure you have the Kaggle API key (kaggle.json) for downloading the dataset.

2. Flask Web Application
Run the Flask app:
bash:
python app.py
Access the web application at http://localhost:5000 in your web browser.

## File Structure
Twitter Sentiment Analysis.ipynb: Jupyter notebook for data preprocessing and model training.
app.py: Flask web application for sentiment prediction.
templates/: HTML templates for the web application.
static/: Static files (e.g., CSS, JS).

Acknowledgments
Dataset: Sentiment140 on Kaggle.
Flask: Flask Documentation
