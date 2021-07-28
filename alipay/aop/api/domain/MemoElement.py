#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemoElement(object):

    def __init__(self):
        self._constant = None
        self._key = None

    @property
    def constant(self):
        return self._constant

    @constant.setter
    def constant(self, value):
        self._constant = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.constant:
            if hasattr(self.constant, 'to_alipay_dict'):
                params['constant'] = self.constant.to_alipay_dict()
            else:
                params['constant'] = self.constant
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemoElement()
        if 'constant' in d:
            o.constant = d['constant']
        if 'key' in d:
            o.key = d['key']
        return o


