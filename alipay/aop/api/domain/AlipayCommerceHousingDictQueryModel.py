#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingDictQueryModel(object):

    def __init__(self):
        self._code = None
        self._enum_type = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def enum_type(self):
        return self._enum_type

    @enum_type.setter
    def enum_type(self, value):
        self._enum_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.enum_type:
            if hasattr(self.enum_type, 'to_alipay_dict'):
                params['enum_type'] = self.enum_type.to_alipay_dict()
            else:
                params['enum_type'] = self.enum_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingDictQueryModel()
        if 'code' in d:
            o.code = d['code']
        if 'enum_type' in d:
            o.enum_type = d['enum_type']
        return o


