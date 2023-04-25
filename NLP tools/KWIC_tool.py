#!/usr/bin/env python3

import nltk
from nltk import FreqDist
from nltk.util import ngrams
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import stopwords
from collections import defaultdict


#def read_file(file_path):
#	with open(file_path, 'r', encoding='utf-8') as file:
#		return file.read()
	

#def write_results_to_file(file_path, results, title):
#	with open(file_path, 'w', encoding='utf-8') as file:
#		file.write(f"{title}\n")
#		for left, key, right in results:
#			file.write(f"{left} | {key} | {right}\n")
#		file.write("\n")

class KWICTool:
	def __init__(self, text):
		self.text = text
		self.tokens = nltk.word_tokenize(text)
		self.pos_tags = nltk.pos_tag(self.tokens)
		self.stopwords = set(stopwords.words('english'))
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
		file_path = '' #insert path 
#		sample_text = read_file(file_path)
		sample_text= """ Online, offline and DIY corpus software tools can play an important role at every stage of a corpus linguistics project. At the corpus design and development stage, software tools can assist in the collection of raw data that goes into the corpus. For example, there are numerous general-purpose online and offline tools as well as DIY tools that can help researchers convert raw data in the form of audio recordings, webpages, scanned books, PDF/Word files and other data formats into a form more suitable for corpus analysis. For example, many online PDF-to-text converters can be easily found through a simple Internet search. Care should be taken when using these, however, as it can be unclear if the site will store and use the data for its own purposes. They may also only convert a single file at a time, which is inappropriate for many corpus building tasks that require huge numbers of files to be converted. One alternative is AntFileConverter,12 which is an offline tool that can batch-convert PDF and Word files into a text format without any restriction on the number of files being processed."""

		kwic_tool = KWICTool(sample_text)
		
		keywords = " "  # Use space-separated keywords and * for unknown words
		window_size = 5
		filter_pos = {}  # To search for specific POS, change this according to your requirement
		
		results = kwic_tool.search_keyword(keywords, window_size, filter_pos)
		frequency = kwic_tool.keyword_frequency(keywords)
		
		print("KWIC Results:")
		for left, key, right in results:
			print(f"{left} | {key} | {right}")
			
		print(f"\nKeyword frequency: {frequency}")
		
		pos_pattern = " "  # Use space-separated POS tags and * for unknown POS
		window_size = 5
		
		pos_results = kwic_tool.search_pos_pattern(pos_pattern, window_size)
		pos_pattern_frequency = kwic_tool.pos_pattern_frequency(pos_pattern)
		
		print("\nPOS Pattern KWIC Results:")
		for left, key, right in pos_results:
			print(f"{left} | {key} | {right}")
			
		print(f"\nPOS Pattern frequency: {pos_pattern_frequency}")
		
#		output_file_path = ''
	
#			# Write the KWIC Results to the output file
#		write_results_to_file(output_file_path, results, "KWIC Results")
#	
#			# Append the POS Pattern KWIC Results to the output file
#		with open(output_file_path, 'a', encoding='utf-8') as file:
#				file.write(f"POS Pattern KWIC Results:\n")
#				for left, key, right in pos_results:
#					file.write(f"{left} | {key} | {right}\n")
#				file.write("\n")
#				file.write(f"Keyword frequency: {frequency}\n")
#				file.write(f"POS Pattern frequency: {pos_pattern_frequency}\n")