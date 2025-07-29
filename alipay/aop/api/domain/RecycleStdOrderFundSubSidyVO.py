#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleStdOrderFundSubSidyVO(object):

    def __init__(self):
        self._amount = None
        self._pay_status = None
        self._percent = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        self._percent = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.percent:
            if hasattr(self.percent, 'to_alipay_dict'):
                params['percent'] = self.percent.to_alipay_dict()
            else:
                params['percent'] = self.percent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleStdOrderFundSubSidyVO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'percent' in d:
            o.percent = d['percent']
        return o


