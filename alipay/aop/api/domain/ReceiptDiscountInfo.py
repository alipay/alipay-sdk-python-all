#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiptDiscountInfo(object):

    def __init__(self):
        self._amount = None
        self._desc = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptDiscountInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        return o


