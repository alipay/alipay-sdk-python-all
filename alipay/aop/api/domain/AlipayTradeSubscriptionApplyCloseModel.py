#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSubscriptionApplyCloseModel(object):

    def __init__(self):
        self._order_no = None
        self._subscription_id = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        o = AlipayTradeSubscriptionApplyCloseModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'subscription_id' in d:
            o.subscription_id = d['subscription_id']
        return o


