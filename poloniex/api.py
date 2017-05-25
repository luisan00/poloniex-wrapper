#!/usr/bin/env python

import urllib, urllib2
import time, json
import hmac, hashlib


class public():
	
	def request(self, endpoint):
    	me = urllib2.urlopen(urllib2.Request(endpoint))
        return json.loads(me.read(), 'UTF-8')

    def returnTicker(self):
    	return self.request('https://poloniex.com/public?command=returnTicker')

    def return24hVolume(self):
        return self.request('https://poloniex.com/public?command=return24hVolume')

    def returnOrderBook (self, currencyPair, depth = 10):
    	return self.request('''
    		https://poloniex.com/public?command=returnOrderBook&currencyPair=%s&depth=%s
            ''' % (currencyPair, depth))

    def returnTradeHistory (self, currencyPair, start = None, end = None):
    	if (start == None or end == None):
    		return self.request('''
    			https://poloniex.com/public?command=returnTradeHistory&currencyPair=%s
                ''' % currencyPair)
    	else:
    		return self.request('''
    			https://poloniex.com/public?command=returnTradeHistory&currencyPair=%s&start=%s&end=%s
                ''' % (currencyPair, start, end))

    def returnChartData(self, currencyPair, period, start, end):
    	return self.request('''
    		https://poloniex.com/public?command=returnChartData&currencyPair=%s&period=%S&start=%s&end=%s
            ''' % (currencyPair, period, start, end))

    def returnCurrencies(self):
        return self.request('https://poloniex.com/public?command=returnCurrencies')
        
    def returnLoanOrders(self, currency):
        return self.request('''
            https://poloniex.com/public?command=returnLoanOrders&currency=%s
            ''' % currency)
