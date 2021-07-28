#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayGongyiAddressTest(object):

    def __init__(self):
        self._city = None
        self._contury = None
        self._street = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def contury(self):
        return self._contury

    @contury.setter
    def contury(self, value):
        self._contury = value
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.contury:
            if hasattr(self.contury, 'to_alipay_dict'):
                params['contury'] = self.contury.to_alipay_dict()
            else:
                params['contury'] = self.contury
        if self.street:
            if hasattr(self.street, 'to_alipay_dict'):
                params['street'] = self.street.to_alipay_dict()
            else:
                params['street'] = self.street
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayGongyiAddressTest()
        if 'city' in d:
            o.city = d['city']
        if 'contury' in d:
            o.contury = d['contury']
        if 'street' in d:
            o.street = d['street']
        return o


