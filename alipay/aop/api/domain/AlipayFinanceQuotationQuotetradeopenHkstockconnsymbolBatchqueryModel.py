#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PageCond import PageCond


class AlipayFinanceQuotationQuotetradeopenHkstockconnsymbolBatchqueryModel(object):

    def __init__(self):
        self._conn_types = None
        self._page_cond = None
        self._symbols = None

    @property
    def conn_types(self):
        return self._conn_types

    @conn_types.setter
    def conn_types(self, value):
        if isinstance(value, list):
            self._conn_types = list()
            for i in value:
                self._conn_types.append(i)
    @property
    def page_cond(self):
        return self._page_cond

    @page_cond.setter
    def page_cond(self, value):
        if isinstance(value, PageCond):
            self._page_cond = value
        else:
            self._page_cond = PageCond.from_alipay_dict(value)
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
        if self.conn_types:
            if isinstance(self.conn_types, list):
                for i in range(0, len(self.conn_types)):
                    element = self.conn_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conn_types[i] = element.to_alipay_dict()
            if hasattr(self.conn_types, 'to_alipay_dict'):
                params['conn_types'] = self.conn_types.to_alipay_dict()
            else:
                params['conn_types'] = self.conn_types
        if self.page_cond:
            if hasattr(self.page_cond, 'to_alipay_dict'):
                params['page_cond'] = self.page_cond.to_alipay_dict()
            else:
                params['page_cond'] = self.page_cond
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
        o = AlipayFinanceQuotationQuotetradeopenHkstockconnsymbolBatchqueryModel()
        if 'conn_types' in d:
            o.conn_types = d['conn_types']
        if 'page_cond' in d:
            o.page_cond = d['page_cond']
        if 'symbols' in d:
            o.symbols = d['symbols']
        return o


