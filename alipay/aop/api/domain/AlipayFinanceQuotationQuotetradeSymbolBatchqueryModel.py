#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationQuotetradeSymbolBatchqueryModel(object):

    def __init__(self):
        self._symbols = None

    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        if isinstance(value, list):
            self._symbols = list()
            for i in value:
                self._symbols.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.symbols:
            if isinstance(self.symbols, list):
                for i in range(0, len(self.symbols)):
                    element = self.symbols[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbols[i] = element.to_alipay_dict()
            if hasattr(self.symbols, 'to_alipay_dict'):
                params['symbols'] = self.symbols.to_alipay_dict()
            else:
                params['symbols'] = self.symbols
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeSymbolBatchqueryModel()
        if 'symbols' in d:
            o.symbols = d['symbols']
        return o


