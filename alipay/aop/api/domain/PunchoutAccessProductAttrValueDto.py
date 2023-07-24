#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PunchoutAccessProductAttrValueDto(object):

    def __init__(self):
        self._attr_desc = None
        self._attr_en_name = None
        self._attr_en_value_name_list = None
        self._attr_name = None
        self._attr_value_name_list = None
        self._is_key = None

    @property
    def attr_desc(self):
        return self._attr_desc

    @attr_desc.setter
    def attr_desc(self, value):
        self._attr_desc = value
    @property
    def attr_en_name(self):
        return self._attr_en_name

    @attr_en_name.setter
    def attr_en_name(self, value):
        self._attr_en_name = value
    @property
    def attr_en_value_name_list(self):
        return self._attr_en_value_name_list

    @attr_en_value_name_list.setter
    def attr_en_value_name_list(self, value):
        if isinstance(value, list):
            self._attr_en_value_name_list = list()
            for i in value:
                self._attr_en_value_name_list.append(i)
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
    @property
    def is_key(self):
        return self._is_key

    @is_key.setter
    def is_key(self, value):
        self._is_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_desc:
            if hasattr(self.attr_desc, 'to_alipay_dict'):
                params['attr_desc'] = self.attr_desc.to_alipay_dict()
            else:
                params['attr_desc'] = self.attr_desc
        if self.attr_en_name:
            if hasattr(self.attr_en_name, 'to_alipay_dict'):
                params['attr_en_name'] = self.attr_en_name.to_alipay_dict()
            else:
                params['attr_en_name'] = self.attr_en_name
        if self.attr_en_value_name_list:
            if isinstance(self.attr_en_value_name_list, list):
                for i in range(0, len(self.attr_en_value_name_list)):
                    element = self.attr_en_value_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_en_value_name_list[i] = element.to_alipay_dict()
            if hasattr(self.attr_en_value_name_list, 'to_alipay_dict'):
                params['attr_en_value_name_list'] = self.attr_en_value_name_list.to_alipay_dict()
            else:
                params['attr_en_value_name_list'] = self.attr_en_value_name_list
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
        if self.is_key:
            if hasattr(self.is_key, 'to_alipay_dict'):
                params['is_key'] = self.is_key.to_alipay_dict()
            else:
                params['is_key'] = self.is_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PunchoutAccessProductAttrValueDto()
        if 'attr_desc' in d:
            o.attr_desc = d['attr_desc']
        if 'attr_en_name' in d:
            o.attr_en_name = d['attr_en_name']
        if 'attr_en_value_name_list' in d:
            o.attr_en_value_name_list = d['attr_en_value_name_list']
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_value_name_list' in d:
            o.attr_value_name_list = d['attr_value_name_list']
        if 'is_key' in d:
            o.is_key = d['is_key']
        return o


