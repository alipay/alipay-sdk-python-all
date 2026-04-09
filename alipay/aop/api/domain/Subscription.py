#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionQueryItem import SubscriptionQueryItem


class Subscription(object):

    def __init__(self):
        self._cancel_at_period_end = None
        self._canceled_date = None
        self._created = None
        self._current_period_end = None
        self._current_period_start = None
        self._customer_id = None
        self._items = None
        self._start_date = None
        self._subscribe_title = None
        self._subscription_id = None
        self._subscription_status = None

    @property
    def cancel_at_period_end(self):
        return self._cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self._cancel_at_period_end = value
    @property
    def canceled_date(self):
        return self._canceled_date

    @canceled_date.setter
    def canceled_date(self, value):
        self._canceled_date = value
    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value
    @property
    def current_period_end(self):
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self._current_period_end = value
    @property
    def current_period_start(self):
        return self._current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self._current_period_start = value
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
                if isinstance(i, SubscriptionQueryItem):
                    self._items.append(i)
                else:
                    self._items.append(SubscriptionQueryItem.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
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
    @property
    def subscription_status(self):
        return self._subscription_status

    @subscription_status.setter
    def subscription_status(self, value):
        self._subscription_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_at_period_end:
            if hasattr(self.cancel_at_period_end, 'to_alipay_dict'):
                params['cancel_at_period_end'] = self.cancel_at_period_end.to_alipay_dict()
            else:
                params['cancel_at_period_end'] = self.cancel_at_period_end
        if self.canceled_date:
            if hasattr(self.canceled_date, 'to_alipay_dict'):
                params['canceled_date'] = self.canceled_date.to_alipay_dict()
            else:
                params['canceled_date'] = self.canceled_date
        if self.created:
            if hasattr(self.created, 'to_alipay_dict'):
                params['created'] = self.created.to_alipay_dict()
            else:
                params['created'] = self.created
        if self.current_period_end:
            if hasattr(self.current_period_end, 'to_alipay_dict'):
                params['current_period_end'] = self.current_period_end.to_alipay_dict()
            else:
                params['current_period_end'] = self.current_period_end
        if self.current_period_start:
            if hasattr(self.current_period_start, 'to_alipay_dict'):
                params['current_period_start'] = self.current_period_start.to_alipay_dict()
            else:
                params['current_period_start'] = self.current_period_start
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
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
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
        if self.subscription_status:
            if hasattr(self.subscription_status, 'to_alipay_dict'):
                params['subscription_status'] = self.subscription_status.to_alipay_dict()
            else:
                params['subscription_status'] = self.subscription_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Subscription()
        if 'cancel_at_period_end' in d:
            o.cancel_at_period_end = d['cancel_at_period_end']
        if 'canceled_date' in d:
            o.canceled_date = d['canceled_date']
        if 'created' in d:
            o.created = d['created']
        if 'current_period_end' in d:
            o.current_period_end = d['current_period_end']
        if 'current_period_start' in d:
            o.current_period_start = d['current_period_start']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'items' in d:
            o.items = d['items']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'subscribe_title' in d:
            o.subscribe_title = d['subscribe_title']
        if 'subscription_id' in d:
            o.subscription_id = d['subscription_id']
        if 'subscription_status' in d:
            o.subscription_status = d['subscription_status']
        return o


