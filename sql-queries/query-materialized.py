import sys
import traceback

def positiveHash(x):
	h = hash(x)
	return h if h >= 0 else -h

aliasfile = 'query-alias.txt'
outfile = 'materialized-queries.sql'
schema = 'materialized'

falias = open(aliasfile, 'r')
fout = open(outfile, 'w')

for alias in falias:
	if alias == '' or alias == '\n':
		break
	table = schema + '.t' + str(positiveHash(alias[:-1]))
	sql = 'SELECT * FROM ' + table + ';'
	fout.write('-- ' + alias[:-1] + ':\n' + sql + '\n')

falias.close()
fout.close()
