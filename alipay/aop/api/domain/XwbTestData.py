#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XwbTestData(object):

    def __init__(self):
        self._s = None

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value


    def to_alipay_dict(self):
        params = dict()
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XwbTestData()
        if 's' in d:
            o.s = d['s']
        return o


