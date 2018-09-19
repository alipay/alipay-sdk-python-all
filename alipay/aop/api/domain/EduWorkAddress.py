#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduWorkAddress(object):

    def __init__(self):
        self._address = None
        self._city = None
        self._district_name = None
        self._province = None
        self._street_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def street_name(self):
        return self._street_name

    @street_name.setter
    def street_name(self, value):
        self._street_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.street_name:
            if hasattr(self.street_name, 'to_alipay_dict'):
                params['street_name'] = self.street_name.to_alipay_dict()
            else:
                params['street_name'] = self.street_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduWorkAddress()
        if 'address' in d:
            o.address = d['address']
        if 'city' in d:
            o.city = d['city']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'province' in d:
            o.province = d['province']
        if 'street_name' in d:
            o.street_name = d['street_name']
        return o


