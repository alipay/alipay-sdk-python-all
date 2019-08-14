#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MakePriceResult(object):

    def __init__(self):
        self._base_price_cent = None
        self._product_type = None
        self._promo_price = None

    @property
    def base_price_cent(self):
        return self._base_price_cent

    @base_price_cent.setter
    def base_price_cent(self, value):
        self._base_price_cent = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def promo_price(self):
        return self._promo_price

    @promo_price.setter
    def promo_price(self, value):
        self._promo_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_price_cent:
            if hasattr(self.base_price_cent, 'to_alipay_dict'):
                params['base_price_cent'] = self.base_price_cent.to_alipay_dict()
            else:
                params['base_price_cent'] = self.base_price_cent
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.promo_price:
            if hasattr(self.promo_price, 'to_alipay_dict'):
                params['promo_price'] = self.promo_price.to_alipay_dict()
            else:
                params['promo_price'] = self.promo_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MakePriceResult()
        if 'base_price_cent' in d:
            o.base_price_cent = d['base_price_cent']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'promo_price' in d:
            o.promo_price = d['promo_price']
        return o


