#!/usr/bin/env python3

import nltk
from nltk.collocations import TrigramAssocMeasures, TrigramCollocationFinder
from nltk.corpus import stopwords

text = """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human (natural) languages. It is used in various applications, such as text analysis, sentiment analysis, language translation, and speech recognition. The history of natural language processing generally started in the 1950s, although work can be found from earlier periods. In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence.
"""
					
# Tokenize the text
tokens = nltk.word_tokenize(text)

# Count the number of words in the text
word_count = len(tokens)
print(f"Total number of words in the text: {word_count}")

# Remove stopwords and non-alphabetic tokens
stopwords = set(stopwords.words('english'))
filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords]

# Find trigram collocations
trigram_measures = TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(filtered_tokens)
finder.apply_freq_filter(1)  # Only trigrams that appear at least once

# Top N trigrams based on a chosen measure, e.g., Pointwise Mutual Information (PMI)
N = 10
top_n_trigrams = finder.nbest(trigram_measures.pmi, N)
print("Top", N, "trigrams:")

# Print trigrams and their frequencies
for trigram in top_n_trigrams:
		frequency = finder.ngram_fd[trigram]
		print(f"{trigram}: {frequency} times")