#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttributeBean(object):

    def __init__(self):
        self._attribute_name = None
        self._attribute_value = None
        self._attribute_value_list = None

    @property
    def attribute_name(self):
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, value):
        self._attribute_name = value
    @property
    def attribute_value(self):
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, value):
        self._attribute_value = value
    @property
    def attribute_value_list(self):
        return self._attribute_value_list

    @attribute_value_list.setter
    def attribute_value_list(self, value):
        if isinstance(value, list):
            self._attribute_value_list = list()
            for i in value:
                self._attribute_value_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_name:
            if hasattr(self.attribute_name, 'to_alipay_dict'):
                params['attribute_name'] = self.attribute_name.to_alipay_dict()
            else:
                params['attribute_name'] = self.attribute_name
        if self.attribute_value:
            if hasattr(self.attribute_value, 'to_alipay_dict'):
                params['attribute_value'] = self.attribute_value.to_alipay_dict()
            else:
                params['attribute_value'] = self.attribute_value
        if self.attribute_value_list:
            if isinstance(self.attribute_value_list, list):
                for i in range(0, len(self.attribute_value_list)):
                    element = self.attribute_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attribute_value_list[i] = element.to_alipay_dict()
            if hasattr(self.attribute_value_list, 'to_alipay_dict'):
                params['attribute_value_list'] = self.attribute_value_list.to_alipay_dict()
            else:
                params['attribute_value_list'] = self.attribute_value_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttributeBean()
        if 'attribute_name' in d:
            o.attribute_name = d['attribute_name']
        if 'attribute_value' in d:
            o.attribute_value = d['attribute_value']
        if 'attribute_value_list' in d:
            o.attribute_value_list = d['attribute_value_list']
        return o


