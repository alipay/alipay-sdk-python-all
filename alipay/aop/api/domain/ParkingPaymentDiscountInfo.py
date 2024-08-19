#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingPaymentDiscountInfo(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_type = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingPaymentDiscountInfo()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        return o


