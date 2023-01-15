#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessAddressDTO(object):

    def __init__(self):
        self._city_code = None
        self._country_code = None
        self._detail_address = None
        self._district_code = None
        self._province_code = None
        self._town_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
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
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def town_code(self):
        return self._town_code

    @town_code.setter
    def town_code(self, value):
        self._town_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
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
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.town_code:
            if hasattr(self.town_code, 'to_alipay_dict'):
                params['town_code'] = self.town_code.to_alipay_dict()
            else:
                params['town_code'] = self.town_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessAddressDTO()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'town_code' in d:
            o.town_code = d['town_code']
        return o


