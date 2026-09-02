#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscriptionReimbursementVO(object):

    def __init__(self):
        self._reason = None
        self._subscription = None
        self._valid = None
        self._year_month = None

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def subscription(self):
        return self._subscription

    @subscription.setter
    def subscription(self, value):
        self._subscription = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value
    @property
    def year_month(self):
        return self._year_month

    @year_month.setter
    def year_month(self, value):
        self._year_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.subscription:
            if hasattr(self.subscription, 'to_alipay_dict'):
                params['subscription'] = self.subscription.to_alipay_dict()
            else:
                params['subscription'] = self.subscription
        if self.valid:
            if hasattr(self.valid, 'to_alipay_dict'):
                params['valid'] = self.valid.to_alipay_dict()
            else:
                params['valid'] = self.valid
        if self.year_month:
            if hasattr(self.year_month, 'to_alipay_dict'):
                params['year_month'] = self.year_month.to_alipay_dict()
            else:
                params['year_month'] = self.year_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionReimbursementVO()
        if 'reason' in d:
            o.reason = d['reason']
        if 'subscription' in d:
            o.subscription = d['subscription']
        if 'valid' in d:
            o.valid = d['valid']
        if 'year_month' in d:
            o.year_month = d['year_month']
        return o


