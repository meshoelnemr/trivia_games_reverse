import base64
import sqlite3
from Crypto.Cipher import AES

key = 'w4op394t[srhgjs['

output = 'answers.sqlite3'
data_file = 'endless_quiz/assets/databases/data'
query = 'SELECT _id, Question, CorrectAnswer, Category '\
		'FROM MC_Questions '\
		'WHERE Language = "eng"'

aes = AES.new(key, AES.MODE_ECB)


def decrypt(string):
	result = aes.decrypt(base64.b64decode(string))

	pad = ord(result[-1])
	if pad <= 0x10:
		result = result[:-pad]

	return result

with sqlite3.connect(data_file) as db:
	ans_db = sqlite3.connect(output)
	ans_db.text_factory = str
	ans_cursor = ans_db.cursor()

	cursor = db.cursor()
	cursor.execute(query)

	for _id, question, answer, category in cursor.fetchall():
		decrypted_question = decrypt(question)
		decrypted_answer = decrypt(answer)

		try:
			ans_cursor.execute('INSERT INTO Questions VALUES (?,?,?,?);', (_id, decrypted_question, decrypted_answer, category))
		except sqlite3.IntegrityError:
			pass
		else:
			print '[#] added question id %08d' % _id

	ans_db.commit()
	ans_cursor.close()
	ans_db.close()
	
	cursor.close()
