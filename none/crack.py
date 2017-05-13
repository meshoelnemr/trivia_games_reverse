import re

pattern = re.compile(r'document\.getElementById\(\'count\'\)\.value =="(.+?)"' +
				 r'\|\|document\.getElementById\(\'count\'\)\.value =="(.+?)"')


for i in range(1, 51):
	with open('none/assets/www/%d.html' % i) as fp:
		data = fp.read()
		match = pattern.search(data)
		print '%02d ->' % i, "%-15s - %-15s" % (match.group(1), match.group(2))
