import json

decoder = json.JSONDecoder()

with open('none2/assets/none_questions.json', 'r') as fp:
	data = fp.read()

	questions = decoder.decode(data)

	for i, q in enumerate(questions):
		print '| %02d |' % (i + 1),
		print ' - '.join(q['answers'])
