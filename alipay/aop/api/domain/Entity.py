#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Entity(object):

    def __init__(self):
        self._case_id = None
        self._case_type = None
        self._department = None
        self._disease = None
        self._event_id = None

    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value
    @property
    def case_type(self):
        return self._case_type

    @case_type.setter
    def case_type(self, value):
        self._case_type = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def disease(self):
        return self._disease

    @disease.setter
    def disease(self, value):
        self._disease = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_id:
            if hasattr(self.case_id, 'to_alipay_dict'):
                params['case_id'] = self.case_id.to_alipay_dict()
            else:
                params['case_id'] = self.case_id
        if self.case_type:
            if hasattr(self.case_type, 'to_alipay_dict'):
                params['case_type'] = self.case_type.to_alipay_dict()
            else:
                params['case_type'] = self.case_type
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.disease:
            if hasattr(self.disease, 'to_alipay_dict'):
                params['disease'] = self.disease.to_alipay_dict()
            else:
                params['disease'] = self.disease
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Entity()
        if 'case_id' in d:
            o.case_id = d['case_id']
        if 'case_type' in d:
            o.case_type = d['case_type']
        if 'department' in d:
            o.department = d['department']
        if 'disease' in d:
            o.disease = d['disease']
        if 'event_id' in d:
            o.event_id = d['event_id']
        return o


