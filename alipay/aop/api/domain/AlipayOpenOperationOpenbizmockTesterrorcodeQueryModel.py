#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockTesterrorcodeQueryModel(object):

    def __init__(self):
        self._key = None
        self._keykey = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def keykey(self):
        return self._keykey

    @keykey.setter
    def keykey(self, value):
        self._keykey = value


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
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
        o = AlipayOpenOperationOpenbizmockTesterrorcodeQueryModel()
        if 'key' in d:
            o.key = d['key']
        if 'keykey' in d:
            o.keykey = d['keykey']
        return o


