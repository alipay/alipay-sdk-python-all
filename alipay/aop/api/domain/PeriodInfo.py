#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PeriodInfo(object):

    def __init__(self):
        self._dimension = None
        self._value = None

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.dimension:
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
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
        o = PeriodInfo()
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'value' in d:
            o.value = d['value']
        return o


