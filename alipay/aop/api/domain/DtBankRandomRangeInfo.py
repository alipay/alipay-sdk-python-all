#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankRandomRangeInfo(object):

    def __init__(self):
        self._max_amount = None
        self._min_amount = None
        self._percentage = None

    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.percentage:
            if hasattr(self.percentage, 'to_alipay_dict'):
                params['percentage'] = self.percentage.to_alipay_dict()
            else:
                params['percentage'] = self.percentage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankRandomRangeInfo()
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'percentage' in d:
            o.percentage = d['percentage']
        return o


