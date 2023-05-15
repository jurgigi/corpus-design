#!/usr/bin/env python3

import re

# define the regular expression pattern to search for
pattern = r'tel-\d{8}'

# open the input and output files
with open('/Users/jurgigiraud/Documents/results.txt', 'r') as input_file, open('/Users/jurgigiraud/Documents/v3_tel_output.txt', 'w') as output_file:
	# loop through each line in the input file
	num_matches = 0
	
	for line in input_file:
		# search for the pattern in the line using regular expressions
		match = re.search(pattern, line)
		
		# if a match is found, write it to the output file
		if match:
			output_file.write(match.group(0) + '\n')
			num_matches += 1
		
		# print the total number of matches
		print(f'Total matches found: {num_matches}')
			
print('Done.')
