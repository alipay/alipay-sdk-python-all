#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SecuritydataMobileCity(object):

    def __init__(self):
        self._city = None
        self._phone_first_7_digits = None
        self._province = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def phone_first_7_digits(self):
        return self._phone_first_7_digits

    @phone_first_7_digits.setter
    def phone_first_7_digits(self, value):
        self._phone_first_7_digits = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.phone_first_7_digits:
            if hasattr(self.phone_first_7_digits, 'to_alipay_dict'):
                params['phone_first_7_digits'] = self.phone_first_7_digits.to_alipay_dict()
            else:
                params['phone_first_7_digits'] = self.phone_first_7_digits
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SecuritydataMobileCity()
        if 'city' in d:
            o.city = d['city']
        if 'phone_first_7_digits' in d:
            o.phone_first_7_digits = d['phone_first_7_digits']
        if 'province' in d:
            o.province = d['province']
        return o


