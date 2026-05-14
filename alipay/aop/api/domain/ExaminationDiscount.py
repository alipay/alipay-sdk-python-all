#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExaminationDiscount(object):

    def __init__(self):
        self._amount_discount = None

    @property
    def amount_discount(self):
        return self._amount_discount

    @amount_discount.setter
    def amount_discount(self, value):
        self._amount_discount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_discount:
            if hasattr(self.amount_discount, 'to_alipay_dict'):
                params['amount_discount'] = self.amount_discount.to_alipay_dict()
            else:
                params['amount_discount'] = self.amount_discount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationDiscount()
        if 'amount_discount' in d:
            o.amount_discount = d['amount_discount']
        return o


