#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MakePriceCards(object):

    def __init__(self):
        self._base_price_cent = None
        self._expect_promo_price = None
        self._lower_promo_price = None
        self._product_type = None
        self._upper_promo_price = None

    @property
    def base_price_cent(self):
        return self._base_price_cent

    @base_price_cent.setter
    def base_price_cent(self, value):
        self._base_price_cent = value
    @property
    def expect_promo_price(self):
        return self._expect_promo_price

    @expect_promo_price.setter
    def expect_promo_price(self, value):
        self._expect_promo_price = value
    @property
    def lower_promo_price(self):
        return self._lower_promo_price

    @lower_promo_price.setter
    def lower_promo_price(self, value):
        self._lower_promo_price = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def upper_promo_price(self):
        return self._upper_promo_price

    @upper_promo_price.setter
    def upper_promo_price(self, value):
        self._upper_promo_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_price_cent:
            if hasattr(self.base_price_cent, 'to_alipay_dict'):
                params['base_price_cent'] = self.base_price_cent.to_alipay_dict()
            else:
                params['base_price_cent'] = self.base_price_cent
        if self.expect_promo_price:
            if hasattr(self.expect_promo_price, 'to_alipay_dict'):
                params['expect_promo_price'] = self.expect_promo_price.to_alipay_dict()
            else:
                params['expect_promo_price'] = self.expect_promo_price
        if self.lower_promo_price:
            if hasattr(self.lower_promo_price, 'to_alipay_dict'):
                params['lower_promo_price'] = self.lower_promo_price.to_alipay_dict()
            else:
                params['lower_promo_price'] = self.lower_promo_price
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.upper_promo_price:
            if hasattr(self.upper_promo_price, 'to_alipay_dict'):
                params['upper_promo_price'] = self.upper_promo_price.to_alipay_dict()
            else:
                params['upper_promo_price'] = self.upper_promo_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MakePriceCards()
        if 'base_price_cent' in d:
            o.base_price_cent = d['base_price_cent']
        if 'expect_promo_price' in d:
            o.expect_promo_price = d['expect_promo_price']
        if 'lower_promo_price' in d:
            o.lower_promo_price = d['lower_promo_price']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'upper_promo_price' in d:
            o.upper_promo_price = d['upper_promo_price']
        return o


