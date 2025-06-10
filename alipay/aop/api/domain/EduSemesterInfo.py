#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduPeriodInfo import EduPeriodInfo


class EduSemesterInfo(object):

    def __init__(self):
        self._end_date = None
        self._inst_id = None
        self._max_week = None
        self._modified_time = None
        self._operator = None
        self._period = None
        self._semester_desc = None
        self._semester_id = None
        self._semester_name = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def max_week(self):
        return self._max_week

    @max_week.setter
    def max_week(self, value):
        self._max_week = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        if isinstance(value, EduPeriodInfo):
            self._period = value
        else:
            self._period = EduPeriodInfo.from_alipay_dict(value)
    @property
    def semester_desc(self):
        return self._semester_desc

    @semester_desc.setter
    def semester_desc(self, value):
        self._semester_desc = value
    @property
    def semester_id(self):
        return self._semester_id

    @semester_id.setter
    def semester_id(self, value):
        self._semester_id = value
    @property
    def semester_name(self):
        return self._semester_name

    @semester_name.setter
    def semester_name(self, value):
        self._semester_name = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.max_week:
            if hasattr(self.max_week, 'to_alipay_dict'):
                params['max_week'] = self.max_week.to_alipay_dict()
            else:
                params['max_week'] = self.max_week
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.semester_desc:
            if hasattr(self.semester_desc, 'to_alipay_dict'):
                params['semester_desc'] = self.semester_desc.to_alipay_dict()
            else:
                params['semester_desc'] = self.semester_desc
        if self.semester_id:
            if hasattr(self.semester_id, 'to_alipay_dict'):
                params['semester_id'] = self.semester_id.to_alipay_dict()
            else:
                params['semester_id'] = self.semester_id
        if self.semester_name:
            if hasattr(self.semester_name, 'to_alipay_dict'):
                params['semester_name'] = self.semester_name.to_alipay_dict()
            else:
                params['semester_name'] = self.semester_name
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduSemesterInfo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'max_week' in d:
            o.max_week = d['max_week']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'period' in d:
            o.period = d['period']
        if 'semester_desc' in d:
            o.semester_desc = d['semester_desc']
        if 'semester_id' in d:
            o.semester_id = d['semester_id']
        if 'semester_name' in d:
            o.semester_name = d['semester_name']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


