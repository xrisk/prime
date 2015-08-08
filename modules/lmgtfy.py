import urllib

def main(s, priv=False):
	return 'http://lmgtfy.com/?q='+urllib.quote(s)