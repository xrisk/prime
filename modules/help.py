def main(str, priv=False):
	import json
	parsed = json.loads(open('modules.json').read())
	s = 'My commands are:\n    -'
	for i in parsed:
		s = s + i+'\n    -'
	return s[:-1].strip()
