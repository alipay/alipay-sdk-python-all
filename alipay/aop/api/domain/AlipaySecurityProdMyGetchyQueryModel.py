#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdMyGetchyQueryModel(object):

    def __init__(self):
        self._chen = None

    @property
    def chen(self):
        return self._chen

    @chen.setter
    def chen(self, value):
        self._chen = value


    def to_alipay_dict(self):
        params = dict()
        if self.chen:
            if hasattr(self.chen, 'to_alipay_dict'):
                params['chen'] = self.chen.to_alipay_dict()
            else:
                params['chen'] = self.chen
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdMyGetchyQueryModel()
        if 'chen' in d:
            o.chen = d['chen']
        return o


