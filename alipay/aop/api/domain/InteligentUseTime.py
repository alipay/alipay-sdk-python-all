#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteligentUseTime(object):

    def __init__(self):
        self._dimension = None
        self._times = None
        self._values = None

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, value):
        self._times = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value


    def to_alipay_dict(self):
        params = dict()
        if self.dimension:
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
        if self.times:
            if hasattr(self.times, 'to_alipay_dict'):
                params['times'] = self.times.to_alipay_dict()
            else:
                params['times'] = self.times
        if self.values:
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentUseTime()
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'times' in d:
            o.times = d['times']
        if 'values' in d:
            o.values = d['values']
        return o


