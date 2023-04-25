#!/usr/bin/env python3

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample text and reference corpus
text = "This is an example text for keyword extraction. It demonstrates how to identify important words in a given text compared to a reference corpus."
reference_corpus = [
	"This is a document in the reference corpus. It contains some words that may also appear in the example text.",
	"This is another document in the reference corpus. It has a different set of words and phrases.",
	"The reference corpus contains multiple documents, and each document has its own set of unique words and phrases."
]

# Tokenize the text and remove stopwords
stopwords = set(stopwords.words('english'))
tokens = nltk.word_tokenize(text)
filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords]

# Combine the text and reference corpus
documents = [text] + reference_corpus

# Vectorize the documents using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# Extract keywords by sorting words based on their TF-IDF score in the text
feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix[0].toarray().flatten()
sorted_indices = tfidf_scores.argsort()[::-1]

# Print the top N keywords
N = 10
print(f"Top {N} keywords:")
for i in range(N):
	index = sorted_indices[i]
	keyword = feature_names[index]
	tfidf_score = tfidf_scores[index]
	print(f"{keyword}: {tfidf_score}")
	