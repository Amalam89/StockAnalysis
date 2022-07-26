# indicators.py
#
#Ali Malam
#26643054
#
       
from datetime import date, timedelta

#True Range
class TrCalc:
    
    def calculate(self, result: dict, start_date: str, end_date: str) -> [str]:           
        '''
        This function calculates the true range values of a stock of relevant dates with
        relevant parameter of days.
        '''
        indicator_list = []
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        delta = timedelta(days=1)
        DAY = start_date.strftime('%Y-%m-%d')
        P_DAY = start_date.strftime('%Y-%m-%d')
        
        while start_date <= end_date:   
            

            try:               

                day_high = float(result['Time Series (Daily)'][DAY]['2. high'])

                day_low = float(result['Time Series (Daily)'][DAY]['3. low'])

                p_close = float(result['Time Series (Daily)'][P_DAY]['4. close'])

                if DAY == P_DAY:
                    
                    previous_date = start_date
                
                    start_date += delta

                    P_DAY = previous_date.strftime('%Y-%m-%d')
                
                    DAY = start_date.strftime('%Y-%m-%d')

                    indicator_list.append('')

                    continue               
                
                elif p_close > day_high:

                    true_range = round(((p_close - day_low)/p_close)*100, 4)
                
                elif p_close < day_low:

                    true_range = round(((day_high - p_close)/p_close)*100, 4)

                else:

                    true_range = round(((day_high - day_low)/p_close)*100, 4)                


                p_day = round(p_close, 4)

                indicator_list.append('{0:.4f}'.format(true_range))            

                previous_date = start_date
                
                start_date += delta            
                
                P_DAY = previous_date.strftime('%Y-%m-%d')
                
                DAY = start_date.strftime('%Y-%m-%d')            
                            
            except:            
                
                start_date += delta            
                
                DAY = start_date.strftime('%Y-%m-%d')

                continue

        return indicator_list          
                
           
#Moving Average Close
class MacCalc:
    
    def __init__(self, days):
        self._days = days
    
    def calculate(self, result: dict, start_date: str, end_date: str) -> [str]:
        '''
        This function calculates the closing prices moving average values of a stock of relevant dates with
        relevant parameter of days.
        '''
        indicator_list = []
        running_count = []
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        delta = timedelta(days=1)
        DAY = start_date.strftime('%Y-%m-%d')
        count = 0    
        
        while start_date <= end_date:           

            try:
                
                day_close = float(result['Time Series (Daily)'][DAY]['4. close'])

                running_count.append(day_close)            
                
                count += 1                

                start_date += delta
                    
                DAY = start_date.strftime('%Y-%m-%d')            

                if count >= self._days:

                    mov_avg = '{0:.4f}'.format(round((sum(running_count)/self._days), 4))

                    indicator_list.append(mov_avg)

                    running_count.pop(0)
                    
                else:

                    indicator_list.append('')
                            
            except:            
                
                start_date += delta            
                
                DAY = start_date.strftime('%Y-%m-%d')

                continue

        return indicator_list

#Simple Moving Average Volume
class MavCalc:
    
    def __init__(self, days):
        self._days = days
        
    def calculate(self, result: dict, start_date: str, end_date: str) -> [str]:
        '''
        This function calculates the volume moving average values of a stock of relevant dates with
        relevant parameter of days.
        '''
        indicator_list = []
        running_count = []
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        delta = timedelta(days=1)
        DAY = start_date.strftime('%Y-%m-%d')
        count = 0
        sum_vol = 0
        
        while start_date <= end_date:           

            try:
                
                day_vol = float(result['Time Series (Daily)'][DAY]['5. volume'])           

                running_count.append(day_vol)            
                
                count += 1                

                start_date += delta
                    
                DAY = start_date.strftime('%Y-%m-%d')            

                if count >= self._days:

                    mov_avg = '{0:.4f}'.format(round((sum(running_count)/self._days), 4))                              

                    indicator_list.append(mov_avg)

                    running_count.pop(0)          
                    
                else:

                    indicator_list.append('')
                            
            except:            
                
                start_date += delta            
                
                DAY = start_date.strftime('%Y-%m-%d')

                continue

        return indicator_list

#Directional Indicator Closing
class DirCalc:

    def __init__(self, days):
        self._days = days
    
    def calculate(self, result: dict, start_date: str, end_date: str) -> [str]:
        '''
        This function calculates the closing prices directional indicator values of a stock of relevant dates with
        relevant parameter of days.
        '''       
        indicator_list = []
        running_count = []
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        delta = timedelta(days=1)
        DAY = start_date.strftime('%Y-%m-%d')
        P_DAY = start_date.strftime('%Y-%m-%d')    
        count = 0
       
       
        while start_date <= end_date:          

            try:
                   
                day_close = float(result['Time Series (Daily)'][DAY]['4. close'])

                p_close = float(result['Time Series (Daily)'][P_DAY]['4. close'])            

                if DAY == P_DAY:
                       
                    previous_date = start_date

                    start_date += delta

                    P_DAY = previous_date.strftime('%Y-%m-%d')

                    DAY = start_date.strftime('%Y-%m-%d')

                    indicator_list.append(0)

                    count += 1

                    continue              

                if count <= self._days:
                   
                    if day_close > p_close:

                        running_count.append(1)

                        count += 1
               
                    elif day_close < p_close:

                        running_count.append(-1)

                        count+= 1
                   
                else:

                    running_count.pop(0)

                    if day_close > p_close:                    

                        running_count.append(1)                    

                    elif day_close < p_close:                    

                        running_count.append(-1)             
               
                if sum(running_count) == 0:

                    indicator_list.append('0')

                else:
                
                    indicator_list.append('%+d' % sum(running_count))         

                previous_date = start_date

                start_date += delta            

                P_DAY = previous_date.strftime('%Y-%m-%d')

                DAY = start_date.strftime('%Y-%m-%d')                  
                           
            except:            
               
                start_date += delta            

                DAY = start_date.strftime('%Y-%m-%d')

                continue

        return indicator_list



#Directional Indicator Volume
class DirvCalc:

    def __init__(self, days):
        self._days = days
    
    def calculate(self, result: dict, start_date: str, end_date: str) -> [str]:
        '''
        This function calculates the closing prices directional indicator values of a stock of relevant dates with
        relevant parameter of days.
        '''        
        indicator_list = []
        running_count = []
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        delta = timedelta(days=1)
        DAY = start_date.strftime('%Y-%m-%d')
        P_DAY = start_date.strftime('%Y-%m-%d')    
        count = 0

        while start_date <= end_date:          

            try:
               
                day_close = float(result['Time Series (Daily)'][DAY]['5. volume'])

                p_close = float(result['Time Series (Daily)'][P_DAY]['5. volume'])            

                if DAY == P_DAY:
                   
                    previous_date = start_date

                    start_date += delta

                    P_DAY = previous_date.strftime('%Y-%m-%d')

                    DAY = start_date.strftime('%Y-%m-%d')

                    indicator_list.append(0)

                    count += 1

                    continue              

                if count <= self._days:
                   
                    if day_close > p_close:

                        running_count.append(1)

                        count += 1
               
                    elif day_close < p_close:

                        running_count.append(-1)

                        count+= 1
                   
                else:

                    running_count.pop(0)

                    if day_close > p_close:                    

                        running_count.append(1)                    

                    elif day_close < p_close:                    

                        running_count.append(-1)             
               
                
                if sum(running_count) == 0:

                    indicator_list.append('0')

                else:
                
                    indicator_list.append('%+d' % sum(running_count))
                
                previous_date = start_date

                start_date += delta            

                P_DAY = previous_date.strftime('%Y-%m-%d')

                DAY = start_date.strftime('%Y-%m-%d')                  
                           
            except:            

                start_date += delta            

                DAY = start_date.strftime('%Y-%m-%d')

                continue

        return indicator_list
    

def run_calc(calc: 'Calc', result: dict, start_date: str, end_date: str):
    '''
    Function which uses duck typing to call the function of multiple classes.
    '''
            
    current_value = calc.calculate(result, start_date, end_date)

    return current_value


def run_indicators(result: dict, start_date: str, end_date: str, indicator: str):
    '''
    Function which uses the input of user and call the relevant function of multiple classes with relevant parameters.
    '''
        
    temporary_list = indicator.split()    
    
    if len(temporary_list) == 2:
        
        indicator, num = temporary_list    

        num = int(num)
        
    elif len(temporary_list) == 3:            
        
        indicator, buy_signal, sell_signal = temporary_list

    else:
        
        indicator, num, buy_signal, sell_signal = temporary_list

        num = int(num)
    
    if indicator == 'TR':

        indicator_list = run_calc(TrCalc(), result, start_date, end_date)

        return indicator_list

    elif indicator == 'MP':

        indicator_list = run_calc(MacCalc(num), result, start_date, end_date)        

        return indicator_list
  
    elif indicator == 'MV':
        
        indicator_list = run_calc(MavCalc(num), result, start_date, end_date)

        return indicator_list    
    
    elif indicator == 'DP':

       indicator_list = run_calc(DirCalc(num), result, start_date, end_date)

       return indicator_list

    elif indicator == 'DV':

       indicator_list = run_calc(DirvCalc(num), result, start_date, end_date)

       return indicator_list
        


