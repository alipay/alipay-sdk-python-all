#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SyncData(object):

    def __init__(self):
        self._field = None
        self._value = None

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.field:
            if hasattr(self.field, 'to_alipay_dict'):
                params['field'] = self.field.to_alipay_dict()
            else:
                params['field'] = self.field
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
        o = SyncData()
        if 'field' in d:
            o.field = d['field']
        if 'value' in d:
            o.value = d['value']
        return o


