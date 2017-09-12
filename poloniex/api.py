#!/usr/bin/env python3
import certifi
import json
import time
import urllib3

class public():
    def __init__(self):
        self.pool = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())

    def request(self, data):
        response = self.pool.request(
            'GET', 'https://poloniex.com/public', fields=data)
        result = {
            'result': json.loads(response.data.decode('utf-8')),
            'timestamp': '%.0f' % time.time()
        }
        return result

    def returnTicker(self):
        data = {'command': 'returnTicker'}
        return self.request(data)

    def return24hVolume(self):
        data = {'command': 'return24hVolume'}
        return self.request(data)

    def returnOrderBook(self, currencyPair, depth=10):
        data = {
            'command': 'returnOrderBook',
            'currencyPair': currencyPair,
            'depth': depth
        }
        return self.request(data)

    def returnTradeHistory(self, currencyPair, start=None, end=None):
        if (start == None | end == None):
            data = {
                'command': 'returnTradeHistory',
                'currencyPair': currencyPair
            }
        else:
            data = {
                'command': 'returnTradeHistory',
                'currencyPair': currencyPair,
                'start': start,
                'end': end
            }
        return self.request(data)

    def returnChartData(self, currencyPair, period, start, end):
        data = {
            'command': 'returnChartData',
            'currencyPair': currencyPair,
            'period': period,
            'start': start,
            'end': end
        }
        return self.request(data)

    def returnCurrencies(self):
        data = {
            'command': 'returnCurrencies'
        }
        return self.request(data)

    def returnLoanOrders(self, currency):
        data = {
            'command': 'returnLoanOrders'
        }
        return self.request(data)


