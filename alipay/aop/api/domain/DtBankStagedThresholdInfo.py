#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankStagedThresholdInfo(object):

    def __init__(self):
        self._max_threshold_amount = None
        self._min_threshold_amount = None
        self._price_calc_type = None
        self._reduce_amount = None

    @property
    def max_threshold_amount(self):
        return self._max_threshold_amount

    @max_threshold_amount.setter
    def max_threshold_amount(self, value):
        self._max_threshold_amount = value
    @property
    def min_threshold_amount(self):
        return self._min_threshold_amount

    @min_threshold_amount.setter
    def min_threshold_amount(self, value):
        self._min_threshold_amount = value
    @property
    def price_calc_type(self):
        return self._price_calc_type

    @price_calc_type.setter
    def price_calc_type(self, value):
        self._price_calc_type = value
    @property
    def reduce_amount(self):
        return self._reduce_amount

    @reduce_amount.setter
    def reduce_amount(self, value):
        self._reduce_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_threshold_amount:
            if hasattr(self.max_threshold_amount, 'to_alipay_dict'):
                params['max_threshold_amount'] = self.max_threshold_amount.to_alipay_dict()
            else:
                params['max_threshold_amount'] = self.max_threshold_amount
        if self.min_threshold_amount:
            if hasattr(self.min_threshold_amount, 'to_alipay_dict'):
                params['min_threshold_amount'] = self.min_threshold_amount.to_alipay_dict()
            else:
                params['min_threshold_amount'] = self.min_threshold_amount
        if self.price_calc_type:
            if hasattr(self.price_calc_type, 'to_alipay_dict'):
                params['price_calc_type'] = self.price_calc_type.to_alipay_dict()
            else:
                params['price_calc_type'] = self.price_calc_type
        if self.reduce_amount:
            if hasattr(self.reduce_amount, 'to_alipay_dict'):
                params['reduce_amount'] = self.reduce_amount.to_alipay_dict()
            else:
                params['reduce_amount'] = self.reduce_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankStagedThresholdInfo()
        if 'max_threshold_amount' in d:
            o.max_threshold_amount = d['max_threshold_amount']
        if 'min_threshold_amount' in d:
            o.min_threshold_amount = d['min_threshold_amount']
        if 'price_calc_type' in d:
            o.price_calc_type = d['price_calc_type']
        if 'reduce_amount' in d:
            o.reduce_amount = d['reduce_amount']
        return o


