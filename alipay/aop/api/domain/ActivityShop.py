#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityShop(object):

    def __init__(self):
        self._shop_address = None
        self._shop_id = None
        self._shop_latitude = None
        self._shop_longitude = None
        self._shop_name = None

    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_latitude(self):
        return self._shop_latitude

    @shop_latitude.setter
    def shop_latitude(self, value):
        self._shop_latitude = value
    @property
    def shop_longitude(self):
        return self._shop_longitude

    @shop_longitude.setter
    def shop_longitude(self, value):
        self._shop_longitude = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_latitude:
            if hasattr(self.shop_latitude, 'to_alipay_dict'):
                params['shop_latitude'] = self.shop_latitude.to_alipay_dict()
            else:
                params['shop_latitude'] = self.shop_latitude
        if self.shop_longitude:
            if hasattr(self.shop_longitude, 'to_alipay_dict'):
                params['shop_longitude'] = self.shop_longitude.to_alipay_dict()
            else:
                params['shop_longitude'] = self.shop_longitude
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityShop()
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_latitude' in d:
            o.shop_latitude = d['shop_latitude']
        if 'shop_longitude' in d:
            o.shop_longitude = d['shop_longitude']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


