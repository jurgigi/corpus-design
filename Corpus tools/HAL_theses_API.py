
import requests

QUERY = 'bioinformatique OR bioinformatics OR bio-informatique'

# construct the API request URL
url = f'https://api.archives-ouvertes.fr/search/tel/?q={QUERY}&rows=1000&wt=json'

# send the API request
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
	# parse the response JSON and extract the list of documents
	data = response.json()
	docs = data['response']['docs']
	
	with open('', 'w') as f:
			for doc in docs:
				f.write(str(doc) + '\n')
				
	print('Results saved.')

	
else:
	print('Error: API request failed')
	
