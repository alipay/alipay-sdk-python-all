#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PositionPoint(object):

    def __init__(self):
        self._address = None
        self._latitude = None
        self._longitude = None
        self._order_count = None
        self._radius = None
        self._tag = None
        self._taxi_count = None

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
    def order_count(self):
        return self._order_count

    @order_count.setter
    def order_count(self, value):
        self._order_count = value
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def taxi_count(self):
        return self._taxi_count

    @taxi_count.setter
    def taxi_count(self, value):
        self._taxi_count = value


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
        if self.order_count:
            if hasattr(self.order_count, 'to_alipay_dict'):
                params['order_count'] = self.order_count.to_alipay_dict()
            else:
                params['order_count'] = self.order_count
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.taxi_count:
            if hasattr(self.taxi_count, 'to_alipay_dict'):
                params['taxi_count'] = self.taxi_count.to_alipay_dict()
            else:
                params['taxi_count'] = self.taxi_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PositionPoint()
        if 'address' in d:
            o.address = d['address']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'order_count' in d:
            o.order_count = d['order_count']
        if 'radius' in d:
            o.radius = d['radius']
        if 'tag' in d:
            o.tag = d['tag']
        if 'taxi_count' in d:
            o.taxi_count = d['taxi_count']
        return o


