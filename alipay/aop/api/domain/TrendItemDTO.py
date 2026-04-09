#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrendItemDTO(object):

    def __init__(self):
        self._amount = None
        self._averagePrice = None
        self._date = None
        self._price = None
        self._volume = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def averagePrice(self):
        return self._averagePrice

    @averagePrice.setter
    def averagePrice(self, value):
        self._averagePrice = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.averagePrice:
            if hasattr(self.averagePrice, 'to_alipay_dict'):
                params['averagePrice'] = self.averagePrice.to_alipay_dict()
            else:
                params['averagePrice'] = self.averagePrice
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.volume:
            if hasattr(self.volume, 'to_alipay_dict'):
                params['volume'] = self.volume.to_alipay_dict()
            else:
                params['volume'] = self.volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrendItemDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'averagePrice' in d:
            o.averagePrice = d['averagePrice']
        if 'date' in d:
            o.date = d['date']
        if 'price' in d:
            o.price = d['price']
        if 'volume' in d:
            o.volume = d['volume']
        return o


