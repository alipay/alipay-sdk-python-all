#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppSdkTestQueryModel(object):

    def __init__(self):
        self._int_body = None
        self._string_str = None

    @property
    def int_body(self):
        return self._int_body

    @int_body.setter
    def int_body(self, value):
        self._int_body = value
    @property
    def string_str(self):
        return self._string_str

    @string_str.setter
    def string_str(self, value):
        self._string_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.int_body:
            if hasattr(self.int_body, 'to_alipay_dict'):
                params['int_body'] = self.int_body.to_alipay_dict()
            else:
                params['int_body'] = self.int_body
        if self.string_str:
            if hasattr(self.string_str, 'to_alipay_dict'):
                params['string_str'] = self.string_str.to_alipay_dict()
            else:
                params['string_str'] = self.string_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppSdkTestQueryModel()
        if 'int_body' in d:
            o.int_body = d['int_body']
        if 'string_str' in d:
            o.string_str = d['string_str']
        return o


