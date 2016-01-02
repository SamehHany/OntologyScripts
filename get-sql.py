import sys
import os
import commands
import subprocess
from time import time
import re
import traceback


def lineIsSPARQL(line):
	return '?' in line or '$' in line

def getFirstLine(string):
	index = getIndexOfEndOfFirstLine(string)
	return string[:index]

def skipFirstLine(string):
	index = getIndexOfEndOfFirstLine(string)
	return string[index+1:]

def getIndexOfEndOfFirstLine(string):
	l = len(string)
	i = 0
	while i < l:
		ch = string[i]
		if ch == '\n':
			return i
		i+=1

queries_path = 'input-files/movieontology-single-queries/'
query_files = os.listdir(queries_path)

#dump_file = 'dump'
try:
	for fl in query_files:
		full_path = queries_path + fl.replace(' ', '\\ ')
		start = time()
		out = subprocess.check_output(["./ontop", "query", "-m",
		#"input-files/movieontology.obda" ,"-t",
		"graph.obda" ,"-t",
		"movieontology-instances.owl", "-q", full_path])
		elapsed_time = time() - start
		
		index = out.find('SELECT')
		out = out[index:]
		line = getFirstLine(out)
		while lineIsSPARQL(line):
			out = skipFirstLine(out)
			index = out.find('SELECT')
			out = out[index:]
			line = getFirstLine(out)
		#print out
		match = re.search('[0-9]+:[0-9]+:[0-9]+(\.[0-9]+)?\s+\|-DEBUG in i\.u\.k\.o\.o\.core\.QuestStatement - Executing the SQL query and get the result\.\.\.', out)
		
		sql = out[:match.start()] + ';' if match is not None else ''
		
		print fl[:-2].replace('_', ' ').replace('#', '(').replace('^',')').strip() + ":"
		print sql
		print
except:
	traceback.print_exc(file=sys.stdout)
	print "Exiting..."
#os.remove(dump_file)
