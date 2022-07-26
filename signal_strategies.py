# signal_strategies.py
#
#Ali Malam
#26643054
#

from datetime import date, timedelta




class TrCalc:

    def __init__(self, buy_signal, sell_signal):
        self._buy_signal = buy_signal        
        self._sell_signal =  sell_signal        
        
    def calculate(self, result: dict, start_date: str, end_date: str, indicator_list: [str]) -> [str]:
            '''
            This function takes the list of indicator values of true range and performs relevant comparisons
            and appends signal strategy recommendations.
            '''
            indicator_list = indicator_list            
            signal_strategies = []
            start_date = date.fromisoformat(start_date)
            end_date = date.fromisoformat(end_date)
            delta = timedelta(days=1)
            DAY = start_date.strftime('%Y-%m-%d')           
            count = 0
            buy_thresh = self._buy_signal[0]
            buy_num = float(self._buy_signal[1:])
            sell_thresh = self._sell_signal[0]
            sell_num = float(self._sell_signal[1:])
            
            
            
            while start_date <= end_date:           

                try:              
                    
                    
                    indicator_value = indicator_list[count]

                    if indicator_value == '':

                        signal_strategies.append(''+'\t'+'')

                    else:

                        indicator_value = float(indicator_list[count])
                        

                        if (buy_thresh == '<' and indicator_value < buy_num) and (sell_thresh == '<' and indicator_value < sell_num):

                            signal_strategies.append('BUY\tSELL')
                            

                        elif (buy_thresh == '<' and indicator_value < buy_num) and (sell_thresh == '>' and indicator_value > sell_num):

                            signal_strategies.append('BUY\tSELL')
                            
                            
                        elif (buy_thresh == '>' and indicator_value > buy_num) and (sell_thresh == '<' and indicator_value < sell_num):
                            
                            signal_strategies.append('BUY\tSELL')
                            
                            
                        elif (buy_thresh == '>' and indicator_value > buy_num) and (sell_thresh == '>' and indicator_value > sell_num):
                            
                            signal_strategies.append('BUY\tSELL')
                            
                            
                        elif (buy_thresh == '<' and indicator_value < buy_num):
                            
                            signal_strategies.append('BUY'+'\t'+'')

                        elif (buy_thresh == '>' and indicator_value > buy_num):

                            signal_strategies.append('BUY'+'\t'+'')

                        elif (sell_thresh == '<' and indicator_value < sell_num):

                            signal_strategies.append(''+'\tSELL')
                            
                        elif (sell_thresh == '>' and indicator_value > sell_num):

                            signal_strategies.append(''+'\tSELL')

                        else:

                            signal_strategies.append(''+'\t'+'')                   

                    count += 1
                                    
                    start_date += delta                                   
                    
                    DAY = start_date.strftime('%Y-%m-%d') 
                                
                except:            
                    
                    start_date += delta            
                    
                    DAY = start_date.strftime('%Y-%m-%d')

                    continue

            return signal_strategies


class MacCalc:

    def calculate(self, result: dict, start_date: str, end_date: str, indicator_list: [str]) -> [str]:
            '''
            This function takes the list of indicator values for closing price moving average and performs relevant comparisons
            and appends signal strategy recommendations.
            '''
            indicator_list = indicator_list            
            signal_strategies = []
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
                    
                    indicator_value = indicator_list[count]

                    if DAY == P_DAY:
                    
                        previous_date = start_date
                    
                        start_date += delta

                        P_DAY = previous_date.strftime('%Y-%m-%d')
                    
                        DAY = start_date.strftime('%Y-%m-%d')

                        signal_strategies.append(''+'\t'+'')

                        count += 1

                        p_indicator_value = indicator_list[count - 1]
                        
                        continue   
                               

                    elif indicator_value == '' or p_indicator_value == '':

                        signal_strategies.append(''+'\t'+'')                        
                                                
                    elif float(indicator_value) < day_close and p_close < float(p_indicator_value):

                        signal_strategies.append('BUY'+'\t'+'')

                    elif float(indicator_value) > day_close and p_close > float(p_indicator_value):

                        signal_strategies.append(''+'\tSELL')

                    else:

                        signal_strategies.append(''+'\t'+'')


                    count += 1
                    
                    p_indicator_value = indicator_list[count - 1]

                    previous_date = start_date
                    
                    start_date += delta            
                    
                    P_DAY = previous_date.strftime('%Y-%m-%d')
                    
                    DAY = start_date.strftime('%Y-%m-%d') 
                                
                except:            
                    
                    start_date += delta            
                    
                    DAY = start_date.strftime('%Y-%m-%d')

                    continue

            return signal_strategies

class MavCalc:

    def calculate(self, result: dict, start_date: str, end_date: str, indicator_list: [str]) -> [str]:
            '''
            This function takes the list of indicator values for volume value and performs relevant comparisons
            and appends signal strategy recommendations.
            '''
            indicator_list = indicator_list            
            signal_strategies = []
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
                    
                    indicator_value = indicator_list[count]

                    if DAY == P_DAY:
                    
                        previous_date = start_date
                    
                        start_date += delta

                        P_DAY = previous_date.strftime('%Y-%m-%d')
                    
                        DAY = start_date.strftime('%Y-%m-%d')

                        signal_strategies.append(''+'\t'+'')

                        count += 1

                        p_indicator_value = indicator_list[count - 1]
                        
                        continue   
                               

                    elif indicator_value == '' or p_indicator_value == '':

                        signal_strategies.append(''+'\t'+'')                        
                                                
                    elif float(indicator_value) < day_close and p_close < float(p_indicator_value):

                        signal_strategies.append('BUY'+'\t'+'')

                    elif float(indicator_value) > day_close and p_close > float(p_indicator_value):

                        signal_strategies.append(''+'\tSELL')

                    else:

                        signal_strategies.append(''+'\t'+'')


                    count += 1
                    
                    p_indicator_value = indicator_list[count - 1]

                    previous_date = start_date
                    
                    start_date += delta            
                    
                    P_DAY = previous_date.strftime('%Y-%m-%d')
                    
                    DAY = start_date.strftime('%Y-%m-%d') 
                                
                except:            
                    
                    start_date += delta            
                    
                    DAY = start_date.strftime('%Y-%m-%d')

                    continue

            return signal_strategies

class DirCalc:

    def __init__(self, buy_signal, sell_signal):
        self._buy_signal = int(buy_signal)
        self._sell_signal =  int(sell_signal)
        
        
    def calculate(self, result: dict, start_date: str, end_date: str, indicator_list: [str]) -> [str]:
            '''
            This function takes the list of indicator values for directional indicator closing prices and volume value
            and performs relevant comparisons and appends signal strategy recommendations.
            '''
            indicator_list = indicator_list            
            signal_strategies = []
            start_date = date.fromisoformat(start_date)
            end_date = date.fromisoformat(end_date)
            delta = timedelta(days=1)
            DAY = start_date.strftime('%Y-%m-%d')                                  
            buy_num = self._buy_signal           
            sell_num = self._sell_signal
            count = 0
            p_indicator_value = ''
            
            while start_date <= end_date:           

                try:                                                           
                    
                    indicator_value = int(indicator_list[count])

                    if indicator_value == 0 and p_indicator_value == '':

                        signal_strategies.append(''+'\t'+'')                        

                    elif (indicator_value > buy_num) and (p_indicator_value <= buy_num):

                        signal_strategies.append('BUY'+'\t'+'')                        

                    elif (indicator_value < sell_num) and (p_indicator_value >= sell_num):

                        signal_strategies.append(''+'\tSELL')                       
                    
                    else:

                        signal_strategies.append(''+'\t'+'')                   

                    count += 1
                    
                    p_indicator_value = int(indicator_list[count - 1])
                    
                    start_date += delta                   
                    
                    DAY = start_date.strftime('%Y-%m-%d') 
                                
                except:            
                    
                    start_date += delta            
                    
                    DAY = start_date.strftime('%Y-%m-%d')

                    continue

            return signal_strategies
 

def run_calc(calc: 'Calc', result: dict, start_date: str, end_date: str, indicator_list: [str]):
    '''
    Function which uses duck typing to call the function of multiple classes.
    '''
            
    current_value = calc.calculate(result, start_date, end_date, indicator_list)

    return current_value


def run_strategies(result: dict, start_date: str, end_date: str, indicator: str, indicator_list: [str]):
    '''
    Function which uses the input of user and call the relevant function of multiple classes with relevant parameters.
    '''
        
    temporary_list = indicator.split()    
    
    if len(temporary_list) == 2:

        indicator, num = temporary_list

    elif len(temporary_list) == 3:            
        
        indicator, buy_signal, sell_signal = temporary_list

    else:
        
        indicator, num, buy_signal, sell_signal = temporary_list
        
    
    if indicator == 'TR':

        strategy_list = run_calc(TrCalc(buy_signal, sell_signal), result, start_date, end_date, indicator_list)

        return strategy_list
    
    elif indicator == 'MP':

        strategy_list = run_calc(MacCalc(), result, start_date, end_date, indicator_list)        

        return strategy_list
  
    elif indicator == 'MV':
        
        strategy_list = run_calc(MavCalc(), result, start_date, end_date, indicator_list)

        return strategy_list    
    
    elif indicator == 'DP' or 'DV':

       strategy_list = run_calc(DirCalc(buy_signal, sell_signal), result, start_date, end_date, indicator_list)

       return strategy_list


