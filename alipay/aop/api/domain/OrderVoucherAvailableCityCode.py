#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVoucherAvailableCityCode(object):

    def __init__(self):
        self._all_city = None
        self._city_codes = None

    @property
    def all_city(self):
        return self._all_city

    @all_city.setter
    def all_city(self, value):
        self._all_city = value
    @property
    def city_codes(self):
        return self._city_codes

    @city_codes.setter
    def city_codes(self, value):
        if isinstance(value, list):
            self._city_codes = list()
            for i in value:
                self._city_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.all_city:
            if hasattr(self.all_city, 'to_alipay_dict'):
                params['all_city'] = self.all_city.to_alipay_dict()
            else:
                params['all_city'] = self.all_city
        if self.city_codes:
            if isinstance(self.city_codes, list):
                for i in range(0, len(self.city_codes)):
                    element = self.city_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_codes[i] = element.to_alipay_dict()
            if hasattr(self.city_codes, 'to_alipay_dict'):
                params['city_codes'] = self.city_codes.to_alipay_dict()
            else:
                params['city_codes'] = self.city_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherAvailableCityCode()
        if 'all_city' in d:
            o.all_city = d['all_city']
        if 'city_codes' in d:
            o.city_codes = d['city_codes']
        return o


