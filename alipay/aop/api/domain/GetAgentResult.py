#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Doctor import Doctor


class GetAgentResult(object):

    def __init__(self):
        self._doctor = None
        self._operation_status = None
        self._operation_status_description = None

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        if isinstance(value, Doctor):
            self._doctor = value
        else:
            self._doctor = Doctor.from_alipay_dict(value)
    @property
    def operation_status(self):
        return self._operation_status

    @operation_status.setter
    def operation_status(self, value):
        self._operation_status = value
    @property
    def operation_status_description(self):
        return self._operation_status_description

    @operation_status_description.setter
    def operation_status_description(self, value):
        self._operation_status_description = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor:
            if hasattr(self.doctor, 'to_alipay_dict'):
                params['doctor'] = self.doctor.to_alipay_dict()
            else:
                params['doctor'] = self.doctor
        if self.operation_status:
            if hasattr(self.operation_status, 'to_alipay_dict'):
                params['operation_status'] = self.operation_status.to_alipay_dict()
            else:
                params['operation_status'] = self.operation_status
        if self.operation_status_description:
            if hasattr(self.operation_status_description, 'to_alipay_dict'):
                params['operation_status_description'] = self.operation_status_description.to_alipay_dict()
            else:
                params['operation_status_description'] = self.operation_status_description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetAgentResult()
        if 'doctor' in d:
            o.doctor = d['doctor']
        if 'operation_status' in d:
            o.operation_status = d['operation_status']
        if 'operation_status_description' in d:
            o.operation_status_description = d['operation_status_description']
        return o


