#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PortraitCityValue import PortraitCityValue


class PortraitProvinceValue(object):

    def __init__(self):
        self._area_code = None
        self._city_list = None
        self._num = None
        self._portrait_value = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def city_list(self):
        return self._city_list

    @city_list.setter
    def city_list(self, value):
        if isinstance(value, list):
            self._city_list = list()
            for i in value:
                if isinstance(i, PortraitCityValue):
                    self._city_list.append(i)
                else:
                    self._city_list.append(PortraitCityValue.from_alipay_dict(i))
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def portrait_value(self):
        return self._portrait_value

    @portrait_value.setter
    def portrait_value(self, value):
        self._portrait_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.city_list:
            if isinstance(self.city_list, list):
                for i in range(0, len(self.city_list)):
                    element = self.city_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_list[i] = element.to_alipay_dict()
            if hasattr(self.city_list, 'to_alipay_dict'):
                params['city_list'] = self.city_list.to_alipay_dict()
            else:
                params['city_list'] = self.city_list
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.portrait_value:
            if hasattr(self.portrait_value, 'to_alipay_dict'):
                params['portrait_value'] = self.portrait_value.to_alipay_dict()
            else:
                params['portrait_value'] = self.portrait_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitProvinceValue()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'city_list' in d:
            o.city_list = d['city_list']
        if 'num' in d:
            o.num = d['num']
        if 'portrait_value' in d:
            o.portrait_value = d['portrait_value']
        return o


