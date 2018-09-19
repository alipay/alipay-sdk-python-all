#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YLBProfitDetailInfo(object):

    def __init__(self):
        self._day_profit = None
        self._month_profit = None
        self._total_profit = None
        self._week_profit = None

    @property
    def day_profit(self):
        return self._day_profit

    @day_profit.setter
    def day_profit(self, value):
        self._day_profit = value
    @property
    def month_profit(self):
        return self._month_profit

    @month_profit.setter
    def month_profit(self, value):
        self._month_profit = value
    @property
    def total_profit(self):
        return self._total_profit

    @total_profit.setter
    def total_profit(self, value):
        self._total_profit = value
    @property
    def week_profit(self):
        return self._week_profit

    @week_profit.setter
    def week_profit(self, value):
        self._week_profit = value


    def to_alipay_dict(self):
        params = dict()
        if self.day_profit:
            if hasattr(self.day_profit, 'to_alipay_dict'):
                params['day_profit'] = self.day_profit.to_alipay_dict()
            else:
                params['day_profit'] = self.day_profit
        if self.month_profit:
            if hasattr(self.month_profit, 'to_alipay_dict'):
                params['month_profit'] = self.month_profit.to_alipay_dict()
            else:
                params['month_profit'] = self.month_profit
        if self.total_profit:
            if hasattr(self.total_profit, 'to_alipay_dict'):
                params['total_profit'] = self.total_profit.to_alipay_dict()
            else:
                params['total_profit'] = self.total_profit
        if self.week_profit:
            if hasattr(self.week_profit, 'to_alipay_dict'):
                params['week_profit'] = self.week_profit.to_alipay_dict()
            else:
                params['week_profit'] = self.week_profit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YLBProfitDetailInfo()
        if 'day_profit' in d:
            o.day_profit = d['day_profit']
        if 'month_profit' in d:
            o.month_profit = d['month_profit']
        if 'total_profit' in d:
            o.total_profit = d['total_profit']
        if 'week_profit' in d:
            o.week_profit = d['week_profit']
        return o


