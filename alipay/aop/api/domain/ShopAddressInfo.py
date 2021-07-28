#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopAddressInfo(object):

    def __init__(self):
        self._accuracy_type = None
        self._address = None
        self._city = None
        self._country = None
        self._county = None
        self._province = None
        self._town = None

    @property
    def accuracy_type(self):
        return self._accuracy_type

    @accuracy_type.setter
    def accuracy_type(self, value):
        self._accuracy_type = value
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
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def town(self):
        return self._town

    @town.setter
    def town(self, value):
        self._town = value


    def to_alipay_dict(self):
        params = dict()
        if self.accuracy_type:
            if hasattr(self.accuracy_type, 'to_alipay_dict'):
                params['accuracy_type'] = self.accuracy_type.to_alipay_dict()
            else:
                params['accuracy_type'] = self.accuracy_type
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
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.county:
            if hasattr(self.county, 'to_alipay_dict'):
                params['county'] = self.county.to_alipay_dict()
            else:
                params['county'] = self.county
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.town:
            if hasattr(self.town, 'to_alipay_dict'):
                params['town'] = self.town.to_alipay_dict()
            else:
                params['town'] = self.town
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopAddressInfo()
        if 'accuracy_type' in d:
            o.accuracy_type = d['accuracy_type']
        if 'address' in d:
            o.address = d['address']
        if 'city' in d:
            o.city = d['city']
        if 'country' in d:
            o.country = d['country']
        if 'county' in d:
            o.county = d['county']
        if 'province' in d:
            o.province = d['province']
        if 'town' in d:
            o.town = d['town']
        return o


