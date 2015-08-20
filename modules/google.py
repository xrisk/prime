"""
https://github.com/michaelpri10/WelcomeBot/
The MIT License (MIT)
Copyright (c) 2015 michaelpri
"""

import urllib2
import json

def main(search_term, priv=False):
    try:
        results, moreResultsUrl = google_search(search_term)
        print results
    except TypeError:
        print "No results"
        return "No results were found for " + search_term

    if results > 0:
        return "[%s](%s)" % (results['titleNoFormatting'], results['unescapedUrl']) + "\n"\
            + chaterize_message(results["content"]).replace("\n", " ") + "\n"\
            + "[See More...](%s)" % moreResultsUrl

def google_search(search_term):
    search_term = search_term.encode('ascii', errors='replace')
    url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&userip=USERS-IP-ADDRESS" % search_term

    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)

    results = json.load(response)

    if len(results["responseData"]["results"]) > 0:
        return results["responseData"]["results"], results["responseData"]["cursor"]["moreResultsUrl"]

    return False
