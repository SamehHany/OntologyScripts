import sys
import os
import commands
from subprocess import call
import re

in_path = 'input-files/movieontology.q'
out_path = 'input-files/movieontology-single-queries/'

fin = open(in_path, 'r')

query = ''
name = ''
new_query = False
pattern = re.compile("\[.*\]")
inQuery = False
for line in fin:
	line_s = line.strip()
	if pattern.match(line_s):
		inQuery = True
		line_s = line_s.strip('[]')
		name = line_s.split('=')[1].strip().strip('\"');
	elif line_s is not '' and ']]' not in line_s and inQuery:
		query = query + line
	elif line_s is '' and inQuery:
		filepath = out_path + name.replace(' ', '_').replace('(','#').replace(')','^') + '.q'
		fout = open(filepath, 'w') 
		fout.write(query + '\n')
		fout.close()
		query = ''
		inQuery = False

fin.close()
