#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuotationKLineDTO(object):

    def __init__(self):
        self._amount = None
        self._close = None
        self._date = None
        self._high = None
        self._low = None
        self._open = None
        self._previous_close = None
        self._symbol = None
        self._volume = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, value):
        self._close = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        self._high = value
    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        self._low = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def previous_close(self):
        return self._previous_close

    @previous_close.setter
    def previous_close(self, value):
        self._previous_close = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
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
        if self.close:
            if hasattr(self.close, 'to_alipay_dict'):
                params['close'] = self.close.to_alipay_dict()
            else:
                params['close'] = self.close
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.high:
            if hasattr(self.high, 'to_alipay_dict'):
                params['high'] = self.high.to_alipay_dict()
            else:
                params['high'] = self.high
        if self.low:
            if hasattr(self.low, 'to_alipay_dict'):
                params['low'] = self.low.to_alipay_dict()
            else:
                params['low'] = self.low
        if self.open:
            if hasattr(self.open, 'to_alipay_dict'):
                params['open'] = self.open.to_alipay_dict()
            else:
                params['open'] = self.open
        if self.previous_close:
            if hasattr(self.previous_close, 'to_alipay_dict'):
                params['previous_close'] = self.previous_close.to_alipay_dict()
            else:
                params['previous_close'] = self.previous_close
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
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
        o = QuotationKLineDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'close' in d:
            o.close = d['close']
        if 'date' in d:
            o.date = d['date']
        if 'high' in d:
            o.high = d['high']
        if 'low' in d:
            o.low = d['low']
        if 'open' in d:
            o.open = d['open']
        if 'previous_close' in d:
            o.previous_close = d['previous_close']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'volume' in d:
            o.volume = d['volume']
        return o


