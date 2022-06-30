#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVoucherAvailableCityCodeModify(object):

    def __init__(self):
        self._city_codes = None

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
        o = OrderVoucherAvailableCityCodeModify()
        if 'city_codes' in d:
            o.city_codes = d['city_codes']
        return o


