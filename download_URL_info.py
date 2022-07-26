# download_URL_info.py
#
#Ali Malam
#26643054
#

import json
import urllib.parse
import urllib.request
import project3
from datetime import date, timedelta


def build_search_url(URL: str,symbol: str, api_key: str) -> str:
    '''
    This function takes an API key, a search query and  and builds and returns a URL that can be used
    to ask the Alpha vantage API for information about relevant stock.
    '''
    
    query_parameters = [('function', 'TIME_SERIES_DAILY'),('symbol', symbol),
                        ('outputsize', 'full'),('apikey', api_key)]

    return URL + '/query?' + urllib.parse.urlencode(query_parameters)



def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None
    
    try:
        
        response = urllib.request.urlopen(url)
        
        json_text = response.read().decode(encoding = 'utf-8')
        
        return json.loads(json_text)  
        

    finally:
        
        if response != None:
            response.close()
            



    

if __name__ == '__main__':

    run()
