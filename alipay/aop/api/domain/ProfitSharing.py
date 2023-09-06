#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProfitSharing(object):

    def __init__(self):
        self._alloc_account = None
        self._alloc_amount = None

    @property
    def alloc_account(self):
        return self._alloc_account

    @alloc_account.setter
    def alloc_account(self, value):
        self._alloc_account = value
    @property
    def alloc_amount(self):
        return self._alloc_amount

    @alloc_amount.setter
    def alloc_amount(self, value):
        self._alloc_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alloc_account:
            if hasattr(self.alloc_account, 'to_alipay_dict'):
                params['alloc_account'] = self.alloc_account.to_alipay_dict()
            else:
                params['alloc_account'] = self.alloc_account
        if self.alloc_amount:
            if hasattr(self.alloc_amount, 'to_alipay_dict'):
                params['alloc_amount'] = self.alloc_amount.to_alipay_dict()
            else:
                params['alloc_amount'] = self.alloc_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProfitSharing()
        if 'alloc_account' in d:
            o.alloc_account = d['alloc_account']
        if 'alloc_amount' in d:
            o.alloc_amount = d['alloc_amount']
        return o


