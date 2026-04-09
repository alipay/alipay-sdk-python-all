#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DistrictVo import DistrictVo


class CityVo(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._district_list = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def district_list(self):
        return self._district_list

    @district_list.setter
    def district_list(self, value):
        if isinstance(value, list):
            self._district_list = list()
            for i in value:
                if isinstance(i, DistrictVo):
                    self._district_list.append(i)
                else:
                    self._district_list.append(DistrictVo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.district_list:
            if isinstance(self.district_list, list):
                for i in range(0, len(self.district_list)):
                    element = self.district_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_list[i] = element.to_alipay_dict()
            if hasattr(self.district_list, 'to_alipay_dict'):
                params['district_list'] = self.district_list.to_alipay_dict()
            else:
                params['district_list'] = self.district_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CityVo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'district_list' in d:
            o.district_list = d['district_list']
        return o


