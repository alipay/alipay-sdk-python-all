#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceResult(object):

    def __init__(self):
        self._actual_department = None
        self._actual_hospital = None
        self._medical_advice = None
        self._service_summary_photo_url_list = None
        self._special_requirements_record = None
        self._survey_attachment_url_list = None

    @property
    def actual_department(self):
        return self._actual_department

    @actual_department.setter
    def actual_department(self, value):
        self._actual_department = value
    @property
    def actual_hospital(self):
        return self._actual_hospital

    @actual_hospital.setter
    def actual_hospital(self, value):
        self._actual_hospital = value
    @property
    def medical_advice(self):
        return self._medical_advice

    @medical_advice.setter
    def medical_advice(self, value):
        self._medical_advice = value
    @property
    def service_summary_photo_url_list(self):
        return self._service_summary_photo_url_list

    @service_summary_photo_url_list.setter
    def service_summary_photo_url_list(self, value):
        if isinstance(value, list):
            self._service_summary_photo_url_list = list()
            for i in value:
                self._service_summary_photo_url_list.append(i)
    @property
    def special_requirements_record(self):
        return self._special_requirements_record

    @special_requirements_record.setter
    def special_requirements_record(self, value):
        self._special_requirements_record = value
    @property
    def survey_attachment_url_list(self):
        return self._survey_attachment_url_list

    @survey_attachment_url_list.setter
    def survey_attachment_url_list(self, value):
        if isinstance(value, list):
            self._survey_attachment_url_list = list()
            for i in value:
                self._survey_attachment_url_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.actual_department:
            if hasattr(self.actual_department, 'to_alipay_dict'):
                params['actual_department'] = self.actual_department.to_alipay_dict()
            else:
                params['actual_department'] = self.actual_department
        if self.actual_hospital:
            if hasattr(self.actual_hospital, 'to_alipay_dict'):
                params['actual_hospital'] = self.actual_hospital.to_alipay_dict()
            else:
                params['actual_hospital'] = self.actual_hospital
        if self.medical_advice:
            if hasattr(self.medical_advice, 'to_alipay_dict'):
                params['medical_advice'] = self.medical_advice.to_alipay_dict()
            else:
                params['medical_advice'] = self.medical_advice
        if self.service_summary_photo_url_list:
            if isinstance(self.service_summary_photo_url_list, list):
                for i in range(0, len(self.service_summary_photo_url_list)):
                    element = self.service_summary_photo_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_summary_photo_url_list[i] = element.to_alipay_dict()
            if hasattr(self.service_summary_photo_url_list, 'to_alipay_dict'):
                params['service_summary_photo_url_list'] = self.service_summary_photo_url_list.to_alipay_dict()
            else:
                params['service_summary_photo_url_list'] = self.service_summary_photo_url_list
        if self.special_requirements_record:
            if hasattr(self.special_requirements_record, 'to_alipay_dict'):
                params['special_requirements_record'] = self.special_requirements_record.to_alipay_dict()
            else:
                params['special_requirements_record'] = self.special_requirements_record
        if self.survey_attachment_url_list:
            if isinstance(self.survey_attachment_url_list, list):
                for i in range(0, len(self.survey_attachment_url_list)):
                    element = self.survey_attachment_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.survey_attachment_url_list[i] = element.to_alipay_dict()
            if hasattr(self.survey_attachment_url_list, 'to_alipay_dict'):
                params['survey_attachment_url_list'] = self.survey_attachment_url_list.to_alipay_dict()
            else:
                params['survey_attachment_url_list'] = self.survey_attachment_url_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceResult()
        if 'actual_department' in d:
            o.actual_department = d['actual_department']
        if 'actual_hospital' in d:
            o.actual_hospital = d['actual_hospital']
        if 'medical_advice' in d:
            o.medical_advice = d['medical_advice']
        if 'service_summary_photo_url_list' in d:
            o.service_summary_photo_url_list = d['service_summary_photo_url_list']
        if 'special_requirements_record' in d:
            o.special_requirements_record = d['special_requirements_record']
        if 'survey_attachment_url_list' in d:
            o.survey_attachment_url_list = d['survey_attachment_url_list']
        return o


