#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DynamicAttributeVO(object):

    def __init__(self):
        self._attr_alias = None
        self._attr_value = None
        self._value_type = None

    @property
    def attr_alias(self):
        return self._attr_alias

    @attr_alias.setter
    def attr_alias(self, value):
        self._attr_alias = value
    @property
    def attr_value(self):
        return self._attr_value

    @attr_value.setter
    def attr_value(self, value):
        if isinstance(value, list):
            self._attr_value = list()
            for i in value:
                self._attr_value.append(i)
    @property
    def value_type(self):
        return self._value_type

    @value_type.setter
    def value_type(self, value):
        self._value_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_alias:
            if hasattr(self.attr_alias, 'to_alipay_dict'):
                params['attr_alias'] = self.attr_alias.to_alipay_dict()
            else:
                params['attr_alias'] = self.attr_alias
        if self.attr_value:
            if isinstance(self.attr_value, list):
                for i in range(0, len(self.attr_value)):
                    element = self.attr_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_value[i] = element.to_alipay_dict()
            if hasattr(self.attr_value, 'to_alipay_dict'):
                params['attr_value'] = self.attr_value.to_alipay_dict()
            else:
                params['attr_value'] = self.attr_value
        if self.value_type:
            if hasattr(self.value_type, 'to_alipay_dict'):
                params['value_type'] = self.value_type.to_alipay_dict()
            else:
                params['value_type'] = self.value_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DynamicAttributeVO()
        if 'attr_alias' in d:
            o.attr_alias = d['attr_alias']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        if 'value_type' in d:
            o.value_type = d['value_type']
        return o


