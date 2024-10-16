#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PeriodPayBillingRuleDynamicDTO(object):

    def __init__(self):
        self._cycle_hour = None
        self._deduction_date_type = None
        self._deduction_day = None
        self._down_payment_date = None
        self._period_num = None
        self._period_rent_amount_list = None
        self._period_unit = None

    @property
    def cycle_hour(self):
        return self._cycle_hour

    @cycle_hour.setter
    def cycle_hour(self, value):
        self._cycle_hour = value
    @property
    def deduction_date_type(self):
        return self._deduction_date_type

    @deduction_date_type.setter
    def deduction_date_type(self, value):
        self._deduction_date_type = value
    @property
    def deduction_day(self):
        return self._deduction_day

    @deduction_day.setter
    def deduction_day(self, value):
        self._deduction_day = value
    @property
    def down_payment_date(self):
        return self._down_payment_date

    @down_payment_date.setter
    def down_payment_date(self, value):
        self._down_payment_date = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def period_rent_amount_list(self):
        return self._period_rent_amount_list

    @period_rent_amount_list.setter
    def period_rent_amount_list(self, value):
        if isinstance(value, list):
            self._period_rent_amount_list = list()
            for i in value:
                self._period_rent_amount_list.append(i)
    @property
    def period_unit(self):
        return self._period_unit

    @period_unit.setter
    def period_unit(self, value):
        self._period_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_hour:
            if hasattr(self.cycle_hour, 'to_alipay_dict'):
                params['cycle_hour'] = self.cycle_hour.to_alipay_dict()
            else:
                params['cycle_hour'] = self.cycle_hour
        if self.deduction_date_type:
            if hasattr(self.deduction_date_type, 'to_alipay_dict'):
                params['deduction_date_type'] = self.deduction_date_type.to_alipay_dict()
            else:
                params['deduction_date_type'] = self.deduction_date_type
        if self.deduction_day:
            if hasattr(self.deduction_day, 'to_alipay_dict'):
                params['deduction_day'] = self.deduction_day.to_alipay_dict()
            else:
                params['deduction_day'] = self.deduction_day
        if self.down_payment_date:
            if hasattr(self.down_payment_date, 'to_alipay_dict'):
                params['down_payment_date'] = self.down_payment_date.to_alipay_dict()
            else:
                params['down_payment_date'] = self.down_payment_date
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.period_rent_amount_list:
            if isinstance(self.period_rent_amount_list, list):
                for i in range(0, len(self.period_rent_amount_list)):
                    element = self.period_rent_amount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_rent_amount_list[i] = element.to_alipay_dict()
            if hasattr(self.period_rent_amount_list, 'to_alipay_dict'):
                params['period_rent_amount_list'] = self.period_rent_amount_list.to_alipay_dict()
            else:
                params['period_rent_amount_list'] = self.period_rent_amount_list
        if self.period_unit:
            if hasattr(self.period_unit, 'to_alipay_dict'):
                params['period_unit'] = self.period_unit.to_alipay_dict()
            else:
                params['period_unit'] = self.period_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PeriodPayBillingRuleDynamicDTO()
        if 'cycle_hour' in d:
            o.cycle_hour = d['cycle_hour']
        if 'deduction_date_type' in d:
            o.deduction_date_type = d['deduction_date_type']
        if 'deduction_day' in d:
            o.deduction_day = d['deduction_day']
        if 'down_payment_date' in d:
            o.down_payment_date = d['down_payment_date']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'period_rent_amount_list' in d:
            o.period_rent_amount_list = d['period_rent_amount_list']
        if 'period_unit' in d:
            o.period_unit = d['period_unit']
        return o


