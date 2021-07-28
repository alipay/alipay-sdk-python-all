#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFacePayModel(object):

    def __init__(self):
        self._a = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFacePayModel()
        if 'a' in d:
            o.a = d['a']
        return o


