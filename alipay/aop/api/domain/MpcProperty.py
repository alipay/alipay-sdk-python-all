#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcProperty(object):

    def __init__(self):
        self._property_name = None
        self._property_value = None

    @property
    def property_name(self):
        return self._property_name

    @property_name.setter
    def property_name(self, value):
        self._property_name = value
    @property
    def property_value(self):
        return self._property_value

    @property_value.setter
    def property_value(self, value):
        self._property_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.property_name:
            if hasattr(self.property_name, 'to_alipay_dict'):
                params['property_name'] = self.property_name.to_alipay_dict()
            else:
                params['property_name'] = self.property_name
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
        o = MpcProperty()
        if 'property_name' in d:
            o.property_name = d['property_name']
        if 'property_value' in d:
            o.property_value = d['property_value']
        return o


