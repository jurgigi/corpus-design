#!/usr/bin/env python3

import spacy
import nltk
from nltk import FreqDist
from nltk.util import ngrams
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import stopwords
from collections import defaultdict

nlp = spacy.load('fr_core_news_sm')

def bold_text(text):
	return f"\033[1m{text}\033[0m"

class KWICTool:
	def __init__(self, text):
		self.text = text
		self.tokens = nltk.word_tokenize(text, language='french')
		self.pos_tags = [(token.text, token.pos_) for token in nlp(text)]
		self.stopwords = set(stopwords.words('french'))
		self.bigram_measures = BigramAssocMeasures()
		self.finder = BigramCollocationFinder.from_words(self.tokens)
		
		
	def search_keyword(self, keywords, window_size=5, filter_pos=None):
		if filter_pos:
			tokens = [token for token, pos in self.pos_tags if pos in filter_pos]
		else:
			tokens = self.tokens
			
		keywords = keywords.split()
		wildcard = '_WILDCARD_'
		keywords = [word if word != '*' else wildcard for word in keywords]
		
		keyword_ngrams = ngrams(tokens, len(keywords))
		
		kwic_results = []
		for idx, ngram in enumerate(keyword_ngrams):
			if all(k == t or k == wildcard for k, t in zip(keywords, ngram)):
				left = ' '.join(tokens[max(0, idx - window_size):idx])
				right = ' '.join(tokens[idx + len(keywords):idx + len(keywords) + window_size])
				kwic_results.append((left, ' '.join(ngram), right))
				
		return kwic_results
	
	def keyword_frequency(self, keyword):
			keyword = keyword.split()
			wildcard = '_WILDCARD_'
			keyword = [k if k != '*' else wildcard for k in keyword]
			ngram_size = len(keyword)
		
			ngram_freq = FreqDist(ngrams(self.tokens, ngram_size))
		
			return sum(
				count for ngram, count in ngram_freq.items()
				if all(k == t or k == wildcard for k, t in zip(keyword, ngram))
			)
	
	def search_by_pos(self, pos_tags):
			return [token for token, pos in self.pos_tags if pos in pos_tags]
	
	def search_pos_pattern(self, pos_pattern, window_size=5):
			wildcard = '_WILDCARD_'
			pos_pattern = pos_pattern.split()
			pos_pattern = [pos if pos != '*' else wildcard for pos in pos_pattern]
		
			pos_ngrams = ngrams(self.pos_tags, len(pos_pattern))
		
			kwic_results = []
			for idx, ngram in enumerate(pos_ngrams):
				if all(p == pos or p == wildcard for p, (token, pos) in zip(pos_pattern, ngram)):
					left = ' '.join(token for token, pos in self.pos_tags[max(0, idx - window_size):idx])
					right = ' '.join(token for token, pos in self.pos_tags[idx + len(pos_pattern):idx + len(pos_pattern) + window_size])
					key = ' '.join(token for token, pos in ngram)
					kwic_results.append((left, key, right))
					
			return kwic_results
	
	def pos_pattern_frequency(self, pos_pattern):
			pos_pattern = pos_pattern.split()
			wildcard = '_WILDCARD_'
			pos_pattern = [pos if pos != '*' else wildcard for pos in pos_pattern]
			ngram_size = len(pos_pattern)
		
			pos_ngram_freq = FreqDist(ngrams(self.pos_tags, ngram_size))
		
			return sum(
				count for ngram, count in pos_ngram_freq.items()
				if all(p == pos or p == wildcard for p, (token, pos) in zip(pos_pattern, ngram))
			)
			
if __name__ == "__main__":
	sample_text = """Le CRAN (pour Comprehensive R Archive Network) est évidemment LE répertoire de packages R. Il centralise bon nombre d'entre eux, touchant à des domaines variés : statistiques, physique, mathématiques, psychologie, écologie, visualisations, machine learning, cartographie, ..., et bioinformatique. Cependant à avoir autant de variété, on s'y perd. C'est pourquoi Bioconductor a en partie été créé. Bioconductor c'est un répertoire alternatif de packages R spécifiquement dédié à la bioinformatique créé en 2002. Akira vous le présentait en 2012 sur le blog, et huit ans plus tard, force est de constater que le projet tient toujours, et même prend de l'ampleur (cf. Figure 1). La vocation est restée la même : regrouper sous une même bannière des packages spécifiques à la bioinformatique, et notamment à l'analyse et la compréhension de données de séquençage haut débit.
	
	"""
	
	kwic_tool = KWICTool(sample_text)
	
	keywords = " "  # Use space-separated keywords and * for unknown words
	window_size = 5
	filter_pos = {}  # To search for nouns, change this according to your requirement
	
	results = kwic_tool.search_keyword(keywords, window_size, filter_pos)
	frequency = kwic_tool.keyword_frequency(keywords)
	
	print("KWIC Results:")
	for left, key, right in results:
		print(f"{left} | {bold_text(key)} | {right}")
		
	print(f"\nKeyword frequency: {frequency}")
	
	pos_pattern = " "  # Use space-separated POS tags and * for unknown POS
	window_size = 5
	
	pos_results = kwic_tool.search_pos_pattern(pos_pattern, window_size)
	pos_pattern_frequency = kwic_tool.pos_pattern_frequency(pos_pattern)
	
	print("\nPOS Pattern KWIC Results:")
	for left, key, right in pos_results:
		print(f"{left} | {bold_text(key)} | {right}")
		
	print(f"\nPOS Pattern frequency: {pos_pattern_frequency}")