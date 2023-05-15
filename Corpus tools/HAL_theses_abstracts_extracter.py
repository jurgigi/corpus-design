
import re
import requests
from bs4 import BeautifulSoup
import csv

pattern = r'tel-\d{8}'
abstracts = []

# open the input file
with open('', 'r') as input_file:
	for line in input_file:
		match = re.search(pattern, line)
		
		if match:
			url = f'https://theses.hal.science/{match.group(0)}/Abstract'
			response = requests.get(url)
			
			if response.status_code == 200:
				soup = BeautifulSoup(response.content, 'html.parser')
				
				abstract_en = soup.find('abstract', {'xml:lang': 'en'})
				abstract_fr = soup.find('abstract', {'xml:lang': 'fr'})
				
				abstracts.append([match.group(0), abstract_fr.get_text() if abstract_fr else '', abstract_en.get_text() if abstract_en else ''])
			else:
				print(f'Error {response.status_code} while accessing {url}')
				
# save the abstracts into a CSV file
with open('', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['tel- fragment', 'French abstract', 'English abstract'])
	for abstract in abstracts:
		writer.writerow(abstract)
		
print('Done.')
