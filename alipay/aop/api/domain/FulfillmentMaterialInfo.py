#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FulfillmentMaterialInfo(object):

    def __init__(self):
        self._examination_appointment_url = None
        self._examination_report_url = None
        self._hospitalization_notice_url = None
        self._hospitalization_record_url = None
        self._outpatient_record_url = None
        self._pathology_report_url = None
        self._patient_card_url = None
        self._registration_slip_url = None
        self._surgery_notice_url = None

    @property
    def examination_appointment_url(self):
        return self._examination_appointment_url

    @examination_appointment_url.setter
    def examination_appointment_url(self, value):
        self._examination_appointment_url = value
    @property
    def examination_report_url(self):
        return self._examination_report_url

    @examination_report_url.setter
    def examination_report_url(self, value):
        self._examination_report_url = value
    @property
    def hospitalization_notice_url(self):
        return self._hospitalization_notice_url

    @hospitalization_notice_url.setter
    def hospitalization_notice_url(self, value):
        self._hospitalization_notice_url = value
    @property
    def hospitalization_record_url(self):
        return self._hospitalization_record_url

    @hospitalization_record_url.setter
    def hospitalization_record_url(self, value):
        self._hospitalization_record_url = value
    @property
    def outpatient_record_url(self):
        return self._outpatient_record_url

    @outpatient_record_url.setter
    def outpatient_record_url(self, value):
        self._outpatient_record_url = value
    @property
    def pathology_report_url(self):
        return self._pathology_report_url

    @pathology_report_url.setter
    def pathology_report_url(self, value):
        self._pathology_report_url = value
    @property
    def patient_card_url(self):
        return self._patient_card_url

    @patient_card_url.setter
    def patient_card_url(self, value):
        self._patient_card_url = value
    @property
    def registration_slip_url(self):
        return self._registration_slip_url

    @registration_slip_url.setter
    def registration_slip_url(self, value):
        self._registration_slip_url = value
    @property
    def surgery_notice_url(self):
        return self._surgery_notice_url

    @surgery_notice_url.setter
    def surgery_notice_url(self, value):
        self._surgery_notice_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.examination_appointment_url:
            if hasattr(self.examination_appointment_url, 'to_alipay_dict'):
                params['examination_appointment_url'] = self.examination_appointment_url.to_alipay_dict()
            else:
                params['examination_appointment_url'] = self.examination_appointment_url
        if self.examination_report_url:
            if hasattr(self.examination_report_url, 'to_alipay_dict'):
                params['examination_report_url'] = self.examination_report_url.to_alipay_dict()
            else:
                params['examination_report_url'] = self.examination_report_url
        if self.hospitalization_notice_url:
            if hasattr(self.hospitalization_notice_url, 'to_alipay_dict'):
                params['hospitalization_notice_url'] = self.hospitalization_notice_url.to_alipay_dict()
            else:
                params['hospitalization_notice_url'] = self.hospitalization_notice_url
        if self.hospitalization_record_url:
            if hasattr(self.hospitalization_record_url, 'to_alipay_dict'):
                params['hospitalization_record_url'] = self.hospitalization_record_url.to_alipay_dict()
            else:
                params['hospitalization_record_url'] = self.hospitalization_record_url
        if self.outpatient_record_url:
            if hasattr(self.outpatient_record_url, 'to_alipay_dict'):
                params['outpatient_record_url'] = self.outpatient_record_url.to_alipay_dict()
            else:
                params['outpatient_record_url'] = self.outpatient_record_url
        if self.pathology_report_url:
            if hasattr(self.pathology_report_url, 'to_alipay_dict'):
                params['pathology_report_url'] = self.pathology_report_url.to_alipay_dict()
            else:
                params['pathology_report_url'] = self.pathology_report_url
        if self.patient_card_url:
            if hasattr(self.patient_card_url, 'to_alipay_dict'):
                params['patient_card_url'] = self.patient_card_url.to_alipay_dict()
            else:
                params['patient_card_url'] = self.patient_card_url
        if self.registration_slip_url:
            if hasattr(self.registration_slip_url, 'to_alipay_dict'):
                params['registration_slip_url'] = self.registration_slip_url.to_alipay_dict()
            else:
                params['registration_slip_url'] = self.registration_slip_url
        if self.surgery_notice_url:
            if hasattr(self.surgery_notice_url, 'to_alipay_dict'):
                params['surgery_notice_url'] = self.surgery_notice_url.to_alipay_dict()
            else:
                params['surgery_notice_url'] = self.surgery_notice_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentMaterialInfo()
        if 'examination_appointment_url' in d:
            o.examination_appointment_url = d['examination_appointment_url']
        if 'examination_report_url' in d:
            o.examination_report_url = d['examination_report_url']
        if 'hospitalization_notice_url' in d:
            o.hospitalization_notice_url = d['hospitalization_notice_url']
        if 'hospitalization_record_url' in d:
            o.hospitalization_record_url = d['hospitalization_record_url']
        if 'outpatient_record_url' in d:
            o.outpatient_record_url = d['outpatient_record_url']
        if 'pathology_report_url' in d:
            o.pathology_report_url = d['pathology_report_url']
        if 'patient_card_url' in d:
            o.patient_card_url = d['patient_card_url']
        if 'registration_slip_url' in d:
            o.registration_slip_url = d['registration_slip_url']
        if 'surgery_notice_url' in d:
            o.surgery_notice_url = d['surgery_notice_url']
        return o


