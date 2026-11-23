#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSubscriptionPaymentsettingSetModel(object):

    def __init__(self):
        self._payer_customer_id = None
        self._subscription_id = None

    @property
    def payer_customer_id(self):
        return self._payer_customer_id

    @payer_customer_id.setter
    def payer_customer_id(self, value):
        self._payer_customer_id = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.payer_customer_id:
            if hasattr(self.payer_customer_id, 'to_alipay_dict'):
                params['payer_customer_id'] = self.payer_customer_id.to_alipay_dict()
            else:
                params['payer_customer_id'] = self.payer_customer_id
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
        o = AlipayTradeSubscriptionPaymentsettingSetModel()
        if 'payer_customer_id' in d:
            o.payer_customer_id = d['payer_customer_id']
        if 'subscription_id' in d:
            o.subscription_id = d['subscription_id']
        return o


