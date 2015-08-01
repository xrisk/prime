import json
from urllib import urlopen
def main(search_string, priv=False):
	j =urlopen('http://api.icndb.com/jokes/random').read()
	parsed_data = json.loads(j)
	try:
		return parsed_data['value']['joke']
	except:
		return "We couldn't find a joke for you. :/"
