#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PriceInfoModifyDTO(object):

    def __init__(self):
        self._order_price = None
        self._real_order_price = None

    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def real_order_price(self):
        return self._real_order_price

    @real_order_price.setter
    def real_order_price(self, value):
        self._real_order_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.real_order_price:
            if hasattr(self.real_order_price, 'to_alipay_dict'):
                params['real_order_price'] = self.real_order_price.to_alipay_dict()
            else:
                params['real_order_price'] = self.real_order_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PriceInfoModifyDTO()
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'real_order_price' in d:
            o.real_order_price = d['real_order_price']
        return o


