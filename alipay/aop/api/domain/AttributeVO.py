#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttributeVO(object):

    def __init__(self):
        self._is_required = None
        self._key = None
        self._length = None
        self._name = None
        self._range = None
        self._type = None
        self._value = None

    @property
    def is_required(self):
        return self._is_required

    @is_required.setter
    def is_required(self, value):
        self._is_required = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
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
        if self.is_required:
            if hasattr(self.is_required, 'to_alipay_dict'):
                params['is_required'] = self.is_required.to_alipay_dict()
            else:
                params['is_required'] = self.is_required
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
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
        if 'is_required' in d:
            o.is_required = d['is_required']
        if 'key' in d:
            o.key = d['key']
        if 'length' in d:
            o.length = d['length']
        if 'name' in d:
            o.name = d['name']
        if 'range' in d:
            o.range = d['range']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


