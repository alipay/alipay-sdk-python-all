#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CityVo import CityVo


class ProvinceVo(object):

    def __init__(self):
        self._city_list = None
        self._province_code = None
        self._province_name = None

    @property
    def city_list(self):
        return self._city_list

    @city_list.setter
    def city_list(self, value):
        if isinstance(value, list):
            self._city_list = list()
            for i in value:
                if isinstance(i, CityVo):
                    self._city_list.append(i)
                else:
                    self._city_list.append(CityVo.from_alipay_dict(i))
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProvinceVo()
        if 'city_list' in d:
            o.city_list = d['city_list']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        return o


