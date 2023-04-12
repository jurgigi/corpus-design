#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import csv

def scrap_url(url):
	# Make a GET request to the URL and get the HTML content
	response = requests.get(url)
	html_content = response.text
	
	# Parse the HTML content using BeautifulSoup
	soup = BeautifulSoup(html_content, 'html.parser')
	
	# Find all paragraphs in the HTML document
	all_paragraphs = soup.find_all('p')
	
	# Find the indexes of the paragraphs that contain each of the two separate words
	keywords1 = 'Résumé'
	keywords2 = 'Abstract'
	matching_indexes1 = [index for index, paragraph in enumerate(all_paragraphs) if keywords1 in paragraph.text]
	matching_indexes2 = [index for index, paragraph in enumerate(all_paragraphs) if keywords2 in paragraph.text]
	
	# Extract the paragraphs that follow the matching indexes for each word
	paragraphs1 = []
	for index in matching_indexes1:
		next_nonempty = all_paragraphs[index+1]
		while not next_nonempty.text.strip():
			index += 1
			next_nonempty = all_paragraphs[index+1]
		if len(next_nonempty.text.split()) >= 10:
			paragraphs1.append(next_nonempty.text)
			
	paragraphs2 = []
	for index in matching_indexes2:
		next_nonempty = all_paragraphs[index+1]
		while not next_nonempty.text.strip():
			index += 1
			next_nonempty = all_paragraphs[index+1]
		if len(next_nonempty.text.split()) >= 10:
			paragraphs2.append(next_nonempty.text)
			
	# Return the extracted abstract and resume text as a tuple
	return (' '.join(paragraphs2), ' '.join(paragraphs1))

	
with open('/parallel_abstracts.csv', 'w', newline='') as f1:
	writer = csv.writer(f1, quoting=csv.QUOTE_ALL, quotechar='"')
	
	with open('/Users/jurgigiraud/Documents/articles.csv', 'r', newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[2] == '10.1051':
				# 1. convert each DOI into URLs by adding "http://doi.org/" before each DOI
				url1 = "https://doi.org/" + row[1]
				
				# 2. Extract the content (i.e., abstract and resume)
				abs, res = scrap_url(url1)
				
				# 3. Write the extracted data to the output file
				writer.writerow([row[0], row[1], row[2], abs, res])
				
