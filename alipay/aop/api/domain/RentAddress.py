#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentAddress(object):

    def __init__(self):
        self._city_code = None
        self._detail_address = None
        self._district_code = None
        self._full_address = None
        self._province_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def full_address(self):
        return self._full_address

    @full_address.setter
    def full_address(self, value):
        self._full_address = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.full_address:
            if hasattr(self.full_address, 'to_alipay_dict'):
                params['full_address'] = self.full_address.to_alipay_dict()
            else:
                params['full_address'] = self.full_address
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
        o = RentAddress()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'full_address' in d:
            o.full_address = d['full_address']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


