#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPriceInfoDTO(object):

    def __init__(self):
        self._discounted_price = None
        self._order_price = None

    @property
    def discounted_price(self):
        return self._discounted_price

    @discounted_price.setter
    def discounted_price(self, value):
        self._discounted_price = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.discounted_price:
            if hasattr(self.discounted_price, 'to_alipay_dict'):
                params['discounted_price'] = self.discounted_price.to_alipay_dict()
            else:
                params['discounted_price'] = self.discounted_price
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPriceInfoDTO()
        if 'discounted_price' in d:
            o.discounted_price = d['discounted_price']
        if 'order_price' in d:
            o.order_price = d['order_price']
        return o


