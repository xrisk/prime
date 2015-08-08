"""
https://github.com/michaelpri10/WelcomeBot/

The MIT License (MIT)

Copyright (c) 2015 michaelpri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import urllib2, urllib
from bs4 import BeautifulSoup
import random
import re


def main(search_term, priv=False):

    site = "http://www.google.com/search?tbm=isch&safe=strict&q=" + urllib.quote(search_term)
    print site
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

    req = urllib2.Request(site, headers=hdr)

    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
        return False

    images_page = page.read()
    parsing_page = BeautifulSoup(images_page)
    image_container = parsing_page.select("div#rg_s")[0]
    image_tags = image_container.findAll("a", {"class": "rg_l"}, limit=20)
    final = ""
    counter = 0
    while counter < len(image_tags):
        i = random.choice(image_tags)
        split_at = i["href"].find("imgurl=") + 7
        end_split = i["href"].find("&imgrefurl")
        result = i["href"][split_at:end_split]
        if result.endswith((".jpg", ".gif", ".png", ".jpeg")):
            try_open = True
            single_image = None
            try:
                single_image = urllib2.urlopen(result)
            except:
                try_open = False
            if try_open:
                if len(BeautifulSoup(single_image).findAll(text=re.compile('404'))) > 0:
                    break
                else:
                    final = result
                    break
            else:
                pass
        counter += 1

    if final == "":
        return "Nothing found .-."
    else:
        return final
      


