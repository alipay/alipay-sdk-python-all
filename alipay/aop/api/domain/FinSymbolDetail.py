#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinSymbolDetail(object):

    def __init__(self):
        self._symbol_code = None
        self._symbol_name = None

    @property
    def symbol_code(self):
        return self._symbol_code

    @symbol_code.setter
    def symbol_code(self, value):
        self._symbol_code = value
    @property
    def symbol_name(self):
        return self._symbol_name

    @symbol_name.setter
    def symbol_name(self, value):
        self._symbol_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.symbol_code:
            if hasattr(self.symbol_code, 'to_alipay_dict'):
                params['symbol_code'] = self.symbol_code.to_alipay_dict()
            else:
                params['symbol_code'] = self.symbol_code
        if self.symbol_name:
            if hasattr(self.symbol_name, 'to_alipay_dict'):
                params['symbol_name'] = self.symbol_name.to_alipay_dict()
            else:
                params['symbol_name'] = self.symbol_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinSymbolDetail()
        if 'symbol_code' in d:
            o.symbol_code = d['symbol_code']
        if 'symbol_name' in d:
            o.symbol_name = d['symbol_name']
        return o


