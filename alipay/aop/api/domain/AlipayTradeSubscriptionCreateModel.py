#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionItem import SubscriptionItem


class AlipayTradeSubscriptionCreateModel(object):

    def __init__(self):
        self._customer_id = None
        self._items = None
        self._subscribe_title = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, SubscriptionItem):
                    self._items.append(i)
                else:
                    self._items.append(SubscriptionItem.from_alipay_dict(i))
    @property
    def subscribe_title(self):
        return self._subscribe_title

    @subscribe_title.setter
    def subscribe_title(self, value):
        self._subscribe_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.subscribe_title:
            if hasattr(self.subscribe_title, 'to_alipay_dict'):
                params['subscribe_title'] = self.subscribe_title.to_alipay_dict()
            else:
                params['subscribe_title'] = self.subscribe_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSubscriptionCreateModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'items' in d:
            o.items = d['items']
        if 'subscribe_title' in d:
            o.subscribe_title = d['subscribe_title']
        return o


