#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnfreezeExtendParams(object):

    def __init__(self):
        self._quit_type = None
        self._total_discount_amount = None
        self._total_real_pay_amount = None
        self._total_task_count = None

    @property
    def quit_type(self):
        return self._quit_type

    @quit_type.setter
    def quit_type(self, value):
        self._quit_type = value
    @property
    def total_discount_amount(self):
        return self._total_discount_amount

    @total_discount_amount.setter
    def total_discount_amount(self, value):
        self._total_discount_amount = value
    @property
    def total_real_pay_amount(self):
        return self._total_real_pay_amount

    @total_real_pay_amount.setter
    def total_real_pay_amount(self, value):
        self._total_real_pay_amount = value
    @property
    def total_task_count(self):
        return self._total_task_count

    @total_task_count.setter
    def total_task_count(self, value):
        self._total_task_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.quit_type:
            if hasattr(self.quit_type, 'to_alipay_dict'):
                params['quit_type'] = self.quit_type.to_alipay_dict()
            else:
                params['quit_type'] = self.quit_type
        if self.total_discount_amount:
            if hasattr(self.total_discount_amount, 'to_alipay_dict'):
                params['total_discount_amount'] = self.total_discount_amount.to_alipay_dict()
            else:
                params['total_discount_amount'] = self.total_discount_amount
        if self.total_real_pay_amount:
            if hasattr(self.total_real_pay_amount, 'to_alipay_dict'):
                params['total_real_pay_amount'] = self.total_real_pay_amount.to_alipay_dict()
            else:
                params['total_real_pay_amount'] = self.total_real_pay_amount
        if self.total_task_count:
            if hasattr(self.total_task_count, 'to_alipay_dict'):
                params['total_task_count'] = self.total_task_count.to_alipay_dict()
            else:
                params['total_task_count'] = self.total_task_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnfreezeExtendParams()
        if 'quit_type' in d:
            o.quit_type = d['quit_type']
        if 'total_discount_amount' in d:
            o.total_discount_amount = d['total_discount_amount']
        if 'total_real_pay_amount' in d:
            o.total_real_pay_amount = d['total_real_pay_amount']
        if 'total_task_count' in d:
            o.total_task_count = d['total_task_count']
        return o


