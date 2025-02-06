#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupRestrictionInfo(object):

    def __init__(self):
        self._max = None
        self._min = None

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value


    def to_alipay_dict(self):
        params = dict()
        if self.max:
            if hasattr(self.max, 'to_alipay_dict'):
                params['max'] = self.max.to_alipay_dict()
            else:
                params['max'] = self.max
        if self.min:
            if hasattr(self.min, 'to_alipay_dict'):
                params['min'] = self.min.to_alipay_dict()
            else:
                params['min'] = self.min
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupRestrictionInfo()
        if 'max' in d:
            o.max = d['max']
        if 'min' in d:
            o.min = d['min']
        return o


