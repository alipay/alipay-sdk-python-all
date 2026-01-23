#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuranceVisitInfo(object):

    def __init__(self):
        self._hospital_name = None
        self._medical_type = None
        self._visit_date = None

    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def medical_type(self):
        return self._medical_type

    @medical_type.setter
    def medical_type(self, value):
        self._medical_type = value
    @property
    def visit_date(self):
        return self._visit_date

    @visit_date.setter
    def visit_date(self, value):
        self._visit_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.medical_type:
            if hasattr(self.medical_type, 'to_alipay_dict'):
                params['medical_type'] = self.medical_type.to_alipay_dict()
            else:
                params['medical_type'] = self.medical_type
        if self.visit_date:
            if hasattr(self.visit_date, 'to_alipay_dict'):
                params['visit_date'] = self.visit_date.to_alipay_dict()
            else:
                params['visit_date'] = self.visit_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuranceVisitInfo()
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'medical_type' in d:
            o.medical_type = d['medical_type']
        if 'visit_date' in d:
            o.visit_date = d['visit_date']
        return o


