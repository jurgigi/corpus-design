#!/usr/bin/env python3

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def sentiment_analysis_vader(text):
	sia = SentimentIntensityAnalyzer()
	sentiment_scores = sia.polarity_scores(text)
	return sentiment_scores

def sentiment_analysis_textblob(text):
	blob = TextBlob(text)
	sentiment = blob.sentiment
	return sentiment

# Sample text
text = """ 

"""

# Perform sentiment analysis
sentiment_vader = sentiment_analysis_vader(text)
sentiment_textblob = sentiment_analysis_textblob(text)

# Print the sentiment scores
print("Sentiment scores:")
for score_type, score_value in sentiment_vader.items():
	print(f"{score_type}: {score_value:.2f}")
	
print(f"Polarity: {sentiment_textblob.polarity:.2f}")
print(f"Subjectivity: {sentiment_textblob.subjectivity:.2f}")