#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsureEmployee(object):

    def __init__(self):
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._employee_card_no = None
        self._job = None
        self._job_level = None
        self._out_employee_id = None
        self._phone = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def employee_card_no(self):
        return self._employee_card_no

    @employee_card_no.setter
    def employee_card_no(self, value):
        self._employee_card_no = value
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value
    @property
    def job_level(self):
        return self._job_level

    @job_level.setter
    def job_level(self, value):
        self._job_level = value
    @property
    def out_employee_id(self):
        return self._out_employee_id

    @out_employee_id.setter
    def out_employee_id(self, value):
        self._out_employee_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.employee_card_no:
            if hasattr(self.employee_card_no, 'to_alipay_dict'):
                params['employee_card_no'] = self.employee_card_no.to_alipay_dict()
            else:
                params['employee_card_no'] = self.employee_card_no
        if self.job:
            if hasattr(self.job, 'to_alipay_dict'):
                params['job'] = self.job.to_alipay_dict()
            else:
                params['job'] = self.job
        if self.job_level:
            if hasattr(self.job_level, 'to_alipay_dict'):
                params['job_level'] = self.job_level.to_alipay_dict()
            else:
                params['job_level'] = self.job_level
        if self.out_employee_id:
            if hasattr(self.out_employee_id, 'to_alipay_dict'):
                params['out_employee_id'] = self.out_employee_id.to_alipay_dict()
            else:
                params['out_employee_id'] = self.out_employee_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsureEmployee()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'employee_card_no' in d:
            o.employee_card_no = d['employee_card_no']
        if 'job' in d:
            o.job = d['job']
        if 'job_level' in d:
            o.job_level = d['job_level']
        if 'out_employee_id' in d:
            o.out_employee_id = d['out_employee_id']
        if 'phone' in d:
            o.phone = d['phone']
        return o


