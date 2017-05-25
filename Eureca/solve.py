import sys
import sqlite3

query = 'SELECT question, answer, category \
FROM Questions \
WHERE question LIKE ?'

with sqlite3.connect('decrypted.sqlite3') as db:
	c = db.cursor()

	while True:
		try:
			string = '%%%s%%' % raw_input()
			for question, answer, category in c.execute(query, (string,)).fetchall():
				print category
				print question
				print answer
				print
		except KeyboardInterrupt:
			sys.stdout.write('\b\b  \b\b\n')
			break

	c.close()
