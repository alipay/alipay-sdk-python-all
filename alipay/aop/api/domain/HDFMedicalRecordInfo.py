#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HDFMedicalSummary import HDFMedicalSummary
from alipay.aop.api.domain.HDFPatientAttachment import HDFPatientAttachment


class HDFMedicalRecordInfo(object):

    def __init__(self):
        self._medical_summary = None
        self._paper_order_id = None
        self._patient_attachment_list = None
        self._service_end_time = None
        self._service_start_time = None

    @property
    def medical_summary(self):
        return self._medical_summary

    @medical_summary.setter
    def medical_summary(self, value):
        if isinstance(value, HDFMedicalSummary):
            self._medical_summary = value
        else:
            self._medical_summary = HDFMedicalSummary.from_alipay_dict(value)
    @property
    def paper_order_id(self):
        return self._paper_order_id

    @paper_order_id.setter
    def paper_order_id(self, value):
        self._paper_order_id = value
    @property
    def patient_attachment_list(self):
        return self._patient_attachment_list

    @patient_attachment_list.setter
    def patient_attachment_list(self, value):
        if isinstance(value, list):
            self._patient_attachment_list = list()
            for i in value:
                if isinstance(i, HDFPatientAttachment):
                    self._patient_attachment_list.append(i)
                else:
                    self._patient_attachment_list.append(HDFPatientAttachment.from_alipay_dict(i))
    @property
    def service_end_time(self):
        return self._service_end_time

    @service_end_time.setter
    def service_end_time(self, value):
        self._service_end_time = value
    @property
    def service_start_time(self):
        return self._service_start_time

    @service_start_time.setter
    def service_start_time(self, value):
        self._service_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.medical_summary:
            if hasattr(self.medical_summary, 'to_alipay_dict'):
                params['medical_summary'] = self.medical_summary.to_alipay_dict()
            else:
                params['medical_summary'] = self.medical_summary
        if self.paper_order_id:
            if hasattr(self.paper_order_id, 'to_alipay_dict'):
                params['paper_order_id'] = self.paper_order_id.to_alipay_dict()
            else:
                params['paper_order_id'] = self.paper_order_id
        if self.patient_attachment_list:
            if isinstance(self.patient_attachment_list, list):
                for i in range(0, len(self.patient_attachment_list)):
                    element = self.patient_attachment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.patient_attachment_list[i] = element.to_alipay_dict()
            if hasattr(self.patient_attachment_list, 'to_alipay_dict'):
                params['patient_attachment_list'] = self.patient_attachment_list.to_alipay_dict()
            else:
                params['patient_attachment_list'] = self.patient_attachment_list
        if self.service_end_time:
            if hasattr(self.service_end_time, 'to_alipay_dict'):
                params['service_end_time'] = self.service_end_time.to_alipay_dict()
            else:
                params['service_end_time'] = self.service_end_time
        if self.service_start_time:
            if hasattr(self.service_start_time, 'to_alipay_dict'):
                params['service_start_time'] = self.service_start_time.to_alipay_dict()
            else:
                params['service_start_time'] = self.service_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFMedicalRecordInfo()
        if 'medical_summary' in d:
            o.medical_summary = d['medical_summary']
        if 'paper_order_id' in d:
            o.paper_order_id = d['paper_order_id']
        if 'patient_attachment_list' in d:
            o.patient_attachment_list = d['patient_attachment_list']
        if 'service_end_time' in d:
            o.service_end_time = d['service_end_time']
        if 'service_start_time' in d:
            o.service_start_time = d['service_start_time']
        return o


