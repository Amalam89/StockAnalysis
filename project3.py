#project3.py
#
#Ali Malam
#26643054
#

import download_URL_info

import indicators

import signal_strategies

from datetime import date, timedelta

import urllib.error

import json

import sys

def print_data_analysis(search_result: dict, start_date: str, end_date: str, indicator_strategy: str, symbol: str, indicator: [str], strategies: [str]) -> str:
    '''
    Takes the result from relative dates and prints all info including stock prices, indicators and signal strategies.    
    '''
    
    start_date = date.fromisoformat(start_date)
    end_date = date.fromisoformat(end_date)
    delta = timedelta(days=1)
    DAY = start_date.strftime('%Y-%m-%d')
    count = 0
    body =''
    
      
    while start_date <= end_date:              
        

        try:
            
            day_open = (search_result['Time Series (Daily)'][DAY]['1. open'])            
            day_high = (search_result['Time Series (Daily)'][DAY]['2. high'])
            day_low = (search_result['Time Series (Daily)'][DAY]['3. low'])
            day_close = (search_result['Time Series (Daily)'][DAY]['4. close'])
            day_volume = (search_result['Time Series (Daily)'][DAY]['5. volume'])            
                    
            body += DAY+'\t'+day_open+'\t'+day_high+'\t'+day_low+'\t'+day_close+'\t'+day_volume+'\t'+str(indicator[count])+'\t'+strategies[count]+'\n'
                
            start_date += delta
            DAY = start_date.strftime('%Y-%m-%d')           
            count += 1

        except:

            start_date += delta
            DAY = start_date.strftime('%Y-%m-%d')
            
            continue

    report_header = symbol+"\n"+str(count)+"\n"+indicator_strategy    

    table_header = "Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?"

    print(report_header)
    
    print(table_header)

    print(body, end='')                     
    
    
def run() -> None:
    '''
    This is the function which calls and runs the entire program.
    '''

   
    key_path = input()
    f = open(key_path, "r")
    api_key = f.read()
    URL = input()
    symbol = input()
    start_date = input()
    end_date = input()
    indicator = input()

    try:
    
        result = download_URL_info.get_result(download_URL_info.build_search_url(URL, symbol, api_key))        

        error_message = 'FAILED\n200\nFORMAT'
        
        if 'Time Series (Daily)'not in result:
            
            print(error_message)
            sys.exit() 

        for date in result['Time Series (Daily)']:            

            if '1. open' not in result['Time Series (Daily)'][date]:

                print(error_message)
                sys.exit()
                
            elif '2. high' not in result['Time Series (Daily)'][date]:

                print(error_message)
                sys.exit()
                
            elif '3. low' not in result['Time Series (Daily)'][date]:

                print(error_message)
                sys.exit()
                
            elif '4. close' not in result['Time Series (Daily)'][date]:

                print(error_message)
                sys.exit()
                
            elif '5. volume' not in result['Time Series (Daily)'][date]:

                print(error_message)
                sys.exit()
                
            
        indicator_list = indicators.run_indicators(result, start_date, end_date, indicator)

        ss_list = signal_strategies.run_strategies(result, start_date, end_date, indicator, indicator_list)
        
        print_data_analysis(result, start_date, end_date, indicator, symbol, indicator_list, ss_list)

    except urllib.error.HTTPError as e:

        print('FAILED')
        print(e.code)
        print('NOT 200')
        
    except urllib.error.URLError:
        
        print('FAILED')
        print(0)
        print('NETWORK')    

    except json.JSONDecodeError:

        print('FAILED')
        print(200)
        print('FORMAT')    

    
if __name__ == '__main__':

    run()
