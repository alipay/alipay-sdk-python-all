#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EndowmentOrder(object):

    def __init__(self):
        self._apply_amount = None
        self._order_id = None
        self._pay_time = None
        self._ta_request_id = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def ta_request_id(self):
        return self._ta_request_id

    @ta_request_id.setter
    def ta_request_id(self, value):
        self._ta_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.ta_request_id:
            if hasattr(self.ta_request_id, 'to_alipay_dict'):
                params['ta_request_id'] = self.ta_request_id.to_alipay_dict()
            else:
                params['ta_request_id'] = self.ta_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EndowmentOrder()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'ta_request_id' in d:
            o.ta_request_id = d['ta_request_id']
        return o


