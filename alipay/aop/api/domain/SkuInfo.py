#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuInfo(object):

    def __init__(self):
        self._price_cent = None
        self._reserve_price = None
        self._sku_id = None

    @property
    def price_cent(self):
        return self._price_cent

    @price_cent.setter
    def price_cent(self, value):
        self._price_cent = value
    @property
    def reserve_price(self):
        return self._reserve_price

    @reserve_price.setter
    def reserve_price(self, value):
        self._reserve_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.price_cent:
            if hasattr(self.price_cent, 'to_alipay_dict'):
                params['price_cent'] = self.price_cent.to_alipay_dict()
            else:
                params['price_cent'] = self.price_cent
        if self.reserve_price:
            if hasattr(self.reserve_price, 'to_alipay_dict'):
                params['reserve_price'] = self.reserve_price.to_alipay_dict()
            else:
                params['reserve_price'] = self.reserve_price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuInfo()
        if 'price_cent' in d:
            o.price_cent = d['price_cent']
        if 'reserve_price' in d:
            o.reserve_price = d['reserve_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


