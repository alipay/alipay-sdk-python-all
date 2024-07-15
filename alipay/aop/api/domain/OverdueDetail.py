#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OverdueDetail(object):

    def __init__(self):
        self._overdue_day = None
        self._overdue_desc = None
        self._overdue_fee = None
        self._overdue_period_num = None
        self._overdue_time = None

    @property
    def overdue_day(self):
        return self._overdue_day

    @overdue_day.setter
    def overdue_day(self, value):
        self._overdue_day = value
    @property
    def overdue_desc(self):
        return self._overdue_desc

    @overdue_desc.setter
    def overdue_desc(self, value):
        self._overdue_desc = value
    @property
    def overdue_fee(self):
        return self._overdue_fee

    @overdue_fee.setter
    def overdue_fee(self, value):
        self._overdue_fee = value
    @property
    def overdue_period_num(self):
        return self._overdue_period_num

    @overdue_period_num.setter
    def overdue_period_num(self, value):
        self._overdue_period_num = value
    @property
    def overdue_time(self):
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, value):
        self._overdue_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.overdue_day:
            if hasattr(self.overdue_day, 'to_alipay_dict'):
                params['overdue_day'] = self.overdue_day.to_alipay_dict()
            else:
                params['overdue_day'] = self.overdue_day
        if self.overdue_desc:
            if hasattr(self.overdue_desc, 'to_alipay_dict'):
                params['overdue_desc'] = self.overdue_desc.to_alipay_dict()
            else:
                params['overdue_desc'] = self.overdue_desc
        if self.overdue_fee:
            if hasattr(self.overdue_fee, 'to_alipay_dict'):
                params['overdue_fee'] = self.overdue_fee.to_alipay_dict()
            else:
                params['overdue_fee'] = self.overdue_fee
        if self.overdue_period_num:
            if hasattr(self.overdue_period_num, 'to_alipay_dict'):
                params['overdue_period_num'] = self.overdue_period_num.to_alipay_dict()
            else:
                params['overdue_period_num'] = self.overdue_period_num
        if self.overdue_time:
            if hasattr(self.overdue_time, 'to_alipay_dict'):
                params['overdue_time'] = self.overdue_time.to_alipay_dict()
            else:
                params['overdue_time'] = self.overdue_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OverdueDetail()
        if 'overdue_day' in d:
            o.overdue_day = d['overdue_day']
        if 'overdue_desc' in d:
            o.overdue_desc = d['overdue_desc']
        if 'overdue_fee' in d:
            o.overdue_fee = d['overdue_fee']
        if 'overdue_period_num' in d:
            o.overdue_period_num = d['overdue_period_num']
        if 'overdue_time' in d:
            o.overdue_time = d['overdue_time']
        return o


