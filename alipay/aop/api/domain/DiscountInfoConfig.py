#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountInfoConfig(object):

    def __init__(self):
        self._discount_threshold_amt = None
        self._discount_type = None
        self._discount_value = None

    @property
    def discount_threshold_amt(self):
        return self._discount_threshold_amt

    @discount_threshold_amt.setter
    def discount_threshold_amt(self, value):
        self._discount_threshold_amt = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def discount_value(self):
        return self._discount_value

    @discount_value.setter
    def discount_value(self, value):
        self._discount_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_threshold_amt:
            if hasattr(self.discount_threshold_amt, 'to_alipay_dict'):
                params['discount_threshold_amt'] = self.discount_threshold_amt.to_alipay_dict()
            else:
                params['discount_threshold_amt'] = self.discount_threshold_amt
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.discount_value:
            if hasattr(self.discount_value, 'to_alipay_dict'):
                params['discount_value'] = self.discount_value.to_alipay_dict()
            else:
                params['discount_value'] = self.discount_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountInfoConfig()
        if 'discount_threshold_amt' in d:
            o.discount_threshold_amt = d['discount_threshold_amt']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'discount_value' in d:
            o.discount_value = d['discount_value']
        return o


