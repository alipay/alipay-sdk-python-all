#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttributeVO(object):

    def __init__(self):
        self._length = None
        self._name = None
        self._range = None
        self._required = None
        self._type = None
        self._value = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.length:
            if hasattr(self.length, 'to_alipay_dict'):
                params['length'] = self.length.to_alipay_dict()
            else:
                params['length'] = self.length
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.range:
            if hasattr(self.range, 'to_alipay_dict'):
                params['range'] = self.range.to_alipay_dict()
            else:
                params['range'] = self.range
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AttributeVO()
        if 'length' in d:
            o.length = d['length']
        if 'name' in d:
            o.name = d['name']
        if 'range' in d:
            o.range = d['range']
        if 'required' in d:
            o.required = d['required']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


