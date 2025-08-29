#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ColumnDefinition(object):

    def __init__(self):
        self._data_type = None
        self._default_value = None
        self._name = None
        self._order = None
        self._primary_key = None
        self._required = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def primary_key(self):
        return self._primary_key

    @primary_key.setter
    def primary_key(self, value):
        self._primary_key = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.default_value:
            if hasattr(self.default_value, 'to_alipay_dict'):
                params['default_value'] = self.default_value.to_alipay_dict()
            else:
                params['default_value'] = self.default_value
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.primary_key:
            if hasattr(self.primary_key, 'to_alipay_dict'):
                params['primary_key'] = self.primary_key.to_alipay_dict()
            else:
                params['primary_key'] = self.primary_key
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
        o = ColumnDefinition()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'default_value' in d:
            o.default_value = d['default_value']
        if 'name' in d:
            o.name = d['name']
        if 'order' in d:
            o.order = d['order']
        if 'primary_key' in d:
            o.primary_key = d['primary_key']
        if 'required' in d:
            o.required = d['required']
        return o


