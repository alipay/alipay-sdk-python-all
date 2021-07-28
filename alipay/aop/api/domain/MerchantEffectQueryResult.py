#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantEffectQueryResult(object):

    def __init__(self):
        self._accumulative_recharge_nums = None
        self._accumulative_total_allowance = None
        self._accumulative_total_days = None
        self._accumulative_total_income = None
        self._average_recharge_allowance_rate = None
        self._date = None
        self._effective_increased_income = None
        self._increased_income = None
        self._merchant_allowance = None
        self._merchant_income = None
        self._use_rate = None

    @property
    def accumulative_recharge_nums(self):
        return self._accumulative_recharge_nums

    @accumulative_recharge_nums.setter
    def accumulative_recharge_nums(self, value):
        self._accumulative_recharge_nums = value
    @property
    def accumulative_total_allowance(self):
        return self._accumulative_total_allowance

    @accumulative_total_allowance.setter
    def accumulative_total_allowance(self, value):
        self._accumulative_total_allowance = value
    @property
    def accumulative_total_days(self):
        return self._accumulative_total_days

    @accumulative_total_days.setter
    def accumulative_total_days(self, value):
        self._accumulative_total_days = value
    @property
    def accumulative_total_income(self):
        return self._accumulative_total_income

    @accumulative_total_income.setter
    def accumulative_total_income(self, value):
        self._accumulative_total_income = value
    @property
    def average_recharge_allowance_rate(self):
        return self._average_recharge_allowance_rate

    @average_recharge_allowance_rate.setter
    def average_recharge_allowance_rate(self, value):
        self._average_recharge_allowance_rate = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def effective_increased_income(self):
        return self._effective_increased_income

    @effective_increased_income.setter
    def effective_increased_income(self, value):
        self._effective_increased_income = value
    @property
    def increased_income(self):
        return self._increased_income

    @increased_income.setter
    def increased_income(self, value):
        self._increased_income = value
    @property
    def merchant_allowance(self):
        return self._merchant_allowance

    @merchant_allowance.setter
    def merchant_allowance(self, value):
        self._merchant_allowance = value
    @property
    def merchant_income(self):
        return self._merchant_income

    @merchant_income.setter
    def merchant_income(self, value):
        self._merchant_income = value
    @property
    def use_rate(self):
        return self._use_rate

    @use_rate.setter
    def use_rate(self, value):
        self._use_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.accumulative_recharge_nums:
            if hasattr(self.accumulative_recharge_nums, 'to_alipay_dict'):
                params['accumulative_recharge_nums'] = self.accumulative_recharge_nums.to_alipay_dict()
            else:
                params['accumulative_recharge_nums'] = self.accumulative_recharge_nums
        if self.accumulative_total_allowance:
            if hasattr(self.accumulative_total_allowance, 'to_alipay_dict'):
                params['accumulative_total_allowance'] = self.accumulative_total_allowance.to_alipay_dict()
            else:
                params['accumulative_total_allowance'] = self.accumulative_total_allowance
        if self.accumulative_total_days:
            if hasattr(self.accumulative_total_days, 'to_alipay_dict'):
                params['accumulative_total_days'] = self.accumulative_total_days.to_alipay_dict()
            else:
                params['accumulative_total_days'] = self.accumulative_total_days
        if self.accumulative_total_income:
            if hasattr(self.accumulative_total_income, 'to_alipay_dict'):
                params['accumulative_total_income'] = self.accumulative_total_income.to_alipay_dict()
            else:
                params['accumulative_total_income'] = self.accumulative_total_income
        if self.average_recharge_allowance_rate:
            if hasattr(self.average_recharge_allowance_rate, 'to_alipay_dict'):
                params['average_recharge_allowance_rate'] = self.average_recharge_allowance_rate.to_alipay_dict()
            else:
                params['average_recharge_allowance_rate'] = self.average_recharge_allowance_rate
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.effective_increased_income:
            if hasattr(self.effective_increased_income, 'to_alipay_dict'):
                params['effective_increased_income'] = self.effective_increased_income.to_alipay_dict()
            else:
                params['effective_increased_income'] = self.effective_increased_income
        if self.increased_income:
            if hasattr(self.increased_income, 'to_alipay_dict'):
                params['increased_income'] = self.increased_income.to_alipay_dict()
            else:
                params['increased_income'] = self.increased_income
        if self.merchant_allowance:
            if hasattr(self.merchant_allowance, 'to_alipay_dict'):
                params['merchant_allowance'] = self.merchant_allowance.to_alipay_dict()
            else:
                params['merchant_allowance'] = self.merchant_allowance
        if self.merchant_income:
            if hasattr(self.merchant_income, 'to_alipay_dict'):
                params['merchant_income'] = self.merchant_income.to_alipay_dict()
            else:
                params['merchant_income'] = self.merchant_income
        if self.use_rate:
            if hasattr(self.use_rate, 'to_alipay_dict'):
                params['use_rate'] = self.use_rate.to_alipay_dict()
            else:
                params['use_rate'] = self.use_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantEffectQueryResult()
        if 'accumulative_recharge_nums' in d:
            o.accumulative_recharge_nums = d['accumulative_recharge_nums']
        if 'accumulative_total_allowance' in d:
            o.accumulative_total_allowance = d['accumulative_total_allowance']
        if 'accumulative_total_days' in d:
            o.accumulative_total_days = d['accumulative_total_days']
        if 'accumulative_total_income' in d:
            o.accumulative_total_income = d['accumulative_total_income']
        if 'average_recharge_allowance_rate' in d:
            o.average_recharge_allowance_rate = d['average_recharge_allowance_rate']
        if 'date' in d:
            o.date = d['date']
        if 'effective_increased_income' in d:
            o.effective_increased_income = d['effective_increased_income']
        if 'increased_income' in d:
            o.increased_income = d['increased_income']
        if 'merchant_allowance' in d:
            o.merchant_allowance = d['merchant_allowance']
        if 'merchant_income' in d:
            o.merchant_income = d['merchant_income']
        if 'use_rate' in d:
            o.use_rate = d['use_rate']
        return o


