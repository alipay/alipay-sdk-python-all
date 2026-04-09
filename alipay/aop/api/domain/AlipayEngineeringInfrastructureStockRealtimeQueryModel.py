#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEngineeringInfrastructureStockRealtimeQueryModel(object):

    def __init__(self):
        self._day = None
        self._start = None
        self._symbol = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    def to_alipay_dict(self):
        params = dict()
        if self.day:
            if hasattr(self.day, 'to_alipay_dict'):
                params['day'] = self.day.to_alipay_dict()
            else:
                params['day'] = self.day
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEngineeringInfrastructureStockRealtimeQueryModel()
        if 'day' in d:
            o.day = d['day']
        if 'start' in d:
            o.start = d['start']
        if 'symbol' in d:
            o.symbol = d['symbol']
        return o


