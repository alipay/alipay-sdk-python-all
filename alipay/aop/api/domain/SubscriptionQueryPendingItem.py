#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NexusPayPrice import NexusPayPrice


class SubscriptionQueryPendingItem(object):

    def __init__(self):
        self._created = None
        self._item_id = None
        self._period_end = None
        self._period_start = None
        self._price = None
        self._quantity = None
        self._status = None

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
    def period_end(self):
        return self._period_end

    @period_end.setter
    def period_end(self, value):
        self._period_end = value
    @property
    def period_start(self):
        return self._period_start

    @period_start.setter
    def period_start(self, value):
        self._period_start = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


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
        if self.period_end:
            if hasattr(self.period_end, 'to_alipay_dict'):
                params['period_end'] = self.period_end.to_alipay_dict()
            else:
                params['period_end'] = self.period_end
        if self.period_start:
            if hasattr(self.period_start, 'to_alipay_dict'):
                params['period_start'] = self.period_start.to_alipay_dict()
            else:
                params['period_start'] = self.period_start
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionQueryPendingItem()
        if 'created' in d:
            o.created = d['created']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'period_end' in d:
            o.period_end = d['period_end']
        if 'period_start' in d:
            o.period_start = d['period_start']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'status' in d:
            o.status = d['status']
        return o


