#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutpatientRecord(object):

    def __init__(self):
        self._complaint = None
        self._data_id = None
        self._date = None
        self._department_name = None
        self._hospital_name = None
        self._illness_history = None
        self._physical_exam = None
        self._result = None
        self._treatment_advice = None
        self._type = None

    @property
    def complaint(self):
        return self._complaint

    @complaint.setter
    def complaint(self, value):
        self._complaint = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def illness_history(self):
        return self._illness_history

    @illness_history.setter
    def illness_history(self, value):
        self._illness_history = value
    @property
    def physical_exam(self):
        return self._physical_exam

    @physical_exam.setter
    def physical_exam(self, value):
        self._physical_exam = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def treatment_advice(self):
        return self._treatment_advice

    @treatment_advice.setter
    def treatment_advice(self, value):
        self._treatment_advice = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.complaint:
            if hasattr(self.complaint, 'to_alipay_dict'):
                params['complaint'] = self.complaint.to_alipay_dict()
            else:
                params['complaint'] = self.complaint
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.illness_history:
            if hasattr(self.illness_history, 'to_alipay_dict'):
                params['illness_history'] = self.illness_history.to_alipay_dict()
            else:
                params['illness_history'] = self.illness_history
        if self.physical_exam:
            if hasattr(self.physical_exam, 'to_alipay_dict'):
                params['physical_exam'] = self.physical_exam.to_alipay_dict()
            else:
                params['physical_exam'] = self.physical_exam
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.treatment_advice:
            if hasattr(self.treatment_advice, 'to_alipay_dict'):
                params['treatment_advice'] = self.treatment_advice.to_alipay_dict()
            else:
                params['treatment_advice'] = self.treatment_advice
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutpatientRecord()
        if 'complaint' in d:
            o.complaint = d['complaint']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'date' in d:
            o.date = d['date']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'illness_history' in d:
            o.illness_history = d['illness_history']
        if 'physical_exam' in d:
            o.physical_exam = d['physical_exam']
        if 'result' in d:
            o.result = d['result']
        if 'treatment_advice' in d:
            o.treatment_advice = d['treatment_advice']
        if 'type' in d:
            o.type = d['type']
        return o


