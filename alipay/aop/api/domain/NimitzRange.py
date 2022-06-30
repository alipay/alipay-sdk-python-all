#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NimitzRange(object):

    def __init__(self):
        self._max = None
        self._max_exclude = None
        self._min = None
        self._min_exclude = None

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
    @property
    def max_exclude(self):
        return self._max_exclude

    @max_exclude.setter
    def max_exclude(self, value):
        self._max_exclude = value
    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value
    @property
    def min_exclude(self):
        return self._min_exclude

    @min_exclude.setter
    def min_exclude(self, value):
        self._min_exclude = value


    def to_alipay_dict(self):
        params = dict()
        if self.max:
            if hasattr(self.max, 'to_alipay_dict'):
                params['max'] = self.max.to_alipay_dict()
            else:
                params['max'] = self.max
        if self.max_exclude:
            if hasattr(self.max_exclude, 'to_alipay_dict'):
                params['max_exclude'] = self.max_exclude.to_alipay_dict()
            else:
                params['max_exclude'] = self.max_exclude
        if self.min:
            if hasattr(self.min, 'to_alipay_dict'):
                params['min'] = self.min.to_alipay_dict()
            else:
                params['min'] = self.min
        if self.min_exclude:
            if hasattr(self.min_exclude, 'to_alipay_dict'):
                params['min_exclude'] = self.min_exclude.to_alipay_dict()
            else:
                params['min_exclude'] = self.min_exclude
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NimitzRange()
        if 'max' in d:
            o.max = d['max']
        if 'max_exclude' in d:
            o.max_exclude = d['max_exclude']
        if 'min' in d:
            o.min = d['min']
        if 'min_exclude' in d:
            o.min_exclude = d['min_exclude']
        return o


