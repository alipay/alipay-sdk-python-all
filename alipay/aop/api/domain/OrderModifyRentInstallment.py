#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderModifyRentInstallment(object):

    def __init__(self):
        self._installment_no = None
        self._plan_pay_time = None

    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def plan_pay_time(self):
        return self._plan_pay_time

    @plan_pay_time.setter
    def plan_pay_time(self, value):
        self._plan_pay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.plan_pay_time:
            if hasattr(self.plan_pay_time, 'to_alipay_dict'):
                params['plan_pay_time'] = self.plan_pay_time.to_alipay_dict()
            else:
                params['plan_pay_time'] = self.plan_pay_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderModifyRentInstallment()
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'plan_pay_time' in d:
            o.plan_pay_time = d['plan_pay_time']
        return o


