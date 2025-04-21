#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationQuotetradeTrendBatchqueryModel(object):

    def __init__(self):
        self._day = None
        self._start = None
        self._symbols = None

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
        o = AlipayFinanceQuotationQuotetradeTrendBatchqueryModel()
        if 'day' in d:
            o.day = d['day']
        if 'start' in d:
            o.start = d['start']
        if 'symbols' in d:
            o.symbols = d['symbols']
        return o


