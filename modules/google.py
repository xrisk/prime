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
        message.message.reply("No results were found for " + search_term)
        return

    print message.content
    print search_term

    message.message.reply("Search results for **%s**: " % search_term)

    count = len(results) < 3 and len(results) or 3
    for i in range(0, count):
        res = results[i]
        room.send_message("[%s](%s)" % (res['titleNoFormatting'], res['unescapedUrl']))
        room.send_message(chaterize_message(res["content"]).replace("\n", " "))
        room.send_message("[See More...](%s)" % moreResultsUrl)

def google_search(search_term):
    search_term = search_term.encode('ascii', errors='replace')
    url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&userip=USERS-IP-ADDRESS" % search_term

    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)

    results = json.load(response)

    if len(results["responseData"]["results"]) > 0:
        return results["responseData"]["results"], results["responseData"]["cursor"]["moreResultsUrl"]

    return False
