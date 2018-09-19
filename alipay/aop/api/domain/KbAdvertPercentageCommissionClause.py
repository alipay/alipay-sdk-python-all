#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertPercentageCommissionClause(object):

    def __init__(self):
        self._max = None
        self._rate = None

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.max:
            if hasattr(self.max, 'to_alipay_dict'):
                params['max'] = self.max.to_alipay_dict()
            else:
                params['max'] = self.max
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertPercentageCommissionClause()
        if 'max' in d:
            o.max = d['max']
        if 'rate' in d:
            o.rate = d['rate']
        return o


