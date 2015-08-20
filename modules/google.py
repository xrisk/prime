"""
https://github.com/michaelpri10/WelcomeBot/
The MIT License (MIT)
Copyright (c) 2015 michaelpri
"""

import urllib

def main(s, priv=False):
    return 'https://www.google.com/#q=' + urllib.quote(s)
