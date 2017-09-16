#!/usr/bin/env python3
import certifi
import json
import time
import urllib3


class public():
    '''
        Acording to the documentation available in:
        https://poloniex.com/support/api/
        There is six API public methods.
    '''
    def __init__(self):
        self.pool = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())

    def request(self, data):
        '''
        @description: Base request for all methods
        '''
        response = self.pool.request(
            'GET', 'https://poloniex.com/public', fields=data)
        result = {
            'result': json.loads(response.data.decode('utf-8')),
            'timestamp': '%.0f' % time.time()
        }
        return result

    def returnTicker(self):
        '''
        @description:   Ticker for all markets.
        @return:        Object (JSON)
        '''
        data = {
            'command': 'returnTicker'
        }
        return self.request(data)

    def return24hVolume(self):
        '''
        @description:   24-hour volume for all markets.
        @return:        Object (JSON)
        '''

        data = {
            'command': 'return24hVolume'
        }
        return self.request(data)

    def returnOrderBook(self, currencyPair, depth=10):
        '''
        @description:   Order book for a given market or -
                        for all if is equal to: "all".
        @param:         currencyPair
        @param:         depth, default=10
        @return:        Object (JSON)
        '''
        data = {
            'command': 'returnOrderBook',
            'currencyPair': currencyPair,
            'depth': depth
        }
        return self.request(data)

    def returnTradeHistory(self, currencyPair, start=None, end=None):
        '''
        @description:   the last 200 trades for a given market or -
                        up to 50,000 trades between start and end params.
        @param:         currencyPair
        @param:         start - (UTC-timestamp), None by default
        @param:         end -  (UTC-timestamp), None by default
        @return:        Object (JSON)
        '''
        if (start | end):
            data = {
                'command': 'returnTradeHistory',
                'currencyPair': currencyPair,
                'start': start,
                'end': end
            }
        else:
            data = {
                'command': 'returnTradeHistory',
                'currencyPair': currencyPair
            }
        return self.request(data)

    def returnChartData(self, currencyPair, period, start, end):
        '''
        @description    Candlestick chart data for a given [currencyPair]
                        and given [period] in seconds.
                        between [start] and [end] timestamps.
        @currencyPair   String - The required pair.
        @period         Integer - candlestick period.
        @start          Integer - UTC timestamp.
        @end            Integer - UTC timestamp.
        @return         Object (JSON)
        '''
        data = {
            'command': 'returnChartData',
            'currencyPair': currencyPair,
            'period': period,
            'start': start,
            'end': end
        }
        return self.request(data)

    def returnCurrencies(self):
        '''
        @description:   Information about currencies.
        @return:        Object (JSON)
        '''
        data = {
            'command': 'returnCurrencies'
        }
        return self.request(data)

    def returnLoanOrders(self, currency):
        '''
        @description:   List of loan offers and demands for a given currency.
        @param:         currency - String
        @return:        Object (JSON)
        '''
        data = {
            'command': 'returnLoanOrders'
        }
        return self.request(data)
