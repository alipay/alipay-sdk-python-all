#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityAzeQueryModel(object):

    def __init__(self):
        self._in_a = None

    @property
    def in_a(self):
        return self._in_a

    @in_a.setter
    def in_a(self, value):
        self._in_a = value


    def to_alipay_dict(self):
        params = dict()
        if self.in_a:
            if hasattr(self.in_a, 'to_alipay_dict'):
                params['in_a'] = self.in_a.to_alipay_dict()
            else:
                params['in_a'] = self.in_a
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityAzeQueryModel()
        if 'in_a' in d:
            o.in_a = d['in_a']
        return o


