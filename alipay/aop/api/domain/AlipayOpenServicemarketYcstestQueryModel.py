#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.XwbTestData import XwbTestData


class AlipayOpenServicemarketYcstestQueryModel(object):

    def __init__(self):
        self._in_1 = None
        self._in_2 = None
        self._in_3 = None
        self._in_4 = None
        self._in_5 = None
        self._in_6 = None

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
    @property
    def in_3(self):
        return self._in_3

    @in_3.setter
    def in_3(self, value):
        self._in_3 = value
    @property
    def in_4(self):
        return self._in_4

    @in_4.setter
    def in_4(self, value):
        self._in_4 = value
    @property
    def in_5(self):
        return self._in_5

    @in_5.setter
    def in_5(self, value):
        self._in_5 = value
    @property
    def in_6(self):
        return self._in_6

    @in_6.setter
    def in_6(self, value):
        if isinstance(value, XwbTestData):
            self._in_6 = value
        else:
            self._in_6 = XwbTestData.from_alipay_dict(value)


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
        if self.in_3:
            if hasattr(self.in_3, 'to_alipay_dict'):
                params['in_3'] = self.in_3.to_alipay_dict()
            else:
                params['in_3'] = self.in_3
        if self.in_4:
            if hasattr(self.in_4, 'to_alipay_dict'):
                params['in_4'] = self.in_4.to_alipay_dict()
            else:
                params['in_4'] = self.in_4
        if self.in_5:
            if hasattr(self.in_5, 'to_alipay_dict'):
                params['in_5'] = self.in_5.to_alipay_dict()
            else:
                params['in_5'] = self.in_5
        if self.in_6:
            if hasattr(self.in_6, 'to_alipay_dict'):
                params['in_6'] = self.in_6.to_alipay_dict()
            else:
                params['in_6'] = self.in_6
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketYcstestQueryModel()
        if 'in_1' in d:
            o.in_1 = d['in_1']
        if 'in_2' in d:
            o.in_2 = d['in_2']
        if 'in_3' in d:
            o.in_3 = d['in_3']
        if 'in_4' in d:
            o.in_4 = d['in_4']
        if 'in_5' in d:
            o.in_5 = d['in_5']
        if 'in_6' in d:
            o.in_6 = d['in_6']
        return o


