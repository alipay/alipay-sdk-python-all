#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupMsgScheduleConfigVO(object):

    def __init__(self):
        self._cron_time = None
        self._cron_unit = None
        self._cron_value = None
        self._end_time = None
        self._start_time = None

    @property
    def cron_time(self):
        return self._cron_time

    @cron_time.setter
    def cron_time(self, value):
        self._cron_time = value
    @property
    def cron_unit(self):
        return self._cron_unit

    @cron_unit.setter
    def cron_unit(self, value):
        self._cron_unit = value
    @property
    def cron_value(self):
        return self._cron_value

    @cron_value.setter
    def cron_value(self, value):
        self._cron_value = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.cron_time:
            if hasattr(self.cron_time, 'to_alipay_dict'):
                params['cron_time'] = self.cron_time.to_alipay_dict()
            else:
                params['cron_time'] = self.cron_time
        if self.cron_unit:
            if hasattr(self.cron_unit, 'to_alipay_dict'):
                params['cron_unit'] = self.cron_unit.to_alipay_dict()
            else:
                params['cron_unit'] = self.cron_unit
        if self.cron_value:
            if hasattr(self.cron_value, 'to_alipay_dict'):
                params['cron_value'] = self.cron_value.to_alipay_dict()
            else:
                params['cron_value'] = self.cron_value
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgScheduleConfigVO()
        if 'cron_time' in d:
            o.cron_time = d['cron_time']
        if 'cron_unit' in d:
            o.cron_unit = d['cron_unit']
        if 'cron_value' in d:
            o.cron_value = d['cron_value']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


