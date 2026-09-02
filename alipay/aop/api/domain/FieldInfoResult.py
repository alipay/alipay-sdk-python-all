#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FieldInfoResult(object):

    def __init__(self):
        self._field_key = None
        self._field_value = None

    @property
    def field_key(self):
        return self._field_key

    @field_key.setter
    def field_key(self, value):
        self._field_key = value
    @property
    def field_value(self):
        return self._field_value

    @field_value.setter
    def field_value(self, value):
        self._field_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_key:
            if hasattr(self.field_key, 'to_alipay_dict'):
                params['field_key'] = self.field_key.to_alipay_dict()
            else:
                params['field_key'] = self.field_key
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
        o = FieldInfoResult()
        if 'field_key' in d:
            o.field_key = d['field_key']
        if 'field_value' in d:
            o.field_value = d['field_value']
        return o


