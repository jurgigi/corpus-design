#!/usr/bin/env python3

import nltk

def jaccard_similarity(text1, text2):
	# Tokenize the texts
	tokens1 = set(nltk.word_tokenize(text1))
	tokens2 = set(nltk.word_tokenize(text2))
	
	# Calculate the Jaccard similarity
	intersection = tokens1.intersection(tokens2)
	union = tokens1.union(tokens2)
	similarity = len(intersection) / len(union)
	
	return similarity

# Sample texts
text1 = ""
text2 = ""

# Calculate the Jaccard similarity between the texts
similarity = jaccard_similarity(text1, text2)

print(f"Jaccard similarity: {similarity:.2f}")
