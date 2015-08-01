from urllib import urlopen
import json
def main(search_string, priv=False):
    giphy_url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag={}".format(search_string)
    try:
        j = urlopen(giphy_url).read()
        parsed_data = json.loads(j)
        if parsed_data['meta']['status'] == 200:
            return parsed_data['data']['image_url']
        else:
            raise
    except Exception, e:
        return 'The search failed, Jim :(' + str(e)
        
        
    
    