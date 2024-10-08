#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IncentiveMode(object):

    def __init__(self):
        self._finish_num = None
        self._per_incentive_point = None
        self._per_week_check_times = None
        self._total_num = None

    @property
    def finish_num(self):
        return self._finish_num

    @finish_num.setter
    def finish_num(self, value):
        self._finish_num = value
    @property
    def per_incentive_point(self):
        return self._per_incentive_point

    @per_incentive_point.setter
    def per_incentive_point(self, value):
        self._per_incentive_point = value
    @property
    def per_week_check_times(self):
        return self._per_week_check_times

    @per_week_check_times.setter
    def per_week_check_times(self, value):
        self._per_week_check_times = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.finish_num:
            if hasattr(self.finish_num, 'to_alipay_dict'):
                params['finish_num'] = self.finish_num.to_alipay_dict()
            else:
                params['finish_num'] = self.finish_num
        if self.per_incentive_point:
            if hasattr(self.per_incentive_point, 'to_alipay_dict'):
                params['per_incentive_point'] = self.per_incentive_point.to_alipay_dict()
            else:
                params['per_incentive_point'] = self.per_incentive_point
        if self.per_week_check_times:
            if hasattr(self.per_week_check_times, 'to_alipay_dict'):
                params['per_week_check_times'] = self.per_week_check_times.to_alipay_dict()
            else:
                params['per_week_check_times'] = self.per_week_check_times
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IncentiveMode()
        if 'finish_num' in d:
            o.finish_num = d['finish_num']
        if 'per_incentive_point' in d:
            o.per_incentive_point = d['per_incentive_point']
        if 'per_week_check_times' in d:
            o.per_week_check_times = d['per_week_check_times']
        if 'total_num' in d:
            o.total_num = d['total_num']
        return o


