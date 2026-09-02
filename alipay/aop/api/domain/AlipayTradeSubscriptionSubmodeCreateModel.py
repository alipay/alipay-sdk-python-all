#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionSubmodeItem import SubscriptionSubmodeItem


class AlipayTradeSubscriptionSubmodeCreateModel(object):

    def __init__(self):
        self._customer_id = None
        self._deduct_type = None
        self._items = None
        self._metadata = None
        self._pay_amount = None
        self._trial_desc = None
        self._trial_period_days = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def deduct_type(self):
        return self._deduct_type

    @deduct_type.setter
    def deduct_type(self, value):
        self._deduct_type = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, SubscriptionSubmodeItem):
                    self._items.append(i)
                else:
                    self._items.append(SubscriptionSubmodeItem.from_alipay_dict(i))
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def trial_desc(self):
        return self._trial_desc

    @trial_desc.setter
    def trial_desc(self, value):
        self._trial_desc = value
    @property
    def trial_period_days(self):
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, value):
        self._trial_period_days = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.deduct_type:
            if hasattr(self.deduct_type, 'to_alipay_dict'):
                params['deduct_type'] = self.deduct_type.to_alipay_dict()
            else:
                params['deduct_type'] = self.deduct_type
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
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.trial_desc:
            if hasattr(self.trial_desc, 'to_alipay_dict'):
                params['trial_desc'] = self.trial_desc.to_alipay_dict()
            else:
                params['trial_desc'] = self.trial_desc
        if self.trial_period_days:
            if hasattr(self.trial_period_days, 'to_alipay_dict'):
                params['trial_period_days'] = self.trial_period_days.to_alipay_dict()
            else:
                params['trial_period_days'] = self.trial_period_days
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSubscriptionSubmodeCreateModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'deduct_type' in d:
            o.deduct_type = d['deduct_type']
        if 'items' in d:
            o.items = d['items']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'trial_desc' in d:
            o.trial_desc = d['trial_desc']
        if 'trial_period_days' in d:
            o.trial_period_days = d['trial_period_days']
        return o


