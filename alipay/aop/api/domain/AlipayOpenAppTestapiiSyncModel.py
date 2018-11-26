#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestapiiSyncModel(object):

    def __init__(self):
        self._in_1 = None
        self._in_2 = None

    @property
    def in_1(self):
        return self._in_1

    @in_1.setter
    def in_1(self, value):
        self._in_1 = value
    @property
    def in_2(self):
        return self._in_2

    @in_2.setter
    def in_2(self, value):
        self._in_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.in_1:
            if hasattr(self.in_1, 'to_alipay_dict'):
                params['in_1'] = self.in_1.to_alipay_dict()
            else:
                params['in_1'] = self.in_1
        if self.in_2:
            if hasattr(self.in_2, 'to_alipay_dict'):
                params['in_2'] = self.in_2.to_alipay_dict()
            else:
                params['in_2'] = self.in_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestapiiSyncModel()
        if 'in_1' in d:
            o.in_1 = d['in_1']
        if 'in_2' in d:
            o.in_2 = d['in_2']
        return o


