#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiangTestabc(object):

    def __init__(self):
        self._t = None

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value


    def to_alipay_dict(self):
        params = dict()
        if self.t:
            if hasattr(self.t, 'to_alipay_dict'):
                params['t'] = self.t.to_alipay_dict()
            else:
                params['t'] = self.t
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestabc()
        if 't' in d:
            o.t = d['t']
        return o


