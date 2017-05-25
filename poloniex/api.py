#!/usr/bin/env python

import urllib, urllib2
import time, json
import hmac, hashlib

# Public methods
# Working...
class public:

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

# Trading methods
# API Key is required
# Work in progress!!
class trading():

	def __init__(self, sign):
		self.key = sign['key']
		self.secret = sign['secret']

	def request(self, command, args):

		requestData = {
			'command': command,
			'nonce': int(time.time()*1000)
			}

		data = urllib.urlencode(requestData)
		auth = hmac.new(self.secret, data, hashlib.sha512).hexdigest()
		headers = {
			'Sign': auth,
			'Key': self.key
		}
		response = urllib2.urlopen(urllib2.Request('https://poloniex.com/tradingApi', data, headers))
		return json.loads(response.read(), 'UTF-8')
	# Trading methods
	def returnBalances(self):
		pass

	def returnCompleteBalances(self):
		pass

	def returnDepositAddresses(self):
		pass

	def generateNewAddress(self, currency):
		pass

	def returnDepositsWithdrawals(self, start, end):
		pass

	def returnOpenOrders(self, currencyPair='all'):
		pass

	def returnTradeHistory(self, currencyPair='all'):
		pass

	def returnOrderTrades(self, orderNumber):
		pass

	def buy(self, currencyPair, rate, amount):
		pass

	def sell(self, currencyPair, rate, amount):
		pass

	def cancelOrder(self, orderNumber):
		pass

	def moveOrder(self, orderNumber, rate, amount=None):
		pass

	def withdraw(self, currency, amount, address):
		pass

	def returnFeeInfo(self):
		pass

	def returnAvailableAccountBalances(self, account=None):
		pass

	def returnTradableBalances(self):
		pass

	def transferBalance(self, currency, amount, fromAccount, toAccount):
		pass
	# Margin methods
	def marginBuy(self):
		pass

	def marginSell(self):
		pass

	def getMarginPosition(self):
		pass

	def closeMarginPosition(self):
		pass
	# Loans methods
	def createLoanOffer(self):
		pass

	def cancelLoanOffer(self):
		pass

	def returnOpenLoanOffers(self):
		pass

	def returnActiveLoans(self):
		pass

	def returnLendingHistory(self, start, end):
		pass

	def toggleAutoRenew(self, orderNumber):
		pass
