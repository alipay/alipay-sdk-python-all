#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIsponetestWzwtestWzwtestPreviewModel(object):

    def __init__(self):
        self._number_d = None
        self._s = None
        self._ss = None

    @property
    def number_d(self):
        return self._number_d

    @number_d.setter
    def number_d(self, value):
        self._number_d = value
    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value
    @property
    def ss(self):
        return self._ss

    @ss.setter
    def ss(self, value):
        self._ss = value


    def to_alipay_dict(self):
        params = dict()
        if self.number_d:
            if hasattr(self.number_d, 'to_alipay_dict'):
                params['number_d'] = self.number_d.to_alipay_dict()
            else:
                params['number_d'] = self.number_d
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        if self.ss:
            if hasattr(self.ss, 'to_alipay_dict'):
                params['ss'] = self.ss.to_alipay_dict()
            else:
                params['ss'] = self.ss
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIsponetestWzwtestWzwtestPreviewModel()
        if 'number_d' in d:
            o.number_d = d['number_d']
        if 's' in d:
            o.s = d['s']
        if 'ss' in d:
            o.ss = d['ss']
        return o


