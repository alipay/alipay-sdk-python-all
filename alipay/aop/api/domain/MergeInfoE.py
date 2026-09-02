#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MergeInfoE(object):

    def __init__(self):
        self._merge_discount_amount = None
        self._merge_period = None
        self._merge_rent_amount = None
        self._original_period = None

    @property
    def merge_discount_amount(self):
        return self._merge_discount_amount

    @merge_discount_amount.setter
    def merge_discount_amount(self, value):
        self._merge_discount_amount = value
    @property
    def merge_period(self):
        return self._merge_period

    @merge_period.setter
    def merge_period(self, value):
        self._merge_period = value
    @property
    def merge_rent_amount(self):
        return self._merge_rent_amount

    @merge_rent_amount.setter
    def merge_rent_amount(self, value):
        self._merge_rent_amount = value
    @property
    def original_period(self):
        return self._original_period

    @original_period.setter
    def original_period(self, value):
        self._original_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.merge_discount_amount:
            if hasattr(self.merge_discount_amount, 'to_alipay_dict'):
                params['merge_discount_amount'] = self.merge_discount_amount.to_alipay_dict()
            else:
                params['merge_discount_amount'] = self.merge_discount_amount
        if self.merge_period:
            if hasattr(self.merge_period, 'to_alipay_dict'):
                params['merge_period'] = self.merge_period.to_alipay_dict()
            else:
                params['merge_period'] = self.merge_period
        if self.merge_rent_amount:
            if hasattr(self.merge_rent_amount, 'to_alipay_dict'):
                params['merge_rent_amount'] = self.merge_rent_amount.to_alipay_dict()
            else:
                params['merge_rent_amount'] = self.merge_rent_amount
        if self.original_period:
            if hasattr(self.original_period, 'to_alipay_dict'):
                params['original_period'] = self.original_period.to_alipay_dict()
            else:
                params['original_period'] = self.original_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MergeInfoE()
        if 'merge_discount_amount' in d:
            o.merge_discount_amount = d['merge_discount_amount']
        if 'merge_period' in d:
            o.merge_period = d['merge_period']
        if 'merge_rent_amount' in d:
            o.merge_rent_amount = d['merge_rent_amount']
        if 'original_period' in d:
            o.original_period = d['original_period']
        return o


