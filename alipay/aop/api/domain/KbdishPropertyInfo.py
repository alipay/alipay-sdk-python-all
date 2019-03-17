#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishPropertyValueInfo import KbdishPropertyValueInfo


class KbdishPropertyInfo(object):

    def __init__(self):
        self._max_count_limit = None
        self._min_count_limit = None
        self._property_name = None
        self._property_value_info_list = None
        self._sort = None

    @property
    def max_count_limit(self):
        return self._max_count_limit

    @max_count_limit.setter
    def max_count_limit(self, value):
        self._max_count_limit = value
    @property
    def min_count_limit(self):
        return self._min_count_limit

    @min_count_limit.setter
    def min_count_limit(self, value):
        self._min_count_limit = value
    @property
    def property_name(self):
        return self._property_name

    @property_name.setter
    def property_name(self, value):
        self._property_name = value
    @property
    def property_value_info_list(self):
        return self._property_value_info_list

    @property_value_info_list.setter
    def property_value_info_list(self, value):
        if isinstance(value, list):
            self._property_value_info_list = list()
            for i in value:
                if isinstance(i, KbdishPropertyValueInfo):
                    self._property_value_info_list.append(i)
                else:
                    self._property_value_info_list.append(KbdishPropertyValueInfo.from_alipay_dict(i))
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_count_limit:
            if hasattr(self.max_count_limit, 'to_alipay_dict'):
                params['max_count_limit'] = self.max_count_limit.to_alipay_dict()
            else:
                params['max_count_limit'] = self.max_count_limit
        if self.min_count_limit:
            if hasattr(self.min_count_limit, 'to_alipay_dict'):
                params['min_count_limit'] = self.min_count_limit.to_alipay_dict()
            else:
                params['min_count_limit'] = self.min_count_limit
        if self.property_name:
            if hasattr(self.property_name, 'to_alipay_dict'):
                params['property_name'] = self.property_name.to_alipay_dict()
            else:
                params['property_name'] = self.property_name
        if self.property_value_info_list:
            if isinstance(self.property_value_info_list, list):
                for i in range(0, len(self.property_value_info_list)):
                    element = self.property_value_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_value_info_list[i] = element.to_alipay_dict()
            if hasattr(self.property_value_info_list, 'to_alipay_dict'):
                params['property_value_info_list'] = self.property_value_info_list.to_alipay_dict()
            else:
                params['property_value_info_list'] = self.property_value_info_list
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishPropertyInfo()
        if 'max_count_limit' in d:
            o.max_count_limit = d['max_count_limit']
        if 'min_count_limit' in d:
            o.min_count_limit = d['min_count_limit']
        if 'property_name' in d:
            o.property_name = d['property_name']
        if 'property_value_info_list' in d:
            o.property_value_info_list = d['property_value_info_list']
        if 'sort' in d:
            o.sort = d['sort']
        return o


