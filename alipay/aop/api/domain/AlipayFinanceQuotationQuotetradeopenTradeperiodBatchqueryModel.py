#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradingQueryRange import TradingQueryRange


class AlipayFinanceQuotationQuotetradeopenTradeperiodBatchqueryModel(object):

    def __init__(self):
        self._mkt_type_subtype = None
        self._query_range = None
        self._with_stages = None
        self._with_untradings = None

    @property
    def mkt_type_subtype(self):
        return self._mkt_type_subtype

    @mkt_type_subtype.setter
    def mkt_type_subtype(self, value):
        self._mkt_type_subtype = value
    @property
    def query_range(self):
        return self._query_range

    @query_range.setter
    def query_range(self, value):
        if isinstance(value, TradingQueryRange):
            self._query_range = value
        else:
            self._query_range = TradingQueryRange.from_alipay_dict(value)
    @property
    def with_stages(self):
        return self._with_stages

    @with_stages.setter
    def with_stages(self, value):
        self._with_stages = value
    @property
    def with_untradings(self):
        return self._with_untradings

    @with_untradings.setter
    def with_untradings(self, value):
        self._with_untradings = value


    def to_alipay_dict(self):
        params = dict()
        if self.mkt_type_subtype:
            if hasattr(self.mkt_type_subtype, 'to_alipay_dict'):
                params['mkt_type_subtype'] = self.mkt_type_subtype.to_alipay_dict()
            else:
                params['mkt_type_subtype'] = self.mkt_type_subtype
        if self.query_range:
            if hasattr(self.query_range, 'to_alipay_dict'):
                params['query_range'] = self.query_range.to_alipay_dict()
            else:
                params['query_range'] = self.query_range
        if self.with_stages:
            if hasattr(self.with_stages, 'to_alipay_dict'):
                params['with_stages'] = self.with_stages.to_alipay_dict()
            else:
                params['with_stages'] = self.with_stages
        if self.with_untradings:
            if hasattr(self.with_untradings, 'to_alipay_dict'):
                params['with_untradings'] = self.with_untradings.to_alipay_dict()
            else:
                params['with_untradings'] = self.with_untradings
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeopenTradeperiodBatchqueryModel()
        if 'mkt_type_subtype' in d:
            o.mkt_type_subtype = d['mkt_type_subtype']
        if 'query_range' in d:
            o.query_range = d['query_range']
        if 'with_stages' in d:
            o.with_stages = d['with_stages']
        if 'with_untradings' in d:
            o.with_untradings = d['with_untradings']
        return o


