#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionPriceData import SubscriptionPriceData


class SubscriptionSubmodeItem(object):

    def __init__(self):
        self._coupon_id = None
        self._item_id = None
        self._price_data = None
        self._quantity = None

    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def price_data(self):
        return self._price_data

    @price_data.setter
    def price_data(self, value):
        if isinstance(value, SubscriptionPriceData):
            self._price_data = value
        else:
            self._price_data = SubscriptionPriceData.from_alipay_dict(value)
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_id:
            if hasattr(self.coupon_id, 'to_alipay_dict'):
                params['coupon_id'] = self.coupon_id.to_alipay_dict()
            else:
                params['coupon_id'] = self.coupon_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.price_data:
            if hasattr(self.price_data, 'to_alipay_dict'):
                params['price_data'] = self.price_data.to_alipay_dict()
            else:
                params['price_data'] = self.price_data
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionSubmodeItem()
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price_data' in d:
            o.price_data = d['price_data']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o


