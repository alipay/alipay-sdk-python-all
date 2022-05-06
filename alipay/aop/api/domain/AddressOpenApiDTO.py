#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddressOpenApiDTO(object):

    def __init__(self):
        self._addr = None
        self._city = None
        self._country = None
        self._province = None

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, value):
        self._addr = value
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
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.addr:
            if hasattr(self.addr, 'to_alipay_dict'):
                params['addr'] = self.addr.to_alipay_dict()
            else:
                params['addr'] = self.addr
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
        o = AddressOpenApiDTO()
        if 'addr' in d:
            o.addr = d['addr']
        if 'city' in d:
            o.city = d['city']
        if 'country' in d:
            o.country = d['country']
        if 'province' in d:
            o.province = d['province']
        return o


