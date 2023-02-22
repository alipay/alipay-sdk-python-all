#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeRestrictInfo import TimeRestrictInfo


class VoucherAbsolutePeriodInfo(object):

    def __init__(self):
        self._time_restrict_info = None
        self._valid_begin_time = None
        self._valid_end_time = None

    @property
    def time_restrict_info(self):
        return self._time_restrict_info

    @time_restrict_info.setter
    def time_restrict_info(self, value):
        if isinstance(value, TimeRestrictInfo):
            self._time_restrict_info = value
        else:
            self._time_restrict_info = TimeRestrictInfo.from_alipay_dict(value)
    @property
    def valid_begin_time(self):
        return self._valid_begin_time

    @valid_begin_time.setter
    def valid_begin_time(self, value):
        self._valid_begin_time = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.time_restrict_info:
            if hasattr(self.time_restrict_info, 'to_alipay_dict'):
                params['time_restrict_info'] = self.time_restrict_info.to_alipay_dict()
            else:
                params['time_restrict_info'] = self.time_restrict_info
        if self.valid_begin_time:
            if hasattr(self.valid_begin_time, 'to_alipay_dict'):
                params['valid_begin_time'] = self.valid_begin_time.to_alipay_dict()
            else:
                params['valid_begin_time'] = self.valid_begin_time
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAbsolutePeriodInfo()
        if 'time_restrict_info' in d:
            o.time_restrict_info = d['time_restrict_info']
        if 'valid_begin_time' in d:
            o.valid_begin_time = d['valid_begin_time']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        return o


