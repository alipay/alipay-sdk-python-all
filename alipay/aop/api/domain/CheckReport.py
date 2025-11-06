#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InspectionReport import InspectionReport
from alipay.aop.api.domain.LaboratoryReport import LaboratoryReport


class CheckReport(object):

    def __init__(self):
        self._data_id = None
        self._data_source = None
        self._hospital_name = None
        self._hospital_org_id = None
        self._inspection_report = None
        self._laboratory_report = None
        self._report_id = None
        self._report_name = None
        self._report_time = None
        self._report_type = None

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
    def inspection_report(self):
        return self._inspection_report

    @inspection_report.setter
    def inspection_report(self, value):
        if isinstance(value, InspectionReport):
            self._inspection_report = value
        else:
            self._inspection_report = InspectionReport.from_alipay_dict(value)
    @property
    def laboratory_report(self):
        return self._laboratory_report

    @laboratory_report.setter
    def laboratory_report(self, value):
        if isinstance(value, LaboratoryReport):
            self._laboratory_report = value
        else:
            self._laboratory_report = LaboratoryReport.from_alipay_dict(value)
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
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.inspection_report:
            if hasattr(self.inspection_report, 'to_alipay_dict'):
                params['inspection_report'] = self.inspection_report.to_alipay_dict()
            else:
                params['inspection_report'] = self.inspection_report
        if self.laboratory_report:
            if hasattr(self.laboratory_report, 'to_alipay_dict'):
                params['laboratory_report'] = self.laboratory_report.to_alipay_dict()
            else:
                params['laboratory_report'] = self.laboratory_report
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
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckReport()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hospital_org_id' in d:
            o.hospital_org_id = d['hospital_org_id']
        if 'inspection_report' in d:
            o.inspection_report = d['inspection_report']
        if 'laboratory_report' in d:
            o.laboratory_report = d['laboratory_report']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_time' in d:
            o.report_time = d['report_time']
        if 'report_type' in d:
            o.report_type = d['report_type']
        return o


