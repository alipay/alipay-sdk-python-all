#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TapPayInfo(object):

    def __init__(self):
        self._payment_medium_type = None
        self._total_discount_amount = None
        self._total_discount_name = None

    @property
    def payment_medium_type(self):
        return self._payment_medium_type

    @payment_medium_type.setter
    def payment_medium_type(self, value):
        self._payment_medium_type = value
    @property
    def total_discount_amount(self):
        return self._total_discount_amount

    @total_discount_amount.setter
    def total_discount_amount(self, value):
        self._total_discount_amount = value
    @property
    def total_discount_name(self):
        return self._total_discount_name

    @total_discount_name.setter
    def total_discount_name(self, value):
        self._total_discount_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_medium_type:
            if hasattr(self.payment_medium_type, 'to_alipay_dict'):
                params['payment_medium_type'] = self.payment_medium_type.to_alipay_dict()
            else:
                params['payment_medium_type'] = self.payment_medium_type
        if self.total_discount_amount:
            if hasattr(self.total_discount_amount, 'to_alipay_dict'):
                params['total_discount_amount'] = self.total_discount_amount.to_alipay_dict()
            else:
                params['total_discount_amount'] = self.total_discount_amount
        if self.total_discount_name:
            if hasattr(self.total_discount_name, 'to_alipay_dict'):
                params['total_discount_name'] = self.total_discount_name.to_alipay_dict()
            else:
                params['total_discount_name'] = self.total_discount_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TapPayInfo()
        if 'payment_medium_type' in d:
            o.payment_medium_type = d['payment_medium_type']
        if 'total_discount_amount' in d:
            o.total_discount_amount = d['total_discount_amount']
        if 'total_discount_name' in d:
            o.total_discount_name = d['total_discount_name']
        return o


