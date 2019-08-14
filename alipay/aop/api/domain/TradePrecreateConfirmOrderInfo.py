#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradePrecreateConfirmOrderInfo(object):

    def __init__(self):
        self._body = None
        self._pay_expire_time = None
        self._quantity = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def pay_expire_time(self):
        return self._pay_expire_time

    @pay_expire_time.setter
    def pay_expire_time(self, value):
        self._pay_expire_time = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.pay_expire_time:
            if hasattr(self.pay_expire_time, 'to_alipay_dict'):
                params['pay_expire_time'] = self.pay_expire_time.to_alipay_dict()
            else:
                params['pay_expire_time'] = self.pay_expire_time
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradePrecreateConfirmOrderInfo()
        if 'body' in d:
            o.body = d['body']
        if 'pay_expire_time' in d:
            o.pay_expire_time = d['pay_expire_time']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o


