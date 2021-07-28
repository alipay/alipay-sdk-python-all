#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemProperty(object):

    def __init__(self):
        self._prop_key = None
        self._prop_values = None

    @property
    def prop_key(self):
        return self._prop_key

    @prop_key.setter
    def prop_key(self, value):
        self._prop_key = value
    @property
    def prop_values(self):
        return self._prop_values

    @prop_values.setter
    def prop_values(self, value):
        if isinstance(value, list):
            self._prop_values = list()
            for i in value:
                self._prop_values.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.prop_key:
            if hasattr(self.prop_key, 'to_alipay_dict'):
                params['prop_key'] = self.prop_key.to_alipay_dict()
            else:
                params['prop_key'] = self.prop_key
        if self.prop_values:
            if isinstance(self.prop_values, list):
                for i in range(0, len(self.prop_values)):
                    element = self.prop_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prop_values[i] = element.to_alipay_dict()
            if hasattr(self.prop_values, 'to_alipay_dict'):
                params['prop_values'] = self.prop_values.to_alipay_dict()
            else:
                params['prop_values'] = self.prop_values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemProperty()
        if 'prop_key' in d:
            o.prop_key = d['prop_key']
        if 'prop_values' in d:
            o.prop_values = d['prop_values']
        return o


