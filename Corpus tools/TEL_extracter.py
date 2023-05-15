
import re

# define the regular expression pattern to search for
pattern = r'tel-\d{8}'

# open the input and output files
with open('', 'r') as input_file, open('', 'w') as output_file:
	num_matches = 0
	
	for line in input_file:
		match = re.search(pattern, line)
		
		# if a match is found, write it to the output file
		if match:
			output_file.write(match.group(0) + '\n')
			num_matches += 1
		
		# print the total number of matches
		print(f'Total matches found: {num_matches}')
			
print('Done.')
