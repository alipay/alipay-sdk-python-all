#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentProcurementPayItemInfoVO import RentProcurementPayItemInfoVO


class RentProcurementPriceInfoVO(object):

    def __init__(self):
        self._order_price = None
        self._pay_items = None

    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, value):
        if isinstance(value, list):
            self._pay_items = list()
            for i in value:
                if isinstance(i, RentProcurementPayItemInfoVO):
                    self._pay_items.append(i)
                else:
                    self._pay_items.append(RentProcurementPayItemInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.pay_items:
            if isinstance(self.pay_items, list):
                for i in range(0, len(self.pay_items)):
                    element = self.pay_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_items[i] = element.to_alipay_dict()
            if hasattr(self.pay_items, 'to_alipay_dict'):
                params['pay_items'] = self.pay_items.to_alipay_dict()
            else:
                params['pay_items'] = self.pay_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentProcurementPriceInfoVO()
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'pay_items' in d:
            o.pay_items = d['pay_items']
        return o


