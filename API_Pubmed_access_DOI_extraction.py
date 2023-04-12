#!/usr/bin/env python3

from Bio import Entrez
import csv 

Entrez.email = "example@email.com"

def search_articles(query, retmax):
	handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax)
	record = Entrez.read(handle)
	return record["IdList"]

def get_article_info(article_id):
	handle = Entrez.efetch(db='pubmed', id=article_id, retmode='xml')
	article = Entrez.read(handle)['PubmedArticle'][0]
	title = article['MedlineCitation']['Article']['ArticleTitle']
	
	doi = None
	for id in article['PubmedData']['ArticleIdList']:
		if id.attributes['IdType'] == 'doi':
			doi = id.title()
			break
		
	return title, doi

def save_to_txt(articles, file_name):
	with open(file_name, 'w') as f:
		for title, doi in articles:
			f.write(f"Title: {title}\nDOI: {doi}\n\n")
			
query = '(((bioinformatics) OR (computational biology)) AND (French[Language]))'
retmax = 300

article_ids = search_articles(query, retmax)
articles = [get_article_info(article_id) for article_id in article_ids]
filtered_articles = []
for t, d in articles: 
	if d is not None: 
		publisher = d.split('/')[0]
		filtered_articles.append([t, d, publisher])



with open('/articles.csv', 'w') as f: 
	csv.writer(f).writerows(filtered_articles)
