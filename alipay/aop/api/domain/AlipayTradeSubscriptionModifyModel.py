#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionItem import SubscriptionItem


class AlipayTradeSubscriptionModifyModel(object):

    def __init__(self):
        self._cancel_at_period_end = None
        self._description = None
        self._items = None
        self._subscribe_title = None
        self._subscription_id = None

    @property
    def cancel_at_period_end(self):
        return self._cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self._cancel_at_period_end = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
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
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_at_period_end:
            if hasattr(self.cancel_at_period_end, 'to_alipay_dict'):
                params['cancel_at_period_end'] = self.cancel_at_period_end.to_alipay_dict()
            else:
                params['cancel_at_period_end'] = self.cancel_at_period_end
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
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
        if self.subscription_id:
            if hasattr(self.subscription_id, 'to_alipay_dict'):
                params['subscription_id'] = self.subscription_id.to_alipay_dict()
            else:
                params['subscription_id'] = self.subscription_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSubscriptionModifyModel()
        if 'cancel_at_period_end' in d:
            o.cancel_at_period_end = d['cancel_at_period_end']
        if 'description' in d:
            o.description = d['description']
        if 'items' in d:
            o.items = d['items']
        if 'subscribe_title' in d:
            o.subscribe_title = d['subscribe_title']
        if 'subscription_id' in d:
            o.subscription_id = d['subscription_id']
        return o


