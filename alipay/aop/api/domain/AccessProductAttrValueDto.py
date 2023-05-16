#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessProductAttrValueDto(object):

    def __init__(self):
        self._attr_name = None
        self._attr_value_name_list = None

    @property
    def attr_name(self):
        return self._attr_name

    @attr_name.setter
    def attr_name(self, value):
        self._attr_name = value
    @property
    def attr_value_name_list(self):
        return self._attr_value_name_list

    @attr_value_name_list.setter
    def attr_value_name_list(self, value):
        if isinstance(value, list):
            self._attr_value_name_list = list()
            for i in value:
                self._attr_value_name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.attr_name:
            if hasattr(self.attr_name, 'to_alipay_dict'):
                params['attr_name'] = self.attr_name.to_alipay_dict()
            else:
                params['attr_name'] = self.attr_name
        if self.attr_value_name_list:
            if isinstance(self.attr_value_name_list, list):
                for i in range(0, len(self.attr_value_name_list)):
                    element = self.attr_value_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_value_name_list[i] = element.to_alipay_dict()
            if hasattr(self.attr_value_name_list, 'to_alipay_dict'):
                params['attr_value_name_list'] = self.attr_value_name_list.to_alipay_dict()
            else:
                params['attr_value_name_list'] = self.attr_value_name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessProductAttrValueDto()
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_value_name_list' in d:
            o.attr_value_name_list = d['attr_value_name_list']
        return o


