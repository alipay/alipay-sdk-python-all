#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotFmInsuCityVO(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._ins_city_code = None

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
    def ins_city_code(self):
        return self._ins_city_code

    @ins_city_code.setter
    def ins_city_code(self, value):
        self._ins_city_code = value


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
        if self.ins_city_code:
            if hasattr(self.ins_city_code, 'to_alipay_dict'):
                params['ins_city_code'] = self.ins_city_code.to_alipay_dict()
            else:
                params['ins_city_code'] = self.ins_city_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotFmInsuCityVO()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'ins_city_code' in d:
            o.ins_city_code = d['ins_city_code']
        return o


