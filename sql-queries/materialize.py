import sys
import psycopg2
import traceback
from sets import Set

def positiveHash(x):
	h = hash(x)
	return h if h >= 0 else -h

schema = 'materialized'
infile = 'all-queries'
outfile = 'materialize-queries.sql'
try:
	conn = psycopg2.connect("dbname='postgres' user='sameh' host='localhost' password=''")
	cur = conn.cursor()
	#cur.execute("""select * from title where title = 'X-Men';""")
	#rows = cur.fetchall()
	fin = open(infile, 'r')
	fout = open(outfile, 'w')
	#line = fin.readline()
	
	
	#for line in fin:
	#	sql += line
	line = fin.readline()
	
	ids = Set()
	while line != '':
		alias = line[:-2]
		print "Materializing " + alias + "..."
		sql = ''
		line = fin.readline()
		while line != '' and line != '\n':
			sql += line
			line = fin.readline()
		h = str(positiveHash(alias))
		if h in ids:
			print "conflict"
		ids.add(h)
		#print alias + ": " + str(h)
		#print sql
		query = 'CREATE TABLE ' + schema + '.t' + h + ' AS\n' + sql;
		fout.write('-- ' + alias + ':\n' + query + '\n')
		#print query
		cur.execute(query)
		while line == '\n' and line != '':
			line = fin.readline()	
	fin.close()
	fout.close()
except:
	traceback.print_exc(file=sys.stdout)
	print "Unable to connect to the database"

