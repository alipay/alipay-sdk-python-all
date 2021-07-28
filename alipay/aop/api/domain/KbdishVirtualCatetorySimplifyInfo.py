#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishVirtualDishSimplifyInfo import KbdishVirtualDishSimplifyInfo


class KbdishVirtualCatetorySimplifyInfo(object):

    def __init__(self):
        self._catetory_name = None
        self._catetory_sort = None
        self._dish_list = None
        self._out_shop_ids = None
        self._period_type = None
        self._period_value = None
        self._time_ranges = None

    @property
    def catetory_name(self):
        return self._catetory_name

    @catetory_name.setter
    def catetory_name(self, value):
        self._catetory_name = value
    @property
    def catetory_sort(self):
        return self._catetory_sort

    @catetory_sort.setter
    def catetory_sort(self, value):
        self._catetory_sort = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, KbdishVirtualDishSimplifyInfo):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(KbdishVirtualDishSimplifyInfo.from_alipay_dict(i))
    @property
    def out_shop_ids(self):
        return self._out_shop_ids

    @out_shop_ids.setter
    def out_shop_ids(self, value):
        if isinstance(value, list):
            self._out_shop_ids = list()
            for i in value:
                self._out_shop_ids.append(i)
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def period_value(self):
        return self._period_value

    @period_value.setter
    def period_value(self, value):
        self._period_value = value
    @property
    def time_ranges(self):
        return self._time_ranges

    @time_ranges.setter
    def time_ranges(self, value):
        if isinstance(value, list):
            self._time_ranges = list()
            for i in value:
                self._time_ranges.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_name:
            if hasattr(self.catetory_name, 'to_alipay_dict'):
                params['catetory_name'] = self.catetory_name.to_alipay_dict()
            else:
                params['catetory_name'] = self.catetory_name
        if self.catetory_sort:
            if hasattr(self.catetory_sort, 'to_alipay_dict'):
                params['catetory_sort'] = self.catetory_sort.to_alipay_dict()
            else:
                params['catetory_sort'] = self.catetory_sort
        if self.dish_list:
            if isinstance(self.dish_list, list):
                for i in range(0, len(self.dish_list)):
                    element = self.dish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        if self.out_shop_ids:
            if isinstance(self.out_shop_ids, list):
                for i in range(0, len(self.out_shop_ids)):
                    element = self.out_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_shop_ids, 'to_alipay_dict'):
                params['out_shop_ids'] = self.out_shop_ids.to_alipay_dict()
            else:
                params['out_shop_ids'] = self.out_shop_ids
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.period_value:
            if hasattr(self.period_value, 'to_alipay_dict'):
                params['period_value'] = self.period_value.to_alipay_dict()
            else:
                params['period_value'] = self.period_value
        if self.time_ranges:
            if isinstance(self.time_ranges, list):
                for i in range(0, len(self.time_ranges)):
                    element = self.time_ranges[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_ranges[i] = element.to_alipay_dict()
            if hasattr(self.time_ranges, 'to_alipay_dict'):
                params['time_ranges'] = self.time_ranges.to_alipay_dict()
            else:
                params['time_ranges'] = self.time_ranges
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishVirtualCatetorySimplifyInfo()
        if 'catetory_name' in d:
            o.catetory_name = d['catetory_name']
        if 'catetory_sort' in d:
            o.catetory_sort = d['catetory_sort']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        if 'out_shop_ids' in d:
            o.out_shop_ids = d['out_shop_ids']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'period_value' in d:
            o.period_value = d['period_value']
        if 'time_ranges' in d:
            o.time_ranges = d['time_ranges']
        return o


