#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HealthInspectionReport import HealthInspectionReport
from alipay.aop.api.domain.HealthLaboratoryReport import HealthLaboratoryReport


class HealthReport(object):

    def __init__(self):
        self._age = None
        self._data_id = None
        self._data_source = None
        self._hospital_name = None
        self._hospital_org_id = None
        self._inspection_report_list = None
        self._laboratory_report_list = None
        self._memo = None
        self._report_id = None
        self._report_name = None
        self._report_time = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def hospital_org_id(self):
        return self._hospital_org_id

    @hospital_org_id.setter
    def hospital_org_id(self, value):
        self._hospital_org_id = value
    @property
    def inspection_report_list(self):
        return self._inspection_report_list

    @inspection_report_list.setter
    def inspection_report_list(self, value):
        if isinstance(value, list):
            self._inspection_report_list = list()
            for i in value:
                if isinstance(i, HealthInspectionReport):
                    self._inspection_report_list.append(i)
                else:
                    self._inspection_report_list.append(HealthInspectionReport.from_alipay_dict(i))
    @property
    def laboratory_report_list(self):
        return self._laboratory_report_list

    @laboratory_report_list.setter
    def laboratory_report_list(self, value):
        if isinstance(value, list):
            self._laboratory_report_list = list()
            for i in value:
                if isinstance(i, HealthLaboratoryReport):
                    self._laboratory_report_list.append(i)
                else:
                    self._laboratory_report_list.append(HealthLaboratoryReport.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, value):
        self._report_id = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.hospital_org_id:
            if hasattr(self.hospital_org_id, 'to_alipay_dict'):
                params['hospital_org_id'] = self.hospital_org_id.to_alipay_dict()
            else:
                params['hospital_org_id'] = self.hospital_org_id
        if self.inspection_report_list:
            if isinstance(self.inspection_report_list, list):
                for i in range(0, len(self.inspection_report_list)):
                    element = self.inspection_report_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inspection_report_list[i] = element.to_alipay_dict()
            if hasattr(self.inspection_report_list, 'to_alipay_dict'):
                params['inspection_report_list'] = self.inspection_report_list.to_alipay_dict()
            else:
                params['inspection_report_list'] = self.inspection_report_list
        if self.laboratory_report_list:
            if isinstance(self.laboratory_report_list, list):
                for i in range(0, len(self.laboratory_report_list)):
                    element = self.laboratory_report_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.laboratory_report_list[i] = element.to_alipay_dict()
            if hasattr(self.laboratory_report_list, 'to_alipay_dict'):
                params['laboratory_report_list'] = self.laboratory_report_list.to_alipay_dict()
            else:
                params['laboratory_report_list'] = self.laboratory_report_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.report_id:
            if hasattr(self.report_id, 'to_alipay_dict'):
                params['report_id'] = self.report_id.to_alipay_dict()
            else:
                params['report_id'] = self.report_id
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthReport()
        if 'age' in d:
            o.age = d['age']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hospital_org_id' in d:
            o.hospital_org_id = d['hospital_org_id']
        if 'inspection_report_list' in d:
            o.inspection_report_list = d['inspection_report_list']
        if 'laboratory_report_list' in d:
            o.laboratory_report_list = d['laboratory_report_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_time' in d:
            o.report_time = d['report_time']
        return o


