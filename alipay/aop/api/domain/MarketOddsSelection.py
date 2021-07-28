#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarketOddsSelection(object):

    def __init__(self):
        self._code = None
        self._price = None
        self._result = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketOddsSelection()
        if 'code' in d:
            o.code = d['code']
        if 'price' in d:
            o.price = d['price']
        if 'result' in d:
            o.result = d['result']
        return o


