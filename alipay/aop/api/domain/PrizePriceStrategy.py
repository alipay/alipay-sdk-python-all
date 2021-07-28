#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizePriceStrategy(object):

    def __init__(self):
        self._max_price = None
        self._min_price = None
        self._stragety_value = None
        self._strategy_type = None
        self._strategy_value = None

    @property
    def max_price(self):
        return self._max_price

    @max_price.setter
    def max_price(self, value):
        self._max_price = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def stragety_value(self):
        return self._stragety_value

    @stragety_value.setter
    def stragety_value(self, value):
        self._stragety_value = value
    @property
    def strategy_type(self):
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, value):
        self._strategy_type = value
    @property
    def strategy_value(self):
        return self._strategy_value

    @strategy_value.setter
    def strategy_value(self, value):
        self._strategy_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_price:
            if hasattr(self.max_price, 'to_alipay_dict'):
                params['max_price'] = self.max_price.to_alipay_dict()
            else:
                params['max_price'] = self.max_price
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.stragety_value:
            if hasattr(self.stragety_value, 'to_alipay_dict'):
                params['stragety_value'] = self.stragety_value.to_alipay_dict()
            else:
                params['stragety_value'] = self.stragety_value
        if self.strategy_type:
            if hasattr(self.strategy_type, 'to_alipay_dict'):
                params['strategy_type'] = self.strategy_type.to_alipay_dict()
            else:
                params['strategy_type'] = self.strategy_type
        if self.strategy_value:
            if hasattr(self.strategy_value, 'to_alipay_dict'):
                params['strategy_value'] = self.strategy_value.to_alipay_dict()
            else:
                params['strategy_value'] = self.strategy_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizePriceStrategy()
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'stragety_value' in d:
            o.stragety_value = d['stragety_value']
        if 'strategy_type' in d:
            o.strategy_type = d['strategy_type']
        if 'strategy_value' in d:
            o.strategy_value = d['strategy_value']
        return o


