#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalCatePropertyValue(object):

    def __init__(self):
        self._property_id = None
        self._value_alias = None
        self._value_id = None
        self._value_name = None

    @property
    def property_id(self):
        return self._property_id

    @property_id.setter
    def property_id(self, value):
        self._property_id = value
    @property
    def value_alias(self):
        return self._value_alias

    @value_alias.setter
    def value_alias(self, value):
        self._value_alias = value
    @property
    def value_id(self):
        return self._value_id

    @value_id.setter
    def value_id(self, value):
        self._value_id = value
    @property
    def value_name(self):
        return self._value_name

    @value_name.setter
    def value_name(self, value):
        self._value_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.property_id:
            if hasattr(self.property_id, 'to_alipay_dict'):
                params['property_id'] = self.property_id.to_alipay_dict()
            else:
                params['property_id'] = self.property_id
        if self.value_alias:
            if hasattr(self.value_alias, 'to_alipay_dict'):
                params['value_alias'] = self.value_alias.to_alipay_dict()
            else:
                params['value_alias'] = self.value_alias
        if self.value_id:
            if hasattr(self.value_id, 'to_alipay_dict'):
                params['value_id'] = self.value_id.to_alipay_dict()
            else:
                params['value_id'] = self.value_id
        if self.value_name:
            if hasattr(self.value_name, 'to_alipay_dict'):
                params['value_name'] = self.value_name.to_alipay_dict()
            else:
                params['value_name'] = self.value_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalCatePropertyValue()
        if 'property_id' in d:
            o.property_id = d['property_id']
        if 'value_alias' in d:
            o.value_alias = d['value_alias']
        if 'value_id' in d:
            o.value_id = d['value_id']
        if 'value_name' in d:
            o.value_name = d['value_name']
        return o


