import sys
import os
import commands
import subprocess
from time import time

queries_path = 'input-files/movieontology-single-queries/'
query_files = os.listdir(queries_path)

dump_file = 'dump'
try:
	for fl in query_files:
		full_path = queries_path + fl.replace(' ', '\\ ')
		#print fl
		start = time()
		#subprocess.call(["./ontop", "query", "-m", "input-files/movieontology.obda", "-t",
		#"movieontology-instances.owl", "-q", full_path], shell=True)
		#os.system("./ontop query -m input-files/movieontology.obda -t \
		#os.system("./ontop query -m graph.obda -t \
		#movieontology-instances.owl -q " + full_path + " > " + dump_file)
		#"movieontology-instances.owl", "-q", full_path)
		subprocess.check_output(["./ontop", "query", "-m",
		"input-files/movieontology.obda" ,"-t",
		"movieontology-instances.owl", "-q", full_path])
		elapsed_time = time() - start
		print fl[:-2].replace('_', ' ').replace('#', '(').replace('^',')').strip() + ": " + str(elapsed_time)
except:
	print "Exiting..."
os.remove(dump_file)
