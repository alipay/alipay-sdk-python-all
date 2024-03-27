#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentFactor(object):

    def __init__(self):
        self._is_cashier_payment = None
        self._is_in_store_payment = None

    @property
    def is_cashier_payment(self):
        return self._is_cashier_payment

    @is_cashier_payment.setter
    def is_cashier_payment(self, value):
        self._is_cashier_payment = value
    @property
    def is_in_store_payment(self):
        return self._is_in_store_payment

    @is_in_store_payment.setter
    def is_in_store_payment(self, value):
        self._is_in_store_payment = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_cashier_payment:
            if hasattr(self.is_cashier_payment, 'to_alipay_dict'):
                params['is_cashier_payment'] = self.is_cashier_payment.to_alipay_dict()
            else:
                params['is_cashier_payment'] = self.is_cashier_payment
        if self.is_in_store_payment:
            if hasattr(self.is_in_store_payment, 'to_alipay_dict'):
                params['is_in_store_payment'] = self.is_in_store_payment.to_alipay_dict()
            else:
                params['is_in_store_payment'] = self.is_in_store_payment
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentFactor()
        if 'is_cashier_payment' in d:
            o.is_cashier_payment = d['is_cashier_payment']
        if 'is_in_store_payment' in d:
            o.is_in_store_payment = d['is_in_store_payment']
        return o


