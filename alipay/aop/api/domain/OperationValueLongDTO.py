#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationValueLongDTO(object):

    def __init__(self):
        self._last_period_value = None
        self._ratio = None
        self._value = None

    @property
    def last_period_value(self):
        return self._last_period_value

    @last_period_value.setter
    def last_period_value(self, value):
        self._last_period_value = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.last_period_value:
            if hasattr(self.last_period_value, 'to_alipay_dict'):
                params['last_period_value'] = self.last_period_value.to_alipay_dict()
            else:
                params['last_period_value'] = self.last_period_value
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
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
        o = OperationValueLongDTO()
        if 'last_period_value' in d:
            o.last_period_value = d['last_period_value']
        if 'ratio' in d:
            o.ratio = d['ratio']
        if 'value' in d:
            o.value = d['value']
        return o


