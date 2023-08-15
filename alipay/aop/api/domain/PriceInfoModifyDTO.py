#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PriceInfoModifyDTO(object):

    def __init__(self):
        self._order_price = None

    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value


    def to_alipay_dict(self):
        params = dict()
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
        o = PriceInfoModifyDTO()
        if 'order_price' in d:
            o.order_price = d['order_price']
        return o


