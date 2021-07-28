#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationQuotetradeSymbolsQueryModel(object):

    def __init__(self):
        self._market = None
        self._sub_type = None
        self._type = None

    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, value):
        self._market = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.market:
            if hasattr(self.market, 'to_alipay_dict'):
                params['market'] = self.market.to_alipay_dict()
            else:
                params['market'] = self.market
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeSymbolsQueryModel()
        if 'market' in d:
            o.market = d['market']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'type' in d:
            o.type = d['type']
        return o


