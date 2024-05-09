#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StagePayPlanInfoDTO(object):

    def __init__(self):
        self._plan_pay_no = None
        self._plan_pay_price = None
        self._plan_pay_time = None

    @property
    def plan_pay_no(self):
        return self._plan_pay_no

    @plan_pay_no.setter
    def plan_pay_no(self, value):
        self._plan_pay_no = value
    @property
    def plan_pay_price(self):
        return self._plan_pay_price

    @plan_pay_price.setter
    def plan_pay_price(self, value):
        self._plan_pay_price = value
    @property
    def plan_pay_time(self):
        return self._plan_pay_time

    @plan_pay_time.setter
    def plan_pay_time(self, value):
        self._plan_pay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.plan_pay_no:
            if hasattr(self.plan_pay_no, 'to_alipay_dict'):
                params['plan_pay_no'] = self.plan_pay_no.to_alipay_dict()
            else:
                params['plan_pay_no'] = self.plan_pay_no
        if self.plan_pay_price:
            if hasattr(self.plan_pay_price, 'to_alipay_dict'):
                params['plan_pay_price'] = self.plan_pay_price.to_alipay_dict()
            else:
                params['plan_pay_price'] = self.plan_pay_price
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
        o = StagePayPlanInfoDTO()
        if 'plan_pay_no' in d:
            o.plan_pay_no = d['plan_pay_no']
        if 'plan_pay_price' in d:
            o.plan_pay_price = d['plan_pay_price']
        if 'plan_pay_time' in d:
            o.plan_pay_time = d['plan_pay_time']
        return o


