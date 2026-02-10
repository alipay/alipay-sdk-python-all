#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfEnumValueItem import AxfEnumValueItem


class AxfItemAttrTemplate(object):

    def __init__(self):
        self._attr_key = None
        self._attr_type = None
        self._category_code = None
        self._enum_values = None
        self._enumerable = None
        self._input = None
        self._multiple = None
        self._required = None

    @property
    def attr_key(self):
        return self._attr_key

    @attr_key.setter
    def attr_key(self, value):
        self._attr_key = value
    @property
    def attr_type(self):
        return self._attr_type

    @attr_type.setter
    def attr_type(self, value):
        self._attr_type = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def enum_values(self):
        return self._enum_values

    @enum_values.setter
    def enum_values(self, value):
        if isinstance(value, list):
            self._enum_values = list()
            for i in value:
                if isinstance(i, AxfEnumValueItem):
                    self._enum_values.append(i)
                else:
                    self._enum_values.append(AxfEnumValueItem.from_alipay_dict(i))
    @property
    def enumerable(self):
        return self._enumerable

    @enumerable.setter
    def enumerable(self, value):
        self._enumerable = value
    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value
    @property
    def multiple(self):
        return self._multiple

    @multiple.setter
    def multiple(self, value):
        self._multiple = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_key:
            if hasattr(self.attr_key, 'to_alipay_dict'):
                params['attr_key'] = self.attr_key.to_alipay_dict()
            else:
                params['attr_key'] = self.attr_key
        if self.attr_type:
            if hasattr(self.attr_type, 'to_alipay_dict'):
                params['attr_type'] = self.attr_type.to_alipay_dict()
            else:
                params['attr_type'] = self.attr_type
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.enum_values:
            if isinstance(self.enum_values, list):
                for i in range(0, len(self.enum_values)):
                    element = self.enum_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enum_values[i] = element.to_alipay_dict()
            if hasattr(self.enum_values, 'to_alipay_dict'):
                params['enum_values'] = self.enum_values.to_alipay_dict()
            else:
                params['enum_values'] = self.enum_values
        if self.enumerable:
            if hasattr(self.enumerable, 'to_alipay_dict'):
                params['enumerable'] = self.enumerable.to_alipay_dict()
            else:
                params['enumerable'] = self.enumerable
        if self.input:
            if hasattr(self.input, 'to_alipay_dict'):
                params['input'] = self.input.to_alipay_dict()
            else:
                params['input'] = self.input
        if self.multiple:
            if hasattr(self.multiple, 'to_alipay_dict'):
                params['multiple'] = self.multiple.to_alipay_dict()
            else:
                params['multiple'] = self.multiple
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfItemAttrTemplate()
        if 'attr_key' in d:
            o.attr_key = d['attr_key']
        if 'attr_type' in d:
            o.attr_type = d['attr_type']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'enum_values' in d:
            o.enum_values = d['enum_values']
        if 'enumerable' in d:
            o.enumerable = d['enumerable']
        if 'input' in d:
            o.input = d['input']
        if 'multiple' in d:
            o.multiple = d['multiple']
        if 'required' in d:
            o.required = d['required']
        return o


