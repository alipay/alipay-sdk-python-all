#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorWorkDepartmentInfo(object):

    def __init__(self):
        self._department_id = None
        self._department_name = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorWorkDepartmentInfo()
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        return o


