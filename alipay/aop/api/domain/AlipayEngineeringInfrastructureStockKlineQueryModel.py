#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryRange import QueryRange


class AlipayEngineeringInfrastructureStockKlineQueryModel(object):

    def __init__(self):
        self._count = None
        self._period = None
        self._query_range = None
        self._split = None
        self._symbol = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def query_range(self):
        return self._query_range

    @query_range.setter
    def query_range(self, value):
        if isinstance(value, QueryRange):
            self._query_range = value
        else:
            self._query_range = QueryRange.from_alipay_dict(value)
    @property
    def split(self):
        return self._split

    @split.setter
    def split(self, value):
        self._split = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.query_range:
            if hasattr(self.query_range, 'to_alipay_dict'):
                params['query_range'] = self.query_range.to_alipay_dict()
            else:
                params['query_range'] = self.query_range
        if self.split:
            if hasattr(self.split, 'to_alipay_dict'):
                params['split'] = self.split.to_alipay_dict()
            else:
                params['split'] = self.split
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
        o = AlipayEngineeringInfrastructureStockKlineQueryModel()
        if 'count' in d:
            o.count = d['count']
        if 'period' in d:
            o.period = d['period']
        if 'query_range' in d:
            o.query_range = d['query_range']
        if 'split' in d:
            o.split = d['split']
        if 'symbol' in d:
            o.symbol = d['symbol']
        return o


