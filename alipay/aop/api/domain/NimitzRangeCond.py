#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NimitzRange import NimitzRange


class NimitzRangeCond(object):

    def __init__(self):
        self._key = None
        self._range = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        if isinstance(value, NimitzRange):
            self._range = value
        else:
            self._range = NimitzRange.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.range:
            if hasattr(self.range, 'to_alipay_dict'):
                params['range'] = self.range.to_alipay_dict()
            else:
                params['range'] = self.range
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NimitzRangeCond()
        if 'key' in d:
            o.key = d['key']
        if 'range' in d:
            o.range = d['range']
        return o


