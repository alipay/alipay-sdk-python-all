#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceAddressSimpleVO(object):

    def __init__(self):
        self._latitude = None
        self._longitude = None
        self._poi_address = None
        self._poi_code = None
        self._poi_name = None

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def poi_address(self):
        return self._poi_address

    @poi_address.setter
    def poi_address(self, value):
        self._poi_address = value
    @property
    def poi_code(self):
        return self._poi_code

    @poi_code.setter
    def poi_code(self, value):
        self._poi_code = value
    @property
    def poi_name(self):
        return self._poi_name

    @poi_name.setter
    def poi_name(self, value):
        self._poi_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.poi_address:
            if hasattr(self.poi_address, 'to_alipay_dict'):
                params['poi_address'] = self.poi_address.to_alipay_dict()
            else:
                params['poi_address'] = self.poi_address
        if self.poi_code:
            if hasattr(self.poi_code, 'to_alipay_dict'):
                params['poi_code'] = self.poi_code.to_alipay_dict()
            else:
                params['poi_code'] = self.poi_code
        if self.poi_name:
            if hasattr(self.poi_name, 'to_alipay_dict'):
                params['poi_name'] = self.poi_name.to_alipay_dict()
            else:
                params['poi_name'] = self.poi_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceAddressSimpleVO()
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'poi_address' in d:
            o.poi_address = d['poi_address']
        if 'poi_code' in d:
            o.poi_code = d['poi_code']
        if 'poi_name' in d:
            o.poi_name = d['poi_name']
        return o


