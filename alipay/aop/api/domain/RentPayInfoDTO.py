#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayInfoDTO(object):

    def __init__(self):
        self._act_pay_amount = None
        self._act_pay_time = None
        self._fund_type = None
        self._period = None
        self._promo_amount = None
        self._stage = None

    @property
    def act_pay_amount(self):
        return self._act_pay_amount

    @act_pay_amount.setter
    def act_pay_amount(self, value):
        self._act_pay_amount = value
    @property
    def act_pay_time(self):
        return self._act_pay_time

    @act_pay_time.setter
    def act_pay_time(self, value):
        self._act_pay_time = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def promo_amount(self):
        return self._promo_amount

    @promo_amount.setter
    def promo_amount(self, value):
        self._promo_amount = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value


    def to_alipay_dict(self):
        params = dict()
        if self.act_pay_amount:
            if hasattr(self.act_pay_amount, 'to_alipay_dict'):
                params['act_pay_amount'] = self.act_pay_amount.to_alipay_dict()
            else:
                params['act_pay_amount'] = self.act_pay_amount
        if self.act_pay_time:
            if hasattr(self.act_pay_time, 'to_alipay_dict'):
                params['act_pay_time'] = self.act_pay_time.to_alipay_dict()
            else:
                params['act_pay_time'] = self.act_pay_time
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.promo_amount:
            if hasattr(self.promo_amount, 'to_alipay_dict'):
                params['promo_amount'] = self.promo_amount.to_alipay_dict()
            else:
                params['promo_amount'] = self.promo_amount
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
        o = RentPayInfoDTO()
        if 'act_pay_amount' in d:
            o.act_pay_amount = d['act_pay_amount']
        if 'act_pay_time' in d:
            o.act_pay_time = d['act_pay_time']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'period' in d:
            o.period = d['period']
        if 'promo_amount' in d:
            o.promo_amount = d['promo_amount']
        if 'stage' in d:
            o.stage = d['stage']
        return o


