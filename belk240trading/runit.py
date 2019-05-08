
from Robinhood import Robinhood
import json
import csv
import shelve
#from rh_SMA import SMA
import decimal
import fix_yahoo_finance as yf

import requests
msft = yf.Ticker("DIS190510C00135000")

# get stock info
print(print(msft.info))

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits
'''
'''
def getcloseandopen(trader,stocksymbol):
      #stocksymbol string, trader = robinhood object
      applequotedata = trader.quote_data(stocksymbol)
      fundamentals=trader.get_fundamentals(stocksymbol)

      previous_close= applequotedata['adjusted_previous_close']
      open_price = applequotedata['last_trade_price']
      volume= fundamentals['volume']
      return {'symbol':stocksymbol,'previous_close':previous_close,'open_price':open_price,'volume':volume}
#print('volume')
#print(fundamentals)
'''
def topofthemorning(previous_close,open_price,volume,trader):
      #previous_close string, open_price string
      gap = float(previous_close) - float(open_price)                        # Example: 250 close price - 249.80 open price
      stopsell=float(open_price) - gap
      print(gap)
        
      if float(volume) > 30000:                         
            if  gap > 0.40:                        #if gap is more than 40 cents            #Buy SPY at open price                                                // buy SPY at 249.80
                  print("buy @" +open_price)
                  trader.place_order(owned_stock['instrument'], owned_stock['quantity'], 1, 'sell', 'immediate', 'market')
                  print('sell limit'+previous_close)                  #sell limit at 250
                  #my_trader.place_order(owned_stock['instrument'], owned_stock['quantity'], 1, 'sell', 'immediate', 'market')
                  print(' Set Stop Sell Order='+str(stopsell))                      # sell if SPY drops by gap amount
                  #my_trader.place_order(owned_stock['instrument'], owned_stock['quantity'], 1, 'sell', 'immediate', 'market')
            elif gap > 0.10:                                                              # if gap is less than 40 cents but greater than 10
                  print("buy @" +open_price)   
                  #my_trader.place_order(owned_stock['instrument'], owned_stock['quantity'], 1, 'sell', 'immediate', 'market')
                                    # buy SPY at 249.80  
                  print('Set Sell limit Price ='+( float(previous_close)  - 0.03))         # sell limit at 249.97
                  #my_trader.place_order(owned_stock['instrument'], owned_stock['quantity'], 1, 'sell', 'immediate', 'market')
      
                  print(' Set Stop Sell Order='+str(stopsell))                  # sell if SPY drops to 246  
                  #my_trader.place_order(owned_stock['instrument'], owned_stock['quantity'], 1, 'sell', 'immediate', 'market')

def kelly_criterion(prob_winning, odds):
      kelly_calc =(prob_winning * (odds+1)-1)/odds
      return kelly_calc

'''



varsymbol="aapl"
r = requests.get('https://api.iextrading.com/1.0/stock/'+varsymbol+'/book').json()
print(r)
