#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KLineDTO(object):

    def __init__(self):
        self._amount = None
        self._close_price = None
        self._date = None
        self._high_price = None
        self._low_price = None
        self._open_price = None
        self._previous_price = None
        self._volume = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def close_price(self):
        return self._close_price

    @close_price.setter
    def close_price(self, value):
        self._close_price = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def high_price(self):
        return self._high_price

    @high_price.setter
    def high_price(self, value):
        self._high_price = value
    @property
    def low_price(self):
        return self._low_price

    @low_price.setter
    def low_price(self, value):
        self._low_price = value
    @property
    def open_price(self):
        return self._open_price

    @open_price.setter
    def open_price(self, value):
        self._open_price = value
    @property
    def previous_price(self):
        return self._previous_price

    @previous_price.setter
    def previous_price(self, value):
        self._previous_price = value
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
        if self.close_price:
            if hasattr(self.close_price, 'to_alipay_dict'):
                params['close_price'] = self.close_price.to_alipay_dict()
            else:
                params['close_price'] = self.close_price
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.high_price:
            if hasattr(self.high_price, 'to_alipay_dict'):
                params['high_price'] = self.high_price.to_alipay_dict()
            else:
                params['high_price'] = self.high_price
        if self.low_price:
            if hasattr(self.low_price, 'to_alipay_dict'):
                params['low_price'] = self.low_price.to_alipay_dict()
            else:
                params['low_price'] = self.low_price
        if self.open_price:
            if hasattr(self.open_price, 'to_alipay_dict'):
                params['open_price'] = self.open_price.to_alipay_dict()
            else:
                params['open_price'] = self.open_price
        if self.previous_price:
            if hasattr(self.previous_price, 'to_alipay_dict'):
                params['previous_price'] = self.previous_price.to_alipay_dict()
            else:
                params['previous_price'] = self.previous_price
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
        o = KLineDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'close_price' in d:
            o.close_price = d['close_price']
        if 'date' in d:
            o.date = d['date']
        if 'high_price' in d:
            o.high_price = d['high_price']
        if 'low_price' in d:
            o.low_price = d['low_price']
        if 'open_price' in d:
            o.open_price = d['open_price']
        if 'previous_price' in d:
            o.previous_price = d['previous_price']
        if 'volume' in d:
            o.volume = d['volume']
        return o


