#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplyBusinessCity(object):

    def __init__(self):
        self._area_code = None
        self._city_level = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def city_level(self):
        return self._city_level

    @city_level.setter
    def city_level(self, value):
        self._city_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.city_level:
            if hasattr(self.city_level, 'to_alipay_dict'):
                params['city_level'] = self.city_level.to_alipay_dict()
            else:
                params['city_level'] = self.city_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyBusinessCity()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'city_level' in d:
            o.city_level = d['city_level']
        return o


