#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenNumberRangeValue(object):

    def __init__(self):
        self._number_value = None
        self._operator = None

    @property
    def number_value(self):
        return self._number_value

    @number_value.setter
    def number_value(self, value):
        self._number_value = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.number_value:
            if hasattr(self.number_value, 'to_alipay_dict'):
                params['number_value'] = self.number_value.to_alipay_dict()
            else:
                params['number_value'] = self.number_value
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenNumberRangeValue()
        if 'number_value' in d:
            o.number_value = d['number_value']
        if 'operator' in d:
            o.operator = d['operator']
        return o


