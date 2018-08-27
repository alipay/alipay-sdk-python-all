#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CalendarScheduleInfo import CalendarScheduleInfo


class AlipayDaoweiSpScheduleModifyModel(object):

    def __init__(self):
        self._calendar_schedule = None
        self._out_sp_id = None

    @property
    def calendar_schedule(self):
        return self._calendar_schedule

    @calendar_schedule.setter
    def calendar_schedule(self, value):
        if isinstance(value, CalendarScheduleInfo):
            self._calendar_schedule = value
        else:
            self._calendar_schedule = CalendarScheduleInfo.from_alipay_dict(value)
    @property
    def out_sp_id(self):
        return self._out_sp_id

    @out_sp_id.setter
    def out_sp_id(self, value):
        self._out_sp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.calendar_schedule:
            if hasattr(self.calendar_schedule, 'to_alipay_dict'):
                params['calendar_schedule'] = self.calendar_schedule.to_alipay_dict()
            else:
                params['calendar_schedule'] = self.calendar_schedule
        if self.out_sp_id:
            if hasattr(self.out_sp_id, 'to_alipay_dict'):
                params['out_sp_id'] = self.out_sp_id.to_alipay_dict()
            else:
                params['out_sp_id'] = self.out_sp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDaoweiSpScheduleModifyModel()
        if 'calendar_schedule' in d:
            o.calendar_schedule = d['calendar_schedule']
        if 'out_sp_id' in d:
            o.out_sp_id = d['out_sp_id']
        return o


