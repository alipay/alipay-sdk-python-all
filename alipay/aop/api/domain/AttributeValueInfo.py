#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttributeValueInfo(object):

    def __init__(self):
        self._alias = None
        self._value = None
        self._value_id = None

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def value_id(self):
        return self._value_id

    @value_id.setter
    def value_id(self, value):
        self._value_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.value_id:
            if hasattr(self.value_id, 'to_alipay_dict'):
                params['value_id'] = self.value_id.to_alipay_dict()
            else:
                params['value_id'] = self.value_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttributeValueInfo()
        if 'alias' in d:
            o.alias = d['alias']
        if 'value' in d:
            o.value = d['value']
        if 'value_id' in d:
            o.value_id = d['value_id']
        return o


