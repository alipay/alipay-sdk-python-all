#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MANPRIVATE(object):

    def __init__(self):
        self._ss = None

    @property
    def ss(self):
        return self._ss

    @ss.setter
    def ss(self, value):
        self._ss = value


    def to_alipay_dict(self):
        params = dict()
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
        o = MANPRIVATE()
        if 'ss' in d:
            o.ss = d['ss']
        return o


