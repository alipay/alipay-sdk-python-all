#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomInfo import CustomInfo
from alipay.aop.api.domain.CustomInfo import CustomInfo
from alipay.aop.api.domain.CustomInfo import CustomInfo


class PaymentBusinessInfo(object):

    def __init__(self):
        self._discounts = None
        self._other = None
        self._payments = None

    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, value):
        if isinstance(value, list):
            self._discounts = list()
            for i in value:
                if isinstance(i, CustomInfo):
                    self._discounts.append(i)
                else:
                    self._discounts.append(CustomInfo.from_alipay_dict(i))
    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        if isinstance(value, list):
            self._other = list()
            for i in value:
                if isinstance(i, CustomInfo):
                    self._other.append(i)
                else:
                    self._other.append(CustomInfo.from_alipay_dict(i))
    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, value):
        if isinstance(value, list):
            self._payments = list()
            for i in value:
                if isinstance(i, CustomInfo):
                    self._payments.append(i)
                else:
                    self._payments.append(CustomInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.discounts:
            if isinstance(self.discounts, list):
                for i in range(0, len(self.discounts)):
                    element = self.discounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discounts[i] = element.to_alipay_dict()
            if hasattr(self.discounts, 'to_alipay_dict'):
                params['discounts'] = self.discounts.to_alipay_dict()
            else:
                params['discounts'] = self.discounts
        if self.other:
            if isinstance(self.other, list):
                for i in range(0, len(self.other)):
                    element = self.other[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other[i] = element.to_alipay_dict()
            if hasattr(self.other, 'to_alipay_dict'):
                params['other'] = self.other.to_alipay_dict()
            else:
                params['other'] = self.other
        if self.payments:
            if isinstance(self.payments, list):
                for i in range(0, len(self.payments)):
                    element = self.payments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payments[i] = element.to_alipay_dict()
            if hasattr(self.payments, 'to_alipay_dict'):
                params['payments'] = self.payments.to_alipay_dict()
            else:
                params['payments'] = self.payments
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentBusinessInfo()
        if 'discounts' in d:
            o.discounts = d['discounts']
        if 'other' in d:
            o.other = d['other']
        if 'payments' in d:
            o.payments = d['payments']
        return o


