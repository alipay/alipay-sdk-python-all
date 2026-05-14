#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CycleAvgDiscountAmountConfig(object):

    def __init__(self):
        self._avg_discount_amount = None
        self._day_of_week = None
        self._order = None

    @property
    def avg_discount_amount(self):
        return self._avg_discount_amount

    @avg_discount_amount.setter
    def avg_discount_amount(self, value):
        self._avg_discount_amount = value
    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, value):
        if isinstance(value, list):
            self._day_of_week = list()
            for i in value:
                self._day_of_week.append(i)
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_discount_amount:
            if hasattr(self.avg_discount_amount, 'to_alipay_dict'):
                params['avg_discount_amount'] = self.avg_discount_amount.to_alipay_dict()
            else:
                params['avg_discount_amount'] = self.avg_discount_amount
        if self.day_of_week:
            if isinstance(self.day_of_week, list):
                for i in range(0, len(self.day_of_week)):
                    element = self.day_of_week[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.day_of_week[i] = element.to_alipay_dict()
            if hasattr(self.day_of_week, 'to_alipay_dict'):
                params['day_of_week'] = self.day_of_week.to_alipay_dict()
            else:
                params['day_of_week'] = self.day_of_week
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CycleAvgDiscountAmountConfig()
        if 'avg_discount_amount' in d:
            o.avg_discount_amount = d['avg_discount_amount']
        if 'day_of_week' in d:
            o.day_of_week = d['day_of_week']
        if 'order' in d:
            o.order = d['order']
        return o


