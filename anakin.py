""" Re-balances pair of currencies automatically at t intervals"""

import pandas as pd
import coinbasepro

#TODO setup connections

c = coinbasepro.PublicClient()

#TODO get necessary balances

class Balance:
    def __init__(self, ticker = 'ETH-USD'):
        self.ticker = ticker
    def open(self):
        return float(c.get_product_24hr_stats(self.ticker)['open'])


#TODO execute re-balance



