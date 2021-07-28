#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtraParams(object):

    def __init__(self):
        self._period = None
        self._period_summary_info = None
        self._quit_type = None
        self._withhold_index = None

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
    @property
    def quit_type(self):
        return self._quit_type

    @quit_type.setter
    def quit_type(self, value):
        self._quit_type = value
    @property
    def withhold_index(self):
        return self._withhold_index

    @withhold_index.setter
    def withhold_index(self, value):
        self._withhold_index = value


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
        if self.quit_type:
            if hasattr(self.quit_type, 'to_alipay_dict'):
                params['quit_type'] = self.quit_type.to_alipay_dict()
            else:
                params['quit_type'] = self.quit_type
        if self.withhold_index:
            if hasattr(self.withhold_index, 'to_alipay_dict'):
                params['withhold_index'] = self.withhold_index.to_alipay_dict()
            else:
                params['withhold_index'] = self.withhold_index
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
        if 'quit_type' in d:
            o.quit_type = d['quit_type']
        if 'withhold_index' in d:
            o.withhold_index = d['withhold_index']
        return o


