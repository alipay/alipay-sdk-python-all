#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSubscriptionQueryModel(object):

    def __init__(self):
        self._customer_id = None
        self._subscription_id = None
        self._subscription_status = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
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
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
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
        o = AlipayTradeSubscriptionQueryModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'subscription_id' in d:
            o.subscription_id = d['subscription_id']
        if 'subscription_status' in d:
            o.subscription_status = d['subscription_status']
        return o


