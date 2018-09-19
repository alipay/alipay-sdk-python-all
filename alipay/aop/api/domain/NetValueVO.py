#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NetValueVO(object):

    def __init__(self):
        self._net_value = None
        self._net_value_date = None
        self._profit_seven_days = None
        self._profit_ten_thousand = None

    @property
    def net_value(self):
        return self._net_value

    @net_value.setter
    def net_value(self, value):
        self._net_value = value
    @property
    def net_value_date(self):
        return self._net_value_date

    @net_value_date.setter
    def net_value_date(self, value):
        self._net_value_date = value
    @property
    def profit_seven_days(self):
        return self._profit_seven_days

    @profit_seven_days.setter
    def profit_seven_days(self, value):
        self._profit_seven_days = value
    @property
    def profit_ten_thousand(self):
        return self._profit_ten_thousand

    @profit_ten_thousand.setter
    def profit_ten_thousand(self, value):
        self._profit_ten_thousand = value


    def to_alipay_dict(self):
        params = dict()
        if self.net_value:
            if hasattr(self.net_value, 'to_alipay_dict'):
                params['net_value'] = self.net_value.to_alipay_dict()
            else:
                params['net_value'] = self.net_value
        if self.net_value_date:
            if hasattr(self.net_value_date, 'to_alipay_dict'):
                params['net_value_date'] = self.net_value_date.to_alipay_dict()
            else:
                params['net_value_date'] = self.net_value_date
        if self.profit_seven_days:
            if hasattr(self.profit_seven_days, 'to_alipay_dict'):
                params['profit_seven_days'] = self.profit_seven_days.to_alipay_dict()
            else:
                params['profit_seven_days'] = self.profit_seven_days
        if self.profit_ten_thousand:
            if hasattr(self.profit_ten_thousand, 'to_alipay_dict'):
                params['profit_ten_thousand'] = self.profit_ten_thousand.to_alipay_dict()
            else:
                params['profit_ten_thousand'] = self.profit_ten_thousand
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NetValueVO()
        if 'net_value' in d:
            o.net_value = d['net_value']
        if 'net_value_date' in d:
            o.net_value_date = d['net_value_date']
        if 'profit_seven_days' in d:
            o.profit_seven_days = d['profit_seven_days']
        if 'profit_ten_thousand' in d:
            o.profit_ten_thousand = d['profit_ten_thousand']
        return o


