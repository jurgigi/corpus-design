#!/usr/bin/env python3
import nltk
import string
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

text = """ Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human (natural) languages. It is used in various applications, such as text analysis, sentiment analysis, language translation, and speech recognition. The history of natural language processing generally started in the 1950s, although work can be found from earlier periods. In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence.
"""
lower_text = text.lower()

tokens = []
for token in re.findall(r'\b\w[\w-]*\b', lower_text):
	# Check if token contains hyphen
	if '-' in token:
		# If token contains hyphen, add it to the tokens
		tokens.append(token)
	else:
		# If token does not contain hyphen, remove all punctuations and add to the tokens
		tokens.append(re.sub(r'[^\w\s-]', '', token))

stems = []
for token in tokens:
	stem = stemmer.stem(token)
	stems.append(stem)
	
lemmas = []
for token in tokens:
	lemma = lemmatizer.lemmatize(token)
	lemmas.append(lemma)
	

print(tokens)
print(stems)
print(lemmas)

pos_text = text
pos_tokens = nltk.word_tokenize(pos_text)	
pos_tags = nltk.pos_tag(pos_tokens)

#print(pos_tags)

pos_of_interest = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]

#pos_of_interest = []
#filtered_tokens = [tk for tk in pos_tags if tk[1] in pos_of_interest]

filtered_tokens = []
for tk_pos in pos_tags:
	if (tk_pos[1] in pos_of_interest):
		filtered_tokens.append(tk_pos)

print(filtered_tokens)
	