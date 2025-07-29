#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedagentAgentQueryModel(object):

    def __init__(self):
        self._department = None
        self._doctor = None
        self._hospital_name = None

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        self._doctor = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.doctor:
            if hasattr(self.doctor, 'to_alipay_dict'):
                params['doctor'] = self.doctor.to_alipay_dict()
            else:
                params['doctor'] = self.doctor
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
        o = AlipayCommerceMedicalMedagentAgentQueryModel()
        if 'department' in d:
            o.department = d['department']
        if 'doctor' in d:
            o.doctor = d['doctor']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        return o


