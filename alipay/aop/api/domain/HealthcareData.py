#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckReport import CheckReport
from alipay.aop.api.domain.InpatientRecord import InpatientRecord
from alipay.aop.api.domain.OutpatientPrescription import OutpatientPrescription
from alipay.aop.api.domain.OutpatientRecord import OutpatientRecord


class HealthcareData(object):

    def __init__(self):
        self._check_report_list = None
        self._inpatient_record_list = None
        self._outpatient_prescription_list = None
        self._outpatient_record_list = None
        self._pic_type = None
        self._pic_url = None

    @property
    def check_report_list(self):
        return self._check_report_list

    @check_report_list.setter
    def check_report_list(self, value):
        if isinstance(value, list):
            self._check_report_list = list()
            for i in value:
                if isinstance(i, CheckReport):
                    self._check_report_list.append(i)
                else:
                    self._check_report_list.append(CheckReport.from_alipay_dict(i))
    @property
    def inpatient_record_list(self):
        return self._inpatient_record_list

    @inpatient_record_list.setter
    def inpatient_record_list(self, value):
        if isinstance(value, list):
            self._inpatient_record_list = list()
            for i in value:
                if isinstance(i, InpatientRecord):
                    self._inpatient_record_list.append(i)
                else:
                    self._inpatient_record_list.append(InpatientRecord.from_alipay_dict(i))
    @property
    def outpatient_prescription_list(self):
        return self._outpatient_prescription_list

    @outpatient_prescription_list.setter
    def outpatient_prescription_list(self, value):
        if isinstance(value, list):
            self._outpatient_prescription_list = list()
            for i in value:
                if isinstance(i, OutpatientPrescription):
                    self._outpatient_prescription_list.append(i)
                else:
                    self._outpatient_prescription_list.append(OutpatientPrescription.from_alipay_dict(i))
    @property
    def outpatient_record_list(self):
        return self._outpatient_record_list

    @outpatient_record_list.setter
    def outpatient_record_list(self, value):
        if isinstance(value, list):
            self._outpatient_record_list = list()
            for i in value:
                if isinstance(i, OutpatientRecord):
                    self._outpatient_record_list.append(i)
                else:
                    self._outpatient_record_list.append(OutpatientRecord.from_alipay_dict(i))
    @property
    def pic_type(self):
        return self._pic_type

    @pic_type.setter
    def pic_type(self, value):
        self._pic_type = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_report_list:
            if isinstance(self.check_report_list, list):
                for i in range(0, len(self.check_report_list)):
                    element = self.check_report_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_report_list[i] = element.to_alipay_dict()
            if hasattr(self.check_report_list, 'to_alipay_dict'):
                params['check_report_list'] = self.check_report_list.to_alipay_dict()
            else:
                params['check_report_list'] = self.check_report_list
        if self.inpatient_record_list:
            if isinstance(self.inpatient_record_list, list):
                for i in range(0, len(self.inpatient_record_list)):
                    element = self.inpatient_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inpatient_record_list[i] = element.to_alipay_dict()
            if hasattr(self.inpatient_record_list, 'to_alipay_dict'):
                params['inpatient_record_list'] = self.inpatient_record_list.to_alipay_dict()
            else:
                params['inpatient_record_list'] = self.inpatient_record_list
        if self.outpatient_prescription_list:
            if isinstance(self.outpatient_prescription_list, list):
                for i in range(0, len(self.outpatient_prescription_list)):
                    element = self.outpatient_prescription_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.outpatient_prescription_list[i] = element.to_alipay_dict()
            if hasattr(self.outpatient_prescription_list, 'to_alipay_dict'):
                params['outpatient_prescription_list'] = self.outpatient_prescription_list.to_alipay_dict()
            else:
                params['outpatient_prescription_list'] = self.outpatient_prescription_list
        if self.outpatient_record_list:
            if isinstance(self.outpatient_record_list, list):
                for i in range(0, len(self.outpatient_record_list)):
                    element = self.outpatient_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.outpatient_record_list[i] = element.to_alipay_dict()
            if hasattr(self.outpatient_record_list, 'to_alipay_dict'):
                params['outpatient_record_list'] = self.outpatient_record_list.to_alipay_dict()
            else:
                params['outpatient_record_list'] = self.outpatient_record_list
        if self.pic_type:
            if hasattr(self.pic_type, 'to_alipay_dict'):
                params['pic_type'] = self.pic_type.to_alipay_dict()
            else:
                params['pic_type'] = self.pic_type
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthcareData()
        if 'check_report_list' in d:
            o.check_report_list = d['check_report_list']
        if 'inpatient_record_list' in d:
            o.inpatient_record_list = d['inpatient_record_list']
        if 'outpatient_prescription_list' in d:
            o.outpatient_prescription_list = d['outpatient_prescription_list']
        if 'outpatient_record_list' in d:
            o.outpatient_record_list = d['outpatient_record_list']
        if 'pic_type' in d:
            o.pic_type = d['pic_type']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        return o


