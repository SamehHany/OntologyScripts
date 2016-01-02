import sys
import os
import commands
from subprocess import call

if os.path.isdir(sys.argv[1]):
	files = os.listdir(sys.argv[1])
	files_full_path = []
	for i in range(len(files)):
		files_full_path.append(sys.argv[1] + '/' + files[i])
else:
	files = [sys.argv[1]]
	files_full_path = [sys.argv[1]]

data_path = 'property-data/'
for file_full_path, fl in zip(files_full_path, files):
	call(["./ontop", "query", "-m", "input-files/movieontology.obda", "-t",
	#call(["./ontop", "query", "-m", "movieontology-sample.obda", "-t",
	"movieontology-instances.owl", "-q", file_full_path, "-o", data_path +
	fl[:-2] + ".csv"])
