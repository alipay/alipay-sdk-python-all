#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtraParams(object):

    def __init__(self):
        self._period = None
        self._period_summary_info = None

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_summary_info(self):
        return self._period_summary_info

    @period_summary_info.setter
    def period_summary_info(self, value):
        self._period_summary_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_summary_info:
            if hasattr(self.period_summary_info, 'to_alipay_dict'):
                params['period_summary_info'] = self.period_summary_info.to_alipay_dict()
            else:
                params['period_summary_info'] = self.period_summary_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtraParams()
        if 'period' in d:
            o.period = d['period']
        if 'period_summary_info' in d:
            o.period_summary_info = d['period_summary_info']
        return o


