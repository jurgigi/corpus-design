#!/usr/bin/env python3

import spacy

def named_entity_recognition(text, model):
	doc = model(text)
	entities = [(ent.text, ent.label_) for ent in doc.ents]
	return entities

# Load the spaCy model (you need to have the 'en_core_web_sm' model installed)
spacy_model = spacy.load('en_core_web_sm')

# Sample text
text = """
"""

# Perform Named Entity Recognition
entities = named_entity_recognition(text, spacy_model)

print("Named entities:")
for entity, label in entities:
	print(f"{entity} ({label})")