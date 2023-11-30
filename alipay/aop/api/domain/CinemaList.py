#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArrayList import ArrayList


class CinemaList(object):

    def __init__(self):
        self._address = None
        self._cinema_code = None
        self._distance = None
        self._id = None
        self._latitude = None
        self._longitude = None
        self._lowest_price = None
        self._market_price = None
        self._near_future = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def cinema_code(self):
        return self._cinema_code

    @cinema_code.setter
    def cinema_code(self, value):
        self._cinema_code = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
    def lowest_price(self):
        return self._lowest_price

    @lowest_price.setter
    def lowest_price(self, value):
        self._lowest_price = value
    @property
    def market_price(self):
        return self._market_price

    @market_price.setter
    def market_price(self, value):
        self._market_price = value
    @property
    def near_future(self):
        return self._near_future

    @near_future.setter
    def near_future(self, value):
        if isinstance(value, list):
            self._near_future = list()
            for i in value:
                if isinstance(i, ArrayList):
                    self._near_future.append(i)
                else:
                    self._near_future.append(ArrayList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.cinema_code:
            if hasattr(self.cinema_code, 'to_alipay_dict'):
                params['cinema_code'] = self.cinema_code.to_alipay_dict()
            else:
                params['cinema_code'] = self.cinema_code
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        if self.lowest_price:
            if hasattr(self.lowest_price, 'to_alipay_dict'):
                params['lowest_price'] = self.lowest_price.to_alipay_dict()
            else:
                params['lowest_price'] = self.lowest_price
        if self.market_price:
            if hasattr(self.market_price, 'to_alipay_dict'):
                params['market_price'] = self.market_price.to_alipay_dict()
            else:
                params['market_price'] = self.market_price
        if self.near_future:
            if isinstance(self.near_future, list):
                for i in range(0, len(self.near_future)):
                    element = self.near_future[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.near_future[i] = element.to_alipay_dict()
            if hasattr(self.near_future, 'to_alipay_dict'):
                params['near_future'] = self.near_future.to_alipay_dict()
            else:
                params['near_future'] = self.near_future
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CinemaList()
        if 'address' in d:
            o.address = d['address']
        if 'cinema_code' in d:
            o.cinema_code = d['cinema_code']
        if 'distance' in d:
            o.distance = d['distance']
        if 'id' in d:
            o.id = d['id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'lowest_price' in d:
            o.lowest_price = d['lowest_price']
        if 'market_price' in d:
            o.market_price = d['market_price']
        if 'near_future' in d:
            o.near_future = d['near_future']
        return o


