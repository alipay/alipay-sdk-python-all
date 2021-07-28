#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OilStationDetails(object):

    def __init__(self):
        self._address = None
        self._discount_price = None
        self._oil_station_name = None
        self._oil_type = None
        self._poi_id = None
        self._sale_price = None
        self._shop_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value
    @property
    def oil_station_name(self):
        return self._oil_station_name

    @oil_station_name.setter
    def oil_station_name(self, value):
        self._oil_station_name = value
    @property
    def oil_type(self):
        return self._oil_type

    @oil_type.setter
    def oil_type(self, value):
        self._oil_type = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.discount_price:
            if hasattr(self.discount_price, 'to_alipay_dict'):
                params['discount_price'] = self.discount_price.to_alipay_dict()
            else:
                params['discount_price'] = self.discount_price
        if self.oil_station_name:
            if hasattr(self.oil_station_name, 'to_alipay_dict'):
                params['oil_station_name'] = self.oil_station_name.to_alipay_dict()
            else:
                params['oil_station_name'] = self.oil_station_name
        if self.oil_type:
            if hasattr(self.oil_type, 'to_alipay_dict'):
                params['oil_type'] = self.oil_type.to_alipay_dict()
            else:
                params['oil_type'] = self.oil_type
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OilStationDetails()
        if 'address' in d:
            o.address = d['address']
        if 'discount_price' in d:
            o.discount_price = d['discount_price']
        if 'oil_station_name' in d:
            o.oil_station_name = d['oil_station_name']
        if 'oil_type' in d:
            o.oil_type = d['oil_type']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


