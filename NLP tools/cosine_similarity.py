#!/usr/bin/env python3

import numpy as np
import nltk
import os
from nltk.corpus import stopwords
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
from gensim.scripts.glove2word2vec import glove2word2vec

#def load_glove_model(glove_file):
	#return KeyedVectors.load_word2vec_format(glove_file, binary=False)

def load_glove_model(glove_file):
	word2vec_output_file = glove_file + '.word2vec'
	if not os.path.exists(word2vec_output_file):
		glove2word2vec(glove_file, word2vec_output_file)
	return KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

def text_vector(text, model):
	tokens = nltk.word_tokenize(text)
	tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords.words('english')]
	word_vectors = [model[word] for word in tokens if word in model]
	
	if not word_vectors:
		raise ValueError("No valid word vectors found in the input text.")
		
	return np.mean(word_vectors, axis=0)

def text_similarity(text1, text2, model):
	vec1 = text_vector(text1, model)
	vec2 = text_vector(text2, model)
	return cosine_similarity([vec1], [vec2])

# Load the GloVe model (you need to have the GloVe file, e.g., "glove.6B.100d.txt")
glove_model = load_glove_model(" ") #insert file path 

# Sample texts
text1 = "This is an example text for word embedding-based text analysis."
text2 = "This is another example text for comparison using word embeddings."

# Calculate text similarity using word embeddings
similarity = text_similarity(text1, text2, glove_model)

print(f"Cosine similarity: {similarity[0][0]:.2f}")