#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FieldValuePairs(object):

    def __init__(self):
        self._field_key = None
        self._field_status = None
        self._value = None

    @property
    def field_key(self):
        return self._field_key

    @field_key.setter
    def field_key(self, value):
        self._field_key = value
    @property
    def field_status(self):
        return self._field_status

    @field_status.setter
    def field_status(self, value):
        self._field_status = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_key:
            if hasattr(self.field_key, 'to_alipay_dict'):
                params['field_key'] = self.field_key.to_alipay_dict()
            else:
                params['field_key'] = self.field_key
        if self.field_status:
            if hasattr(self.field_status, 'to_alipay_dict'):
                params['field_status'] = self.field_status.to_alipay_dict()
            else:
                params['field_status'] = self.field_status
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FieldValuePairs()
        if 'field_key' in d:
            o.field_key = d['field_key']
        if 'field_status' in d:
            o.field_status = d['field_status']
        if 'value' in d:
            o.value = d['value']
        return o


