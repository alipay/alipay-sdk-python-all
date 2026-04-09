#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GuardrailsContent(object):

    def __init__(self):
        self._property_code = None
        self._property_format = None
        self._property_value = None

    @property
    def property_code(self):
        return self._property_code

    @property_code.setter
    def property_code(self, value):
        self._property_code = value
    @property
    def property_format(self):
        return self._property_format

    @property_format.setter
    def property_format(self, value):
        self._property_format = value
    @property
    def property_value(self):
        return self._property_value

    @property_value.setter
    def property_value(self, value):
        self._property_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.property_code:
            if hasattr(self.property_code, 'to_alipay_dict'):
                params['property_code'] = self.property_code.to_alipay_dict()
            else:
                params['property_code'] = self.property_code
        if self.property_format:
            if hasattr(self.property_format, 'to_alipay_dict'):
                params['property_format'] = self.property_format.to_alipay_dict()
            else:
                params['property_format'] = self.property_format
        if self.property_value:
            if hasattr(self.property_value, 'to_alipay_dict'):
                params['property_value'] = self.property_value.to_alipay_dict()
            else:
                params['property_value'] = self.property_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuardrailsContent()
        if 'property_code' in d:
            o.property_code = d['property_code']
        if 'property_format' in d:
            o.property_format = d['property_format']
        if 'property_value' in d:
            o.property_value = d['property_value']
        return o


