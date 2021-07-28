#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepayTradeDetail(object):

    def __init__(self):
        self._repay_amount = None
        self._trade_no = None

    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepayTradeDetail()
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


