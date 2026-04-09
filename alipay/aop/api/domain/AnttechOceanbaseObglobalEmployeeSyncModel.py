#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalEmployeeSyncModel(object):

    def __init__(self):
        self._employee_identity = None
        self._first_dept_id = None
        self._main_dept_id = None
        self._reporting_to = None
        self._second_dept_id = None
        self._status = None
        self._system_name = None
        self._third_dept_id = None
        self._work_no = None

    @property
    def employee_identity(self):
        return self._employee_identity

    @employee_identity.setter
    def employee_identity(self, value):
        self._employee_identity = value
    @property
    def first_dept_id(self):
        return self._first_dept_id

    @first_dept_id.setter
    def first_dept_id(self, value):
        self._first_dept_id = value
    @property
    def main_dept_id(self):
        return self._main_dept_id

    @main_dept_id.setter
    def main_dept_id(self, value):
        self._main_dept_id = value
    @property
    def reporting_to(self):
        return self._reporting_to

    @reporting_to.setter
    def reporting_to(self, value):
        self._reporting_to = value
    @property
    def second_dept_id(self):
        return self._second_dept_id

    @second_dept_id.setter
    def second_dept_id(self, value):
        self._second_dept_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value
    @property
    def third_dept_id(self):
        return self._third_dept_id

    @third_dept_id.setter
    def third_dept_id(self, value):
        self._third_dept_id = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_identity:
            if hasattr(self.employee_identity, 'to_alipay_dict'):
                params['employee_identity'] = self.employee_identity.to_alipay_dict()
            else:
                params['employee_identity'] = self.employee_identity
        if self.first_dept_id:
            if hasattr(self.first_dept_id, 'to_alipay_dict'):
                params['first_dept_id'] = self.first_dept_id.to_alipay_dict()
            else:
                params['first_dept_id'] = self.first_dept_id
        if self.main_dept_id:
            if hasattr(self.main_dept_id, 'to_alipay_dict'):
                params['main_dept_id'] = self.main_dept_id.to_alipay_dict()
            else:
                params['main_dept_id'] = self.main_dept_id
        if self.reporting_to:
            if hasattr(self.reporting_to, 'to_alipay_dict'):
                params['reporting_to'] = self.reporting_to.to_alipay_dict()
            else:
                params['reporting_to'] = self.reporting_to
        if self.second_dept_id:
            if hasattr(self.second_dept_id, 'to_alipay_dict'):
                params['second_dept_id'] = self.second_dept_id.to_alipay_dict()
            else:
                params['second_dept_id'] = self.second_dept_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
        if self.third_dept_id:
            if hasattr(self.third_dept_id, 'to_alipay_dict'):
                params['third_dept_id'] = self.third_dept_id.to_alipay_dict()
            else:
                params['third_dept_id'] = self.third_dept_id
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalEmployeeSyncModel()
        if 'employee_identity' in d:
            o.employee_identity = d['employee_identity']
        if 'first_dept_id' in d:
            o.first_dept_id = d['first_dept_id']
        if 'main_dept_id' in d:
            o.main_dept_id = d['main_dept_id']
        if 'reporting_to' in d:
            o.reporting_to = d['reporting_to']
        if 'second_dept_id' in d:
            o.second_dept_id = d['second_dept_id']
        if 'status' in d:
            o.status = d['status']
        if 'system_name' in d:
            o.system_name = d['system_name']
        if 'third_dept_id' in d:
            o.third_dept_id = d['third_dept_id']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


