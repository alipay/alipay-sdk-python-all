#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortraitDistribution(object):

    def __init__(self):
        self._key = None
        self._number = None
        self._ratio = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitDistribution()
        if 'key' in d:
            o.key = d['key']
        if 'number' in d:
            o.number = d['number']
        if 'ratio' in d:
            o.ratio = d['ratio']
        return o


