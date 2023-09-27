#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DongCheDiDealerDetail(object):

    def __init__(self):
        self._address = None
        self._dealer_full_name = None
        self._dealer_id = None
        self._dealer_name = None
        self._dealer_type = None
        self._distance = None
        self._id = None
        self._max_dealer_price = None
        self._min_dealer_price = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def dealer_full_name(self):
        return self._dealer_full_name

    @dealer_full_name.setter
    def dealer_full_name(self, value):
        self._dealer_full_name = value
    @property
    def dealer_id(self):
        return self._dealer_id

    @dealer_id.setter
    def dealer_id(self, value):
        self._dealer_id = value
    @property
    def dealer_name(self):
        return self._dealer_name

    @dealer_name.setter
    def dealer_name(self, value):
        self._dealer_name = value
    @property
    def dealer_type(self):
        return self._dealer_type

    @dealer_type.setter
    def dealer_type(self, value):
        self._dealer_type = value
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
    def max_dealer_price(self):
        return self._max_dealer_price

    @max_dealer_price.setter
    def max_dealer_price(self, value):
        self._max_dealer_price = value
    @property
    def min_dealer_price(self):
        return self._min_dealer_price

    @min_dealer_price.setter
    def min_dealer_price(self, value):
        self._min_dealer_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.dealer_full_name:
            if hasattr(self.dealer_full_name, 'to_alipay_dict'):
                params['dealer_full_name'] = self.dealer_full_name.to_alipay_dict()
            else:
                params['dealer_full_name'] = self.dealer_full_name
        if self.dealer_id:
            if hasattr(self.dealer_id, 'to_alipay_dict'):
                params['dealer_id'] = self.dealer_id.to_alipay_dict()
            else:
                params['dealer_id'] = self.dealer_id
        if self.dealer_name:
            if hasattr(self.dealer_name, 'to_alipay_dict'):
                params['dealer_name'] = self.dealer_name.to_alipay_dict()
            else:
                params['dealer_name'] = self.dealer_name
        if self.dealer_type:
            if hasattr(self.dealer_type, 'to_alipay_dict'):
                params['dealer_type'] = self.dealer_type.to_alipay_dict()
            else:
                params['dealer_type'] = self.dealer_type
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
        if self.max_dealer_price:
            if hasattr(self.max_dealer_price, 'to_alipay_dict'):
                params['max_dealer_price'] = self.max_dealer_price.to_alipay_dict()
            else:
                params['max_dealer_price'] = self.max_dealer_price
        if self.min_dealer_price:
            if hasattr(self.min_dealer_price, 'to_alipay_dict'):
                params['min_dealer_price'] = self.min_dealer_price.to_alipay_dict()
            else:
                params['min_dealer_price'] = self.min_dealer_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DongCheDiDealerDetail()
        if 'address' in d:
            o.address = d['address']
        if 'dealer_full_name' in d:
            o.dealer_full_name = d['dealer_full_name']
        if 'dealer_id' in d:
            o.dealer_id = d['dealer_id']
        if 'dealer_name' in d:
            o.dealer_name = d['dealer_name']
        if 'dealer_type' in d:
            o.dealer_type = d['dealer_type']
        if 'distance' in d:
            o.distance = d['distance']
        if 'id' in d:
            o.id = d['id']
        if 'max_dealer_price' in d:
            o.max_dealer_price = d['max_dealer_price']
        if 'min_dealer_price' in d:
            o.min_dealer_price = d['min_dealer_price']
        return o


