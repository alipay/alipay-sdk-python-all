#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthDiscountInfo(object):

    def __init__(self):
        self._discount = None
        self._equity_discount_type = None

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def equity_discount_type(self):
        return self._equity_discount_type

    @equity_discount_type.setter
    def equity_discount_type(self, value):
        self._equity_discount_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.equity_discount_type:
            if hasattr(self.equity_discount_type, 'to_alipay_dict'):
                params['equity_discount_type'] = self.equity_discount_type.to_alipay_dict()
            else:
                params['equity_discount_type'] = self.equity_discount_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthDiscountInfo()
        if 'discount' in d:
            o.discount = d['discount']
        if 'equity_discount_type' in d:
            o.equity_discount_type = d['equity_discount_type']
        return o


