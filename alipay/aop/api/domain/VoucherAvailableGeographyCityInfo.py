#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherAvailableGeographyCityInfo(object):

    def __init__(self):
        self._all_city = None
        self._available_city_codes = None

    @property
    def all_city(self):
        return self._all_city

    @all_city.setter
    def all_city(self, value):
        self._all_city = value
    @property
    def available_city_codes(self):
        return self._available_city_codes

    @available_city_codes.setter
    def available_city_codes(self, value):
        if isinstance(value, list):
            self._available_city_codes = list()
            for i in value:
                self._available_city_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.all_city:
            if hasattr(self.all_city, 'to_alipay_dict'):
                params['all_city'] = self.all_city.to_alipay_dict()
            else:
                params['all_city'] = self.all_city
        if self.available_city_codes:
            if isinstance(self.available_city_codes, list):
                for i in range(0, len(self.available_city_codes)):
                    element = self.available_city_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_city_codes[i] = element.to_alipay_dict()
            if hasattr(self.available_city_codes, 'to_alipay_dict'):
                params['available_city_codes'] = self.available_city_codes.to_alipay_dict()
            else:
                params['available_city_codes'] = self.available_city_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyCityInfo()
        if 'all_city' in d:
            o.all_city = d['all_city']
        if 'available_city_codes' in d:
            o.available_city_codes = d['available_city_codes']
        return o


