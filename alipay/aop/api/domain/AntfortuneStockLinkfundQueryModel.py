#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockLinkfundQueryModel(object):

    def __init__(self):
        self._ret_limit = None
        self._symbol = None

    @property
    def ret_limit(self):
        return self._ret_limit

    @ret_limit.setter
    def ret_limit(self, value):
        self._ret_limit = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    def to_alipay_dict(self):
        params = dict()
        if self.ret_limit:
            if hasattr(self.ret_limit, 'to_alipay_dict'):
                params['ret_limit'] = self.ret_limit.to_alipay_dict()
            else:
                params['ret_limit'] = self.ret_limit
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
        o = AntfortuneStockLinkfundQueryModel()
        if 'ret_limit' in d:
            o.ret_limit = d['ret_limit']
        if 'symbol' in d:
            o.symbol = d['symbol']
        return o


