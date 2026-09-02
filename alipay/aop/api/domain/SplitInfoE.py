#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SplitInfoE(object):

    def __init__(self):
        self._original_period = None
        self._split_other_amount = None
        self._split_period = None
        self._split_rent_amount = None

    @property
    def original_period(self):
        return self._original_period

    @original_period.setter
    def original_period(self, value):
        self._original_period = value
    @property
    def split_other_amount(self):
        return self._split_other_amount

    @split_other_amount.setter
    def split_other_amount(self, value):
        self._split_other_amount = value
    @property
    def split_period(self):
        return self._split_period

    @split_period.setter
    def split_period(self, value):
        self._split_period = value
    @property
    def split_rent_amount(self):
        return self._split_rent_amount

    @split_rent_amount.setter
    def split_rent_amount(self, value):
        self._split_rent_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_period:
            if hasattr(self.original_period, 'to_alipay_dict'):
                params['original_period'] = self.original_period.to_alipay_dict()
            else:
                params['original_period'] = self.original_period
        if self.split_other_amount:
            if hasattr(self.split_other_amount, 'to_alipay_dict'):
                params['split_other_amount'] = self.split_other_amount.to_alipay_dict()
            else:
                params['split_other_amount'] = self.split_other_amount
        if self.split_period:
            if hasattr(self.split_period, 'to_alipay_dict'):
                params['split_period'] = self.split_period.to_alipay_dict()
            else:
                params['split_period'] = self.split_period
        if self.split_rent_amount:
            if hasattr(self.split_rent_amount, 'to_alipay_dict'):
                params['split_rent_amount'] = self.split_rent_amount.to_alipay_dict()
            else:
                params['split_rent_amount'] = self.split_rent_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SplitInfoE()
        if 'original_period' in d:
            o.original_period = d['original_period']
        if 'split_other_amount' in d:
            o.split_other_amount = d['split_other_amount']
        if 'split_period' in d:
            o.split_period = d['split_period']
        if 'split_rent_amount' in d:
            o.split_rent_amount = d['split_rent_amount']
        return o


