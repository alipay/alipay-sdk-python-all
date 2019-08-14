#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayDayRangePricingVO import CreditPayDayRangePricingVO


class CreditPayIntPricingVO(object):

    def __init__(self):
        self._actual_day_int_rate = None
        self._actual_int = None
        self._actual_int_rate = None
        self._day_range_pricing_list = None
        self._origin_day_int_rate = None
        self._origin_int = None
        self._origin_int_rate = None

    @property
    def actual_day_int_rate(self):
        return self._actual_day_int_rate

    @actual_day_int_rate.setter
    def actual_day_int_rate(self, value):
        self._actual_day_int_rate = value
    @property
    def actual_int(self):
        return self._actual_int

    @actual_int.setter
    def actual_int(self, value):
        self._actual_int = value
    @property
    def actual_int_rate(self):
        return self._actual_int_rate

    @actual_int_rate.setter
    def actual_int_rate(self, value):
        self._actual_int_rate = value
    @property
    def day_range_pricing_list(self):
        return self._day_range_pricing_list

    @day_range_pricing_list.setter
    def day_range_pricing_list(self, value):
        if isinstance(value, list):
            self._day_range_pricing_list = list()
            for i in value:
                if isinstance(i, CreditPayDayRangePricingVO):
                    self._day_range_pricing_list.append(i)
                else:
                    self._day_range_pricing_list.append(CreditPayDayRangePricingVO.from_alipay_dict(i))
    @property
    def origin_day_int_rate(self):
        return self._origin_day_int_rate

    @origin_day_int_rate.setter
    def origin_day_int_rate(self, value):
        self._origin_day_int_rate = value
    @property
    def origin_int(self):
        return self._origin_int

    @origin_int.setter
    def origin_int(self, value):
        self._origin_int = value
    @property
    def origin_int_rate(self):
        return self._origin_int_rate

    @origin_int_rate.setter
    def origin_int_rate(self, value):
        self._origin_int_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_day_int_rate:
            if hasattr(self.actual_day_int_rate, 'to_alipay_dict'):
                params['actual_day_int_rate'] = self.actual_day_int_rate.to_alipay_dict()
            else:
                params['actual_day_int_rate'] = self.actual_day_int_rate
        if self.actual_int:
            if hasattr(self.actual_int, 'to_alipay_dict'):
                params['actual_int'] = self.actual_int.to_alipay_dict()
            else:
                params['actual_int'] = self.actual_int
        if self.actual_int_rate:
            if hasattr(self.actual_int_rate, 'to_alipay_dict'):
                params['actual_int_rate'] = self.actual_int_rate.to_alipay_dict()
            else:
                params['actual_int_rate'] = self.actual_int_rate
        if self.day_range_pricing_list:
            if isinstance(self.day_range_pricing_list, list):
                for i in range(0, len(self.day_range_pricing_list)):
                    element = self.day_range_pricing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.day_range_pricing_list[i] = element.to_alipay_dict()
            if hasattr(self.day_range_pricing_list, 'to_alipay_dict'):
                params['day_range_pricing_list'] = self.day_range_pricing_list.to_alipay_dict()
            else:
                params['day_range_pricing_list'] = self.day_range_pricing_list
        if self.origin_day_int_rate:
            if hasattr(self.origin_day_int_rate, 'to_alipay_dict'):
                params['origin_day_int_rate'] = self.origin_day_int_rate.to_alipay_dict()
            else:
                params['origin_day_int_rate'] = self.origin_day_int_rate
        if self.origin_int:
            if hasattr(self.origin_int, 'to_alipay_dict'):
                params['origin_int'] = self.origin_int.to_alipay_dict()
            else:
                params['origin_int'] = self.origin_int
        if self.origin_int_rate:
            if hasattr(self.origin_int_rate, 'to_alipay_dict'):
                params['origin_int_rate'] = self.origin_int_rate.to_alipay_dict()
            else:
                params['origin_int_rate'] = self.origin_int_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayIntPricingVO()
        if 'actual_day_int_rate' in d:
            o.actual_day_int_rate = d['actual_day_int_rate']
        if 'actual_int' in d:
            o.actual_int = d['actual_int']
        if 'actual_int_rate' in d:
            o.actual_int_rate = d['actual_int_rate']
        if 'day_range_pricing_list' in d:
            o.day_range_pricing_list = d['day_range_pricing_list']
        if 'origin_day_int_rate' in d:
            o.origin_day_int_rate = d['origin_day_int_rate']
        if 'origin_int' in d:
            o.origin_int = d['origin_int']
        if 'origin_int_rate' in d:
            o.origin_int_rate = d['origin_int_rate']
        return o


