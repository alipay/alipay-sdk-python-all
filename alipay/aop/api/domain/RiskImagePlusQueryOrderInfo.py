#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskImagePlusQueryOrderInfo(object):

    def __init__(self):
        self._order_items_name = None
        self._order_items_price = None
        self._order_items_quantity = None

    @property
    def order_items_name(self):
        return self._order_items_name

    @order_items_name.setter
    def order_items_name(self, value):
        self._order_items_name = value
    @property
    def order_items_price(self):
        return self._order_items_price

    @order_items_price.setter
    def order_items_price(self, value):
        self._order_items_price = value
    @property
    def order_items_quantity(self):
        return self._order_items_quantity

    @order_items_quantity.setter
    def order_items_quantity(self, value):
        self._order_items_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_items_name:
            if hasattr(self.order_items_name, 'to_alipay_dict'):
                params['order_items_name'] = self.order_items_name.to_alipay_dict()
            else:
                params['order_items_name'] = self.order_items_name
        if self.order_items_price:
            if hasattr(self.order_items_price, 'to_alipay_dict'):
                params['order_items_price'] = self.order_items_price.to_alipay_dict()
            else:
                params['order_items_price'] = self.order_items_price
        if self.order_items_quantity:
            if hasattr(self.order_items_quantity, 'to_alipay_dict'):
                params['order_items_quantity'] = self.order_items_quantity.to_alipay_dict()
            else:
                params['order_items_quantity'] = self.order_items_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskImagePlusQueryOrderInfo()
        if 'order_items_name' in d:
            o.order_items_name = d['order_items_name']
        if 'order_items_price' in d:
            o.order_items_price = d['order_items_price']
        if 'order_items_quantity' in d:
            o.order_items_quantity = d['order_items_quantity']
        return o


