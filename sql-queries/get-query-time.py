import sys
import traceback

aliasfile = 'query-alias.txt'
infile = sys.argv[1]
outfile = sys.argv[2]

falias = open(aliasfile, 'r')
fin = open(infile, 'r')
fout = open(outfile, 'w')

start_of_string = 'LOG:  duration: '
offset = len(start_of_string)
for alias in falias:
	line = fin.readline()
	while line != '':
		if line.startswith(start_of_string):
			line = line[offset+1:]
			break
		line = fin.readline()
	if line == '':
		break
	time = float(line.split('ms')[0].strip())
	fout.write(alias[:-1] + ',' + str(time) + '\n')

falias.close()
fin.close()
fout.close()
