#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmartAddressInfo(object):

    def __init__(self):
        self._area_code = None
        self._city_code = None
        self._machine_address = None
        self._province_code = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def machine_address(self):
        return self._machine_address

    @machine_address.setter
    def machine_address(self, value):
        self._machine_address = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.machine_address:
            if hasattr(self.machine_address, 'to_alipay_dict'):
                params['machine_address'] = self.machine_address.to_alipay_dict()
            else:
                params['machine_address'] = self.machine_address
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmartAddressInfo()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'machine_address' in d:
            o.machine_address = d['machine_address']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


