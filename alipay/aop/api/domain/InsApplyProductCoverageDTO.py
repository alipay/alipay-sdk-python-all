#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsApplyProductCoverageDTO(object):

    def __init__(self):
        self._effective_end_time = None
        self._effective_start_time = None
        self._period = None

    @property
    def effective_end_time(self):
        return self._effective_end_time

    @effective_end_time.setter
    def effective_end_time(self, value):
        self._effective_end_time = value
    @property
    def effective_start_time(self):
        return self._effective_start_time

    @effective_start_time.setter
    def effective_start_time(self, value):
        self._effective_start_time = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_end_time:
            if hasattr(self.effective_end_time, 'to_alipay_dict'):
                params['effective_end_time'] = self.effective_end_time.to_alipay_dict()
            else:
                params['effective_end_time'] = self.effective_end_time
        if self.effective_start_time:
            if hasattr(self.effective_start_time, 'to_alipay_dict'):
                params['effective_start_time'] = self.effective_start_time.to_alipay_dict()
            else:
                params['effective_start_time'] = self.effective_start_time
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsApplyProductCoverageDTO()
        if 'effective_end_time' in d:
            o.effective_end_time = d['effective_end_time']
        if 'effective_start_time' in d:
            o.effective_start_time = d['effective_start_time']
        if 'period' in d:
            o.period = d['period']
        return o


