#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OilProductInfo(object):

    def __init__(self):
        self._discount_price = None
        self._listed_price = None
        self._oil_type = None

    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value
    @property
    def listed_price(self):
        return self._listed_price

    @listed_price.setter
    def listed_price(self, value):
        self._listed_price = value
    @property
    def oil_type(self):
        return self._oil_type

    @oil_type.setter
    def oil_type(self, value):
        self._oil_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_price:
            if hasattr(self.discount_price, 'to_alipay_dict'):
                params['discount_price'] = self.discount_price.to_alipay_dict()
            else:
                params['discount_price'] = self.discount_price
        if self.listed_price:
            if hasattr(self.listed_price, 'to_alipay_dict'):
                params['listed_price'] = self.listed_price.to_alipay_dict()
            else:
                params['listed_price'] = self.listed_price
        if self.oil_type:
            if hasattr(self.oil_type, 'to_alipay_dict'):
                params['oil_type'] = self.oil_type.to_alipay_dict()
            else:
                params['oil_type'] = self.oil_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OilProductInfo()
        if 'discount_price' in d:
            o.discount_price = d['discount_price']
        if 'listed_price' in d:
            o.listed_price = d['listed_price']
        if 'oil_type' in d:
            o.oil_type = d['oil_type']
        return o


