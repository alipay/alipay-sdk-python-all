#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPropertyInfo(object):

    def __init__(self):
        self._property_key = None
        self._property_value_list = None

    @property
    def property_key(self):
        return self._property_key

    @property_key.setter
    def property_key(self, value):
        self._property_key = value
    @property
    def property_value_list(self):
        return self._property_value_list

    @property_value_list.setter
    def property_value_list(self, value):
        if isinstance(value, list):
            self._property_value_list = list()
            for i in value:
                self._property_value_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.property_key:
            if hasattr(self.property_key, 'to_alipay_dict'):
                params['property_key'] = self.property_key.to_alipay_dict()
            else:
                params['property_key'] = self.property_key
        if self.property_value_list:
            if isinstance(self.property_value_list, list):
                for i in range(0, len(self.property_value_list)):
                    element = self.property_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_value_list[i] = element.to_alipay_dict()
            if hasattr(self.property_value_list, 'to_alipay_dict'):
                params['property_value_list'] = self.property_value_list.to_alipay_dict()
            else:
                params['property_value_list'] = self.property_value_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPropertyInfo()
        if 'property_key' in d:
            o.property_key = d['property_key']
        if 'property_value_list' in d:
            o.property_value_list = d['property_value_list']
        return o


