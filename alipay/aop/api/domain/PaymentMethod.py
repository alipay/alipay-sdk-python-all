#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentMethod(object):

    def __init__(self):
        self._customer_id = None
        self._open_id = None
        self._payment_method_type = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def payment_method_type(self):
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self._payment_method_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.payment_method_type:
            if hasattr(self.payment_method_type, 'to_alipay_dict'):
                params['payment_method_type'] = self.payment_method_type.to_alipay_dict()
            else:
                params['payment_method_type'] = self.payment_method_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentMethod()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'payment_method_type' in d:
            o.payment_method_type = d['payment_method_type']
        return o


