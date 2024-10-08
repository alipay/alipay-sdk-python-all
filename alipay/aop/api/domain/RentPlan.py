#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPlan(object):

    def __init__(self):
        self._actual_pay_time = None
        self._buyout_price = None
        self._expect_pay_time = None
        self._installment_id = None
        self._period = None
        self._plan_status = None
        self._rent_price = None
        self._stage = None

    @property
    def actual_pay_time(self):
        return self._actual_pay_time

    @actual_pay_time.setter
    def actual_pay_time(self, value):
        self._actual_pay_time = value
    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def expect_pay_time(self):
        return self._expect_pay_time

    @expect_pay_time.setter
    def expect_pay_time(self, value):
        self._expect_pay_time = value
    @property
    def installment_id(self):
        return self._installment_id

    @installment_id.setter
    def installment_id(self, value):
        self._installment_id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def rent_price(self):
        return self._rent_price

    @rent_price.setter
    def rent_price(self, value):
        self._rent_price = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_pay_time:
            if hasattr(self.actual_pay_time, 'to_alipay_dict'):
                params['actual_pay_time'] = self.actual_pay_time.to_alipay_dict()
            else:
                params['actual_pay_time'] = self.actual_pay_time
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.expect_pay_time:
            if hasattr(self.expect_pay_time, 'to_alipay_dict'):
                params['expect_pay_time'] = self.expect_pay_time.to_alipay_dict()
            else:
                params['expect_pay_time'] = self.expect_pay_time
        if self.installment_id:
            if hasattr(self.installment_id, 'to_alipay_dict'):
                params['installment_id'] = self.installment_id.to_alipay_dict()
            else:
                params['installment_id'] = self.installment_id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.plan_status:
            if hasattr(self.plan_status, 'to_alipay_dict'):
                params['plan_status'] = self.plan_status.to_alipay_dict()
            else:
                params['plan_status'] = self.plan_status
        if self.rent_price:
            if hasattr(self.rent_price, 'to_alipay_dict'):
                params['rent_price'] = self.rent_price.to_alipay_dict()
            else:
                params['rent_price'] = self.rent_price
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPlan()
        if 'actual_pay_time' in d:
            o.actual_pay_time = d['actual_pay_time']
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'expect_pay_time' in d:
            o.expect_pay_time = d['expect_pay_time']
        if 'installment_id' in d:
            o.installment_id = d['installment_id']
        if 'period' in d:
            o.period = d['period']
        if 'plan_status' in d:
            o.plan_status = d['plan_status']
        if 'rent_price' in d:
            o.rent_price = d['rent_price']
        if 'stage' in d:
            o.stage = d['stage']
        return o


