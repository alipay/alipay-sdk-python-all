#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscriptionMonthPair(object):

    def __init__(self):
        self._month = None
        self._subscription = None

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def subscription(self):
        return self._subscription

    @subscription.setter
    def subscription(self, value):
        self._subscription = value


    def to_alipay_dict(self):
        params = dict()
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.subscription:
            if hasattr(self.subscription, 'to_alipay_dict'):
                params['subscription'] = self.subscription.to_alipay_dict()
            else:
                params['subscription'] = self.subscription
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionMonthPair()
        if 'month' in d:
            o.month = d['month']
        if 'subscription' in d:
            o.subscription = d['subscription']
        return o


