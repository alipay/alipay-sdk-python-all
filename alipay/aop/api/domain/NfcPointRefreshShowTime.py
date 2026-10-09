#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcPointRefreshShowTime(object):

    def __init__(self):
        self._end_date = None
        self._end_date_time_stamp = None
        self._start_date = None
        self._start_date_time_stamp = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def end_date_time_stamp(self):
        return self._end_date_time_stamp

    @end_date_time_stamp.setter
    def end_date_time_stamp(self, value):
        self._end_date_time_stamp = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def start_date_time_stamp(self):
        return self._start_date_time_stamp

    @start_date_time_stamp.setter
    def start_date_time_stamp(self, value):
        self._start_date_time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.end_date_time_stamp:
            if hasattr(self.end_date_time_stamp, 'to_alipay_dict'):
                params['end_date_time_stamp'] = self.end_date_time_stamp.to_alipay_dict()
            else:
                params['end_date_time_stamp'] = self.end_date_time_stamp
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.start_date_time_stamp:
            if hasattr(self.start_date_time_stamp, 'to_alipay_dict'):
                params['start_date_time_stamp'] = self.start_date_time_stamp.to_alipay_dict()
            else:
                params['start_date_time_stamp'] = self.start_date_time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshShowTime()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_date_time_stamp' in d:
            o.end_date_time_stamp = d['end_date_time_stamp']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'start_date_time_stamp' in d:
            o.start_date_time_stamp = d['start_date_time_stamp']
        return o


