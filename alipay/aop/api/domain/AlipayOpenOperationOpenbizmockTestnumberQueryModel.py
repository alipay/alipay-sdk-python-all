#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockTestnumberQueryModel(object):

    def __init__(self):
        self._a = None
        self._keykey = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def keykey(self):
        return self._keykey

    @keykey.setter
    def keykey(self, value):
        self._keykey = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.keykey:
            if hasattr(self.keykey, 'to_alipay_dict'):
                params['keykey'] = self.keykey.to_alipay_dict()
            else:
                params['keykey'] = self.keykey
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestnumberQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'keykey' in d:
            o.keykey = d['keykey']
        return o


