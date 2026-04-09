#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NexusPayPrice import NexusPayPrice


class SubscriptionQueryItem(object):

    def __init__(self):
        self._created = None
        self._item_id = None
        self._price = None
        self._quantity = None

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, NexusPayPrice):
            self._price = value
        else:
            self._price = NexusPayPrice.from_alipay_dict(value)
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.created:
            if hasattr(self.created, 'to_alipay_dict'):
                params['created'] = self.created.to_alipay_dict()
            else:
                params['created'] = self.created
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
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
        o = SubscriptionQueryItem()
        if 'created' in d:
            o.created = d['created']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o


