#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntTttDetetA(object):

    def __init__(self):
        self._addr = None

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, value):
        self._addr = value


    def to_alipay_dict(self):
        params = dict()
        if self.addr:
            if hasattr(self.addr, 'to_alipay_dict'):
                params['addr'] = self.addr.to_alipay_dict()
            else:
                params['addr'] = self.addr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntTttDetetA()
        if 'addr' in d:
            o.addr = d['addr']
        return o


