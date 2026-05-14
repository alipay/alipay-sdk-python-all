#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalReportSmsSendModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._department = None
        self._hospital_name = None
        self._name = None
        self._phone_number = None
        self._report_count = None
        self._report_ids = None
        self._report_issue_time = None
        self._report_name = None
        self._report_type = None
        self._uscc = None
        self._visit_time = None

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
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def report_count(self):
        return self._report_count

    @report_count.setter
    def report_count(self, value):
        self._report_count = value
    @property
    def report_ids(self):
        return self._report_ids

    @report_ids.setter
    def report_ids(self, value):
        self._report_ids = value
    @property
    def report_issue_time(self):
        return self._report_issue_time

    @report_issue_time.setter
    def report_issue_time(self, value):
        self._report_issue_time = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def visit_time(self):
        return self._visit_time

    @visit_time.setter
    def visit_time(self, value):
        self._visit_time = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.report_count:
            if hasattr(self.report_count, 'to_alipay_dict'):
                params['report_count'] = self.report_count.to_alipay_dict()
            else:
                params['report_count'] = self.report_count
        if self.report_ids:
            if hasattr(self.report_ids, 'to_alipay_dict'):
                params['report_ids'] = self.report_ids.to_alipay_dict()
            else:
                params['report_ids'] = self.report_ids
        if self.report_issue_time:
            if hasattr(self.report_issue_time, 'to_alipay_dict'):
                params['report_issue_time'] = self.report_issue_time.to_alipay_dict()
            else:
                params['report_issue_time'] = self.report_issue_time
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        if self.visit_time:
            if hasattr(self.visit_time, 'to_alipay_dict'):
                params['visit_time'] = self.visit_time.to_alipay_dict()
            else:
                params['visit_time'] = self.visit_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalReportSmsSendModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'department' in d:
            o.department = d['department']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'name' in d:
            o.name = d['name']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'report_count' in d:
            o.report_count = d['report_count']
        if 'report_ids' in d:
            o.report_ids = d['report_ids']
        if 'report_issue_time' in d:
            o.report_issue_time = d['report_issue_time']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'uscc' in d:
            o.uscc = d['uscc']
        if 'visit_time' in d:
            o.visit_time = d['visit_time']
        return o


