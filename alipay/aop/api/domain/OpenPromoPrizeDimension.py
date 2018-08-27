#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenPromoPrizeDimension(object):

    def __init__(self):
        self._dimension = None
        self._values = None

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                self._values.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.dimension:
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
        if self.values:
            if isinstance(self.values, list):
                for i in range(0, len(self.values)):
                    element = self.values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.values[i] = element.to_alipay_dict()
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenPromoPrizeDimension()
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'values' in d:
            o.values = d['values']
        return o


