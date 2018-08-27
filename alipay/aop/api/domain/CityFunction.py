#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CityFunction(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._function_type = None

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
    def function_type(self):
        return self._function_type

    @function_type.setter
    def function_type(self, value):
        if isinstance(value, list):
            self._function_type = list()
            for i in value:
                self._function_type.append(i)


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
        if self.function_type:
            if isinstance(self.function_type, list):
                for i in range(0, len(self.function_type)):
                    element = self.function_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.function_type[i] = element.to_alipay_dict()
            if hasattr(self.function_type, 'to_alipay_dict'):
                params['function_type'] = self.function_type.to_alipay_dict()
            else:
                params['function_type'] = self.function_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CityFunction()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'function_type' in d:
            o.function_type = d['function_type']
        return o


