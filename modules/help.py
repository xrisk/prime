def open(file,mode='r',buffering=-1):
    import __builtin__    #use import builtins for Python 3.x
    import os.path
    filePath = os.path.join(os.path.dirname(__file__),file)
    return __builtin__.open(filePath,mode,buffering)

def main(str, priv=False):
	import json
	parsed = json.loads(open('modules.json').read())
	s = 'My commands are:\n    -'
	for i in parsed:
		s = s + i+'\n    -'
	return s[:-1].strip()
