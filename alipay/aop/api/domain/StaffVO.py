#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DepartmentJobVO import DepartmentJobVO


class StaffVO(object):

    def __init__(self):
        self._department_jobs = None
        self._name = None
        self._phone = None
        self._staff_id = None
        self._staff_no = None

    @property
    def department_jobs(self):
        return self._department_jobs

    @department_jobs.setter
    def department_jobs(self, value):
        if isinstance(value, list):
            self._department_jobs = list()
            for i in value:
                if isinstance(i, DepartmentJobVO):
                    self._department_jobs.append(i)
                else:
                    self._department_jobs.append(DepartmentJobVO.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value
    @property
    def staff_no(self):
        return self._staff_no

    @staff_no.setter
    def staff_no(self, value):
        self._staff_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_jobs:
            if isinstance(self.department_jobs, list):
                for i in range(0, len(self.department_jobs)):
                    element = self.department_jobs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_jobs[i] = element.to_alipay_dict()
            if hasattr(self.department_jobs, 'to_alipay_dict'):
                params['department_jobs'] = self.department_jobs.to_alipay_dict()
            else:
                params['department_jobs'] = self.department_jobs
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.staff_id:
            if hasattr(self.staff_id, 'to_alipay_dict'):
                params['staff_id'] = self.staff_id.to_alipay_dict()
            else:
                params['staff_id'] = self.staff_id
        if self.staff_no:
            if hasattr(self.staff_no, 'to_alipay_dict'):
                params['staff_no'] = self.staff_no.to_alipay_dict()
            else:
                params['staff_no'] = self.staff_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StaffVO()
        if 'department_jobs' in d:
            o.department_jobs = d['department_jobs']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'staff_id' in d:
            o.staff_id = d['staff_id']
        if 'staff_no' in d:
            o.staff_no = d['staff_no']
        return o


