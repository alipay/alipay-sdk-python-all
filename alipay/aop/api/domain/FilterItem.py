#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FilterItem(object):

    def __init__(self):
        self._department_id = None
        self._schedule_date = None
        self._sub_hospital_uniq_code = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def schedule_date(self):
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, value):
        self._schedule_date = value
    @property
    def sub_hospital_uniq_code(self):
        return self._sub_hospital_uniq_code

    @sub_hospital_uniq_code.setter
    def sub_hospital_uniq_code(self, value):
        self._sub_hospital_uniq_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.schedule_date:
            if hasattr(self.schedule_date, 'to_alipay_dict'):
                params['schedule_date'] = self.schedule_date.to_alipay_dict()
            else:
                params['schedule_date'] = self.schedule_date
        if self.sub_hospital_uniq_code:
            if hasattr(self.sub_hospital_uniq_code, 'to_alipay_dict'):
                params['sub_hospital_uniq_code'] = self.sub_hospital_uniq_code.to_alipay_dict()
            else:
                params['sub_hospital_uniq_code'] = self.sub_hospital_uniq_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FilterItem()
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'schedule_date' in d:
            o.schedule_date = d['schedule_date']
        if 'sub_hospital_uniq_code' in d:
            o.sub_hospital_uniq_code = d['sub_hospital_uniq_code']
        return o


