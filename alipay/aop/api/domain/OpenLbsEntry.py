#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenLbsEntry(object):

    def __init__(self):
        self._address = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._radius = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenLbsEntry()
        if 'address' in d:
            o.address = d['address']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'radius' in d:
            o.radius = d['radius']
        return o


