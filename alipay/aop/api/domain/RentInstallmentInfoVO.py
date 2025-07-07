#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentInstallmentInfoVO(object):

    def __init__(self):
        self._buyout_price = None
        self._installment_no = None
        self._installment_price = None
        self._plan_pay_time = None

    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def installment_price(self):
        return self._installment_price

    @installment_price.setter
    def installment_price(self, value):
        self._installment_price = value
    @property
    def plan_pay_time(self):
        return self._plan_pay_time

    @plan_pay_time.setter
    def plan_pay_time(self, value):
        self._plan_pay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.installment_price:
            if hasattr(self.installment_price, 'to_alipay_dict'):
                params['installment_price'] = self.installment_price.to_alipay_dict()
            else:
                params['installment_price'] = self.installment_price
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
        o = RentInstallmentInfoVO()
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'installment_price' in d:
            o.installment_price = d['installment_price']
        if 'plan_pay_time' in d:
            o.plan_pay_time = d['plan_pay_time']
        return o


