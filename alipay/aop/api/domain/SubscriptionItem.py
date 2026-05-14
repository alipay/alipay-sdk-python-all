#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscriptionItem(object):

    def __init__(self):
        self._coupon_id = None
        self._item_id = None
        self._price_id = None
        self._quantity = None
        self._source_quantity = None
        self._target_quantity = None

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
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def source_quantity(self):
        return self._source_quantity

    @source_quantity.setter
    def source_quantity(self, value):
        self._source_quantity = value
    @property
    def target_quantity(self):
        return self._target_quantity

    @target_quantity.setter
    def target_quantity(self, value):
        self._target_quantity = value


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
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.source_quantity:
            if hasattr(self.source_quantity, 'to_alipay_dict'):
                params['source_quantity'] = self.source_quantity.to_alipay_dict()
            else:
                params['source_quantity'] = self.source_quantity
        if self.target_quantity:
            if hasattr(self.target_quantity, 'to_alipay_dict'):
                params['target_quantity'] = self.target_quantity.to_alipay_dict()
            else:
                params['target_quantity'] = self.target_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionItem()
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'source_quantity' in d:
            o.source_quantity = d['source_quantity']
        if 'target_quantity' in d:
            o.target_quantity = d['target_quantity']
        return o


