#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DelegationTaskParams(object):

    def __init__(self):
        self._period_count = None
        self._period_times = None
        self._period_unit = None
        self._total_periods = None

    @property
    def period_count(self):
        return self._period_count

    @period_count.setter
    def period_count(self, value):
        self._period_count = value
    @property
    def period_times(self):
        return self._period_times

    @period_times.setter
    def period_times(self, value):
        self._period_times = value
    @property
    def period_unit(self):
        return self._period_unit

    @period_unit.setter
    def period_unit(self, value):
        self._period_unit = value
    @property
    def total_periods(self):
        return self._total_periods

    @total_periods.setter
    def total_periods(self, value):
        self._total_periods = value


    def to_alipay_dict(self):
        params = dict()
        if self.period_count:
            if hasattr(self.period_count, 'to_alipay_dict'):
                params['period_count'] = self.period_count.to_alipay_dict()
            else:
                params['period_count'] = self.period_count
        if self.period_times:
            if hasattr(self.period_times, 'to_alipay_dict'):
                params['period_times'] = self.period_times.to_alipay_dict()
            else:
                params['period_times'] = self.period_times
        if self.period_unit:
            if hasattr(self.period_unit, 'to_alipay_dict'):
                params['period_unit'] = self.period_unit.to_alipay_dict()
            else:
                params['period_unit'] = self.period_unit
        if self.total_periods:
            if hasattr(self.total_periods, 'to_alipay_dict'):
                params['total_periods'] = self.total_periods.to_alipay_dict()
            else:
                params['total_periods'] = self.total_periods
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DelegationTaskParams()
        if 'period_count' in d:
            o.period_count = d['period_count']
        if 'period_times' in d:
            o.period_times = d['period_times']
        if 'period_unit' in d:
            o.period_unit = d['period_unit']
        if 'total_periods' in d:
            o.total_periods = d['total_periods']
        return o


