#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
import csv

# define the regular expression pattern to search for
pattern = r'tel-\d{8}'

# create an empty list to hold the abstracts
abstracts = []

# open the input file
with open('/Users/jurgigiraud/Documents/v3_new_tel_output.txt', 'r') as input_file:
	# loop through each line in the input file
	for line in input_file:
		# search for the pattern in the line using regular expressions
		match = re.search(pattern, line)
		
		# if a match is found, construct the URL and send a request to the webpage
		if match:
			url = f'https://theses.hal.science/{match.group(0)}/Abstract'
			response = requests.get(url)
			
			# check if the request was successful
			if response.status_code == 200:
				# parse the HTML content using BeautifulSoup
				soup = BeautifulSoup(response.content, 'html.parser')
				
				# extract the text from the <abstract> tags
				abstract_en = soup.find('abstract', {'xml:lang': 'en'})
				abstract_fr = soup.find('abstract', {'xml:lang': 'fr'})
				
				# add the abstracts to the list
				abstracts.append([match.group(0), abstract_fr.get_text() if abstract_fr else '', abstract_en.get_text() if abstract_en else ''])
			else:
				print(f'Error {response.status_code} while accessing {url}')
				
# save the abstracts into a CSV file
with open('/Users/jurgigiraud/Documents/v3_new_abstracts.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['tel- fragment', 'French abstract', 'English abstract'])
	for abstract in abstracts:
		writer.writerow(abstract)
		
print('Done.')