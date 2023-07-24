#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CategoryRangeInfo(object):

    def __init__(self):
        self._high = None
        self._low = None

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        self._high = value
    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        self._low = value


    def to_alipay_dict(self):
        params = dict()
        if self.high:
            if hasattr(self.high, 'to_alipay_dict'):
                params['high'] = self.high.to_alipay_dict()
            else:
                params['high'] = self.high
        if self.low:
            if hasattr(self.low, 'to_alipay_dict'):
                params['low'] = self.low.to_alipay_dict()
            else:
                params['low'] = self.low
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryRangeInfo()
        if 'high' in d:
            o.high = d['high']
        if 'low' in d:
            o.low = d['low']
        return o


