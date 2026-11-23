#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettlementDailyDetail(object):

    def __init__(self):
        self._settlement_amount = None
        self._settlement_date = None

    @property
    def settlement_amount(self):
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self._settlement_amount = value
    @property
    def settlement_date(self):
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, value):
        self._settlement_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.settlement_amount:
            if hasattr(self.settlement_amount, 'to_alipay_dict'):
                params['settlement_amount'] = self.settlement_amount.to_alipay_dict()
            else:
                params['settlement_amount'] = self.settlement_amount
        if self.settlement_date:
            if hasattr(self.settlement_date, 'to_alipay_dict'):
                params['settlement_date'] = self.settlement_date.to_alipay_dict()
            else:
                params['settlement_date'] = self.settlement_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettlementDailyDetail()
        if 'settlement_amount' in d:
            o.settlement_amount = d['settlement_amount']
        if 'settlement_date' in d:
            o.settlement_date = d['settlement_date']
        return o


