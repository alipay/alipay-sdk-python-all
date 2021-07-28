#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecuritySssssssQueryModel(object):

    def __init__(self):
        self._ddd = None
        self._x_adfa = None

    @property
    def ddd(self):
        return self._ddd

    @ddd.setter
    def ddd(self, value):
        self._ddd = value
    @property
    def x_adfa(self):
        return self._x_adfa

    @x_adfa.setter
    def x_adfa(self, value):
        self._x_adfa = value


    def to_alipay_dict(self):
        params = dict()
        if self.ddd:
            if hasattr(self.ddd, 'to_alipay_dict'):
                params['ddd'] = self.ddd.to_alipay_dict()
            else:
                params['ddd'] = self.ddd
        if self.x_adfa:
            if hasattr(self.x_adfa, 'to_alipay_dict'):
                params['x_adfa'] = self.x_adfa.to_alipay_dict()
            else:
                params['x_adfa'] = self.x_adfa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecuritySssssssQueryModel()
        if 'ddd' in d:
            o.ddd = d['ddd']
        if 'x_adfa' in d:
            o.x_adfa = d['x_adfa']
        return o


