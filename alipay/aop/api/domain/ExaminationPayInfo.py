#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExaminationPayInfo(object):

    def __init__(self):
        self._amount_discount = None
        self._pay_time = None

    @property
    def amount_discount(self):
        return self._amount_discount

    @amount_discount.setter
    def amount_discount(self, value):
        self._amount_discount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_discount:
            if hasattr(self.amount_discount, 'to_alipay_dict'):
                params['amount_discount'] = self.amount_discount.to_alipay_dict()
            else:
                params['amount_discount'] = self.amount_discount
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationPayInfo()
        if 'amount_discount' in d:
            o.amount_discount = d['amount_discount']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        return o


