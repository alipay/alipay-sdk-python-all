#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditpaySubquota(object):

    def __init__(self):
        self._available_amt = None
        self._quota_type = None
        self._total_amt = None

    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        self._available_amt = value
    @property
    def quota_type(self):
        return self._quota_type

    @quota_type.setter
    def quota_type(self, value):
        self._quota_type = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amt:
            if hasattr(self.available_amt, 'to_alipay_dict'):
                params['available_amt'] = self.available_amt.to_alipay_dict()
            else:
                params['available_amt'] = self.available_amt
        if self.quota_type:
            if hasattr(self.quota_type, 'to_alipay_dict'):
                params['quota_type'] = self.quota_type.to_alipay_dict()
            else:
                params['quota_type'] = self.quota_type
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditpaySubquota()
        if 'available_amt' in d:
            o.available_amt = d['available_amt']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        return o


