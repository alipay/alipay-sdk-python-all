#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentFactor import PaymentFactor
from alipay.aop.api.domain.PaymentMethod import PaymentMethod


class AlipayOverseasPaymentsEvaluateModel(object):

    def __init__(self):
        self._payment_factor = None
        self._payment_method = None
        self._total_amount = None

    @property
    def payment_factor(self):
        return self._payment_factor

    @payment_factor.setter
    def payment_factor(self, value):
        if isinstance(value, PaymentFactor):
            self._payment_factor = value
        else:
            self._payment_factor = PaymentFactor.from_alipay_dict(value)
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        if isinstance(value, PaymentMethod):
            self._payment_method = value
        else:
            self._payment_method = PaymentMethod.from_alipay_dict(value)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_factor:
            if hasattr(self.payment_factor, 'to_alipay_dict'):
                params['payment_factor'] = self.payment_factor.to_alipay_dict()
            else:
                params['payment_factor'] = self.payment_factor
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasPaymentsEvaluateModel()
        if 'payment_factor' in d:
            o.payment_factor = d['payment_factor']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


