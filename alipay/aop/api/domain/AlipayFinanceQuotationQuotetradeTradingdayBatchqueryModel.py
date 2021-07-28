#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationQuotetradeTradingdayBatchqueryModel(object):

    def __init__(self):
        self._begin_date = None
        self._end_date = None
        self._market = None

    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, value):
        self._market = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.market:
            if hasattr(self.market, 'to_alipay_dict'):
                params['market'] = self.market.to_alipay_dict()
            else:
                params['market'] = self.market
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeTradingdayBatchqueryModel()
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'market' in d:
            o.market = d['market']
        return o


