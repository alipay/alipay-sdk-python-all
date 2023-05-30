#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankPreferenceSingleRule(object):

    def __init__(self):
        self._amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankPreferenceSingleRule()
        if 'amount' in d:
            o.amount = d['amount']
        return o


