#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPayInfo import RentPayInfo


class FlexibleRentInfo(object):

    def __init__(self):
        self._biweekly_rent = None
        self._monthly_rent = None
        self._pay_plan = None
        self._period_count = None
        self._quarterly_rent = None
        self._rent_type = None
        self._ten_days_rent = None
        self._weekly_rent = None

    @property
    def biweekly_rent(self):
        return self._biweekly_rent

    @biweekly_rent.setter
    def biweekly_rent(self, value):
        self._biweekly_rent = value
    @property
    def monthly_rent(self):
        return self._monthly_rent

    @monthly_rent.setter
    def monthly_rent(self, value):
        self._monthly_rent = value
    @property
    def pay_plan(self):
        return self._pay_plan

    @pay_plan.setter
    def pay_plan(self, value):
        if isinstance(value, list):
            self._pay_plan = list()
            for i in value:
                if isinstance(i, RentPayInfo):
                    self._pay_plan.append(i)
                else:
                    self._pay_plan.append(RentPayInfo.from_alipay_dict(i))
    @property
    def period_count(self):
        return self._period_count

    @period_count.setter
    def period_count(self, value):
        self._period_count = value
    @property
    def quarterly_rent(self):
        return self._quarterly_rent

    @quarterly_rent.setter
    def quarterly_rent(self, value):
        self._quarterly_rent = value
    @property
    def rent_type(self):
        return self._rent_type

    @rent_type.setter
    def rent_type(self, value):
        self._rent_type = value
    @property
    def ten_days_rent(self):
        return self._ten_days_rent

    @ten_days_rent.setter
    def ten_days_rent(self, value):
        self._ten_days_rent = value
    @property
    def weekly_rent(self):
        return self._weekly_rent

    @weekly_rent.setter
    def weekly_rent(self, value):
        self._weekly_rent = value


    def to_alipay_dict(self):
        params = dict()
        if self.biweekly_rent:
            if hasattr(self.biweekly_rent, 'to_alipay_dict'):
                params['biweekly_rent'] = self.biweekly_rent.to_alipay_dict()
            else:
                params['biweekly_rent'] = self.biweekly_rent
        if self.monthly_rent:
            if hasattr(self.monthly_rent, 'to_alipay_dict'):
                params['monthly_rent'] = self.monthly_rent.to_alipay_dict()
            else:
                params['monthly_rent'] = self.monthly_rent
        if self.pay_plan:
            if isinstance(self.pay_plan, list):
                for i in range(0, len(self.pay_plan)):
                    element = self.pay_plan[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_plan[i] = element.to_alipay_dict()
            if hasattr(self.pay_plan, 'to_alipay_dict'):
                params['pay_plan'] = self.pay_plan.to_alipay_dict()
            else:
                params['pay_plan'] = self.pay_plan
        if self.period_count:
            if hasattr(self.period_count, 'to_alipay_dict'):
                params['period_count'] = self.period_count.to_alipay_dict()
            else:
                params['period_count'] = self.period_count
        if self.quarterly_rent:
            if hasattr(self.quarterly_rent, 'to_alipay_dict'):
                params['quarterly_rent'] = self.quarterly_rent.to_alipay_dict()
            else:
                params['quarterly_rent'] = self.quarterly_rent
        if self.rent_type:
            if hasattr(self.rent_type, 'to_alipay_dict'):
                params['rent_type'] = self.rent_type.to_alipay_dict()
            else:
                params['rent_type'] = self.rent_type
        if self.ten_days_rent:
            if hasattr(self.ten_days_rent, 'to_alipay_dict'):
                params['ten_days_rent'] = self.ten_days_rent.to_alipay_dict()
            else:
                params['ten_days_rent'] = self.ten_days_rent
        if self.weekly_rent:
            if hasattr(self.weekly_rent, 'to_alipay_dict'):
                params['weekly_rent'] = self.weekly_rent.to_alipay_dict()
            else:
                params['weekly_rent'] = self.weekly_rent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FlexibleRentInfo()
        if 'biweekly_rent' in d:
            o.biweekly_rent = d['biweekly_rent']
        if 'monthly_rent' in d:
            o.monthly_rent = d['monthly_rent']
        if 'pay_plan' in d:
            o.pay_plan = d['pay_plan']
        if 'period_count' in d:
            o.period_count = d['period_count']
        if 'quarterly_rent' in d:
            o.quarterly_rent = d['quarterly_rent']
        if 'rent_type' in d:
            o.rent_type = d['rent_type']
        if 'ten_days_rent' in d:
            o.ten_days_rent = d['ten_days_rent']
        if 'weekly_rent' in d:
            o.weekly_rent = d['weekly_rent']
        return o


