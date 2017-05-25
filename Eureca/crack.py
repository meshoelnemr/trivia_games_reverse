#!/usr/bin/env python3

import base64
import itertools

import sqlite3

# app_id - last character
KEY = '350918706137'[:-1]
# Questions table
QUERY = 'SELECT _id, Question, Correct, Category FROM en'


def reverse(string, version):
	raw = base64.b64decode(string)
	decoded = raw.decode('utf-8')

	result = []
	for i, j in zip(decoded, itertools.cycle(version)):
		result.append(chr(ord(i) ^ ord(j)))

	return ''.join(result)

with sqlite3.connect('eureka/assets/admob3.xml') as db:
	cursor = db.cursor()
	ans = sqlite3.connect('decrypted.sqlite3')
	ans.text_factory = str
	c = ans.cursor()

	# category names
	categories = {}
	for i, cat in cursor.execute('SELECT _id, en from categories').fetchall():
		categories[i] = str(cat)

	cursor.execute(QUERY)
	for i, question, answer, cat_id in cursor.fetchall():
		c.execute('INSERT INTO questions VALUES(?, ?, ?, ?)',
		(i, reverse(question, KEY), reverse(answer, KEY), categories[cat_id]))

	ans.commit()
	c.close()
	ans.close()
	cursor.close()
