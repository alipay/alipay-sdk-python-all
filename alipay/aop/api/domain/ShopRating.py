#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopRating(object):

    def __init__(self):
        self._lower_bound = None
        self._upper_bound = None
        self._value = None

    @property
    def lower_bound(self):
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, value):
        self._lower_bound = value
    @property
    def upper_bound(self):
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, value):
        self._upper_bound = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.lower_bound:
            if hasattr(self.lower_bound, 'to_alipay_dict'):
                params['lower_bound'] = self.lower_bound.to_alipay_dict()
            else:
                params['lower_bound'] = self.lower_bound
        if self.upper_bound:
            if hasattr(self.upper_bound, 'to_alipay_dict'):
                params['upper_bound'] = self.upper_bound.to_alipay_dict()
            else:
                params['upper_bound'] = self.upper_bound
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopRating()
        if 'lower_bound' in d:
            o.lower_bound = d['lower_bound']
        if 'upper_bound' in d:
            o.upper_bound = d['upper_bound']
        if 'value' in d:
            o.value = d['value']
        return o


