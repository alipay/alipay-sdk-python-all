#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DoctorWorkDepartmentInfo import DoctorWorkDepartmentInfo


class DoctorWorkInfo(object):

    def __init__(self):
        self._department_info = None
        self._hospital_id = None
        self._hospital_name = None

    @property
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, value):
        if isinstance(value, list):
            self._department_info = list()
            for i in value:
                if isinstance(i, DoctorWorkDepartmentInfo):
                    self._department_info.append(i)
                else:
                    self._department_info.append(DoctorWorkDepartmentInfo.from_alipay_dict(i))
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_info:
            if isinstance(self.department_info, list):
                for i in range(0, len(self.department_info)):
                    element = self.department_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_info[i] = element.to_alipay_dict()
            if hasattr(self.department_info, 'to_alipay_dict'):
                params['department_info'] = self.department_info.to_alipay_dict()
            else:
                params['department_info'] = self.department_info
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorWorkInfo()
        if 'department_info' in d:
            o.department_info = d['department_info']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        return o


