#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhoneCardShippingAddressModel(object):

    def __init__(self):
        self._address_detail = None
        self._city_code = None
        self._district_code = None
        self._province_code = None

    @property
    def address_detail(self):
        return self._address_detail

    @address_detail.setter
    def address_detail(self, value):
        self._address_detail = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.address_detail:
            if hasattr(self.address_detail, 'to_alipay_dict'):
                params['address_detail'] = self.address_detail.to_alipay_dict()
            else:
                params['address_detail'] = self.address_detail
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhoneCardShippingAddressModel()
        if 'address_detail' in d:
            o.address_detail = d['address_detail']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


