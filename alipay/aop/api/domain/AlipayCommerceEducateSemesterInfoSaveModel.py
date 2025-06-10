#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSemesterInfoSaveModel(object):

    def __init__(self):
        self._end_date = None
        self._inst_id = None
        self._operator = None
        self._period_id = None
        self._semester_desc = None
        self._semester_id = None
        self._semester_name = None
        self._start_date = None
        self._status = None

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
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def period_id(self):
        return self._period_id

    @period_id.setter
    def period_id(self, value):
        self._period_id = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


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
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.period_id:
            if hasattr(self.period_id, 'to_alipay_dict'):
                params['period_id'] = self.period_id.to_alipay_dict()
            else:
                params['period_id'] = self.period_id
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSemesterInfoSaveModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'period_id' in d:
            o.period_id = d['period_id']
        if 'semester_desc' in d:
            o.semester_desc = d['semester_desc']
        if 'semester_id' in d:
            o.semester_id = d['semester_id']
        if 'semester_name' in d:
            o.semester_name = d['semester_name']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        return o


