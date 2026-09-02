#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalItemPropery(object):

    def __init__(self):
        self._ext_value = None
        self._property_id = None
        self._value_id = None

    @property
    def ext_value(self):
        return self._ext_value

    @ext_value.setter
    def ext_value(self, value):
        self._ext_value = value
    @property
    def property_id(self):
        return self._property_id

    @property_id.setter
    def property_id(self, value):
        self._property_id = value
    @property
    def value_id(self):
        return self._value_id

    @value_id.setter
    def value_id(self, value):
        self._value_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_value:
            if hasattr(self.ext_value, 'to_alipay_dict'):
                params['ext_value'] = self.ext_value.to_alipay_dict()
            else:
                params['ext_value'] = self.ext_value
        if self.property_id:
            if hasattr(self.property_id, 'to_alipay_dict'):
                params['property_id'] = self.property_id.to_alipay_dict()
            else:
                params['property_id'] = self.property_id
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
        o = ExternalItemPropery()
        if 'ext_value' in d:
            o.ext_value = d['ext_value']
        if 'property_id' in d:
            o.property_id = d['property_id']
        if 'value_id' in d:
            o.value_id = d['value_id']
        return o


