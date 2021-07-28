#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemSkuPropertyInfo(object):

    def __init__(self):
        self._property_key = None
        self._property_value = None

    @property
    def property_key(self):
        return self._property_key

    @property_key.setter
    def property_key(self, value):
        self._property_key = value
    @property
    def property_value(self):
        return self._property_value

    @property_value.setter
    def property_value(self, value):
        self._property_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.property_key:
            if hasattr(self.property_key, 'to_alipay_dict'):
                params['property_key'] = self.property_key.to_alipay_dict()
            else:
                params['property_key'] = self.property_key
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
        o = ItemSkuPropertyInfo()
        if 'property_key' in d:
            o.property_key = d['property_key']
        if 'property_value' in d:
            o.property_value = d['property_value']
        return o


