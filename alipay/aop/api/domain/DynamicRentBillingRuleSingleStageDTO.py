#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DynamicRentBillingRuleSingleStageDTO(object):

    def __init__(self):
        self._billing_cap = None
        self._cycle_hour = None
        self._period_rent_amount = None
        self._period_unit = None
        self._period_unit_num = None

    @property
    def billing_cap(self):
        return self._billing_cap

    @billing_cap.setter
    def billing_cap(self, value):
        self._billing_cap = value
    @property
    def cycle_hour(self):
        return self._cycle_hour

    @cycle_hour.setter
    def cycle_hour(self, value):
        self._cycle_hour = value
    @property
    def period_rent_amount(self):
        return self._period_rent_amount

    @period_rent_amount.setter
    def period_rent_amount(self, value):
        self._period_rent_amount = value
    @property
    def period_unit(self):
        return self._period_unit

    @period_unit.setter
    def period_unit(self, value):
        self._period_unit = value
    @property
    def period_unit_num(self):
        return self._period_unit_num

    @period_unit_num.setter
    def period_unit_num(self, value):
        self._period_unit_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.billing_cap:
            if hasattr(self.billing_cap, 'to_alipay_dict'):
                params['billing_cap'] = self.billing_cap.to_alipay_dict()
            else:
                params['billing_cap'] = self.billing_cap
        if self.cycle_hour:
            if hasattr(self.cycle_hour, 'to_alipay_dict'):
                params['cycle_hour'] = self.cycle_hour.to_alipay_dict()
            else:
                params['cycle_hour'] = self.cycle_hour
        if self.period_rent_amount:
            if hasattr(self.period_rent_amount, 'to_alipay_dict'):
                params['period_rent_amount'] = self.period_rent_amount.to_alipay_dict()
            else:
                params['period_rent_amount'] = self.period_rent_amount
        if self.period_unit:
            if hasattr(self.period_unit, 'to_alipay_dict'):
                params['period_unit'] = self.period_unit.to_alipay_dict()
            else:
                params['period_unit'] = self.period_unit
        if self.period_unit_num:
            if hasattr(self.period_unit_num, 'to_alipay_dict'):
                params['period_unit_num'] = self.period_unit_num.to_alipay_dict()
            else:
                params['period_unit_num'] = self.period_unit_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DynamicRentBillingRuleSingleStageDTO()
        if 'billing_cap' in d:
            o.billing_cap = d['billing_cap']
        if 'cycle_hour' in d:
            o.cycle_hour = d['cycle_hour']
        if 'period_rent_amount' in d:
            o.period_rent_amount = d['period_rent_amount']
        if 'period_unit' in d:
            o.period_unit = d['period_unit']
        if 'period_unit_num' in d:
            o.period_unit_num = d['period_unit_num']
        return o


