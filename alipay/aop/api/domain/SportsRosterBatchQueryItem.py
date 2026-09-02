#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SportsRosterBatchQueryItem(object):

    def __init__(self):
        self._department = None
        self._employee_no = None
        self._name = None
        self._status = None
        self._user_code = None

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_code(self):
        return self._user_code

    @user_code.setter
    def user_code(self, value):
        self._user_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_code:
            if hasattr(self.user_code, 'to_alipay_dict'):
                params['user_code'] = self.user_code.to_alipay_dict()
            else:
                params['user_code'] = self.user_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SportsRosterBatchQueryItem()
        if 'department' in d:
            o.department = d['department']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'user_code' in d:
            o.user_code = d['user_code']
        return o


