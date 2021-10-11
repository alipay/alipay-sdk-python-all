#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FvPairList(object):

    def __init__(self):
        self._field_code = None
        self._field_value = None

    @property
    def field_code(self):
        return self._field_code

    @field_code.setter
    def field_code(self, value):
        self._field_code = value
    @property
    def field_value(self):
        return self._field_value

    @field_value.setter
    def field_value(self, value):
        self._field_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_code:
            if hasattr(self.field_code, 'to_alipay_dict'):
                params['field_code'] = self.field_code.to_alipay_dict()
            else:
                params['field_code'] = self.field_code
        if self.field_value:
            if hasattr(self.field_value, 'to_alipay_dict'):
                params['field_value'] = self.field_value.to_alipay_dict()
            else:
                params['field_value'] = self.field_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FvPairList()
        if 'field_code' in d:
            o.field_code = d['field_code']
        if 'field_value' in d:
            o.field_value = d['field_value']
        return o


