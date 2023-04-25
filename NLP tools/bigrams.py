#!/usr/bin/env python3
import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
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

# Find bigram collocations
bigram_measures = BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(filtered_tokens)
finder.apply_freq_filter(1)  # Only bigrams that appear at least once

# Top N bigrams based on a chosen measure, e.g., Pointwise Mutual Information (PMI)
N = 10
top_n_bigrams = finder.nbest(bigram_measures.pmi, N)
print("Top", N, "bigrams:")
print(top_n_bigrams)

# Print bigrams and their frequencies
for bigram in top_n_bigrams:
	frequency = finder.ngram_fd[bigram]
	print(f"{bigram}: {frequency} times")