#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalInsuredCityList(object):

    def __init__(self):
        self._city_code = None
        self._ins_city_code = None
        self._ins_city_name = None
        self._is_default_city = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def ins_city_code(self):
        return self._ins_city_code

    @ins_city_code.setter
    def ins_city_code(self, value):
        self._ins_city_code = value
    @property
    def ins_city_name(self):
        return self._ins_city_name

    @ins_city_name.setter
    def ins_city_name(self, value):
        self._ins_city_name = value
    @property
    def is_default_city(self):
        return self._is_default_city

    @is_default_city.setter
    def is_default_city(self, value):
        self._is_default_city = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.ins_city_code:
            if hasattr(self.ins_city_code, 'to_alipay_dict'):
                params['ins_city_code'] = self.ins_city_code.to_alipay_dict()
            else:
                params['ins_city_code'] = self.ins_city_code
        if self.ins_city_name:
            if hasattr(self.ins_city_name, 'to_alipay_dict'):
                params['ins_city_name'] = self.ins_city_name.to_alipay_dict()
            else:
                params['ins_city_name'] = self.ins_city_name
        if self.is_default_city:
            if hasattr(self.is_default_city, 'to_alipay_dict'):
                params['is_default_city'] = self.is_default_city.to_alipay_dict()
            else:
                params['is_default_city'] = self.is_default_city
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalInsuredCityList()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'ins_city_code' in d:
            o.ins_city_code = d['ins_city_code']
        if 'ins_city_name' in d:
            o.ins_city_name = d['ins_city_name']
        if 'is_default_city' in d:
            o.is_default_city = d['is_default_city']
        return o


