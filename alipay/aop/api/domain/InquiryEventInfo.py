#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InquiryEventInfo(object):

    def __init__(self):
        self._consult_summary_url = None
        self._consult_time = None
        self._doctor_name = None
        self._patient_name = None
        self._prescription_url = None
        self._reserve_jump_url = None
        self._reserved_doctor_name = None
        self._reserved_time = None

    @property
    def consult_summary_url(self):
        return self._consult_summary_url

    @consult_summary_url.setter
    def consult_summary_url(self, value):
        self._consult_summary_url = value
    @property
    def consult_time(self):
        return self._consult_time

    @consult_time.setter
    def consult_time(self, value):
        self._consult_time = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def prescription_url(self):
        return self._prescription_url

    @prescription_url.setter
    def prescription_url(self, value):
        self._prescription_url = value
    @property
    def reserve_jump_url(self):
        return self._reserve_jump_url

    @reserve_jump_url.setter
    def reserve_jump_url(self, value):
        self._reserve_jump_url = value
    @property
    def reserved_doctor_name(self):
        return self._reserved_doctor_name

    @reserved_doctor_name.setter
    def reserved_doctor_name(self, value):
        self._reserved_doctor_name = value
    @property
    def reserved_time(self):
        return self._reserved_time

    @reserved_time.setter
    def reserved_time(self, value):
        self._reserved_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_summary_url:
            if hasattr(self.consult_summary_url, 'to_alipay_dict'):
                params['consult_summary_url'] = self.consult_summary_url.to_alipay_dict()
            else:
                params['consult_summary_url'] = self.consult_summary_url
        if self.consult_time:
            if hasattr(self.consult_time, 'to_alipay_dict'):
                params['consult_time'] = self.consult_time.to_alipay_dict()
            else:
                params['consult_time'] = self.consult_time
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.prescription_url:
            if hasattr(self.prescription_url, 'to_alipay_dict'):
                params['prescription_url'] = self.prescription_url.to_alipay_dict()
            else:
                params['prescription_url'] = self.prescription_url
        if self.reserve_jump_url:
            if hasattr(self.reserve_jump_url, 'to_alipay_dict'):
                params['reserve_jump_url'] = self.reserve_jump_url.to_alipay_dict()
            else:
                params['reserve_jump_url'] = self.reserve_jump_url
        if self.reserved_doctor_name:
            if hasattr(self.reserved_doctor_name, 'to_alipay_dict'):
                params['reserved_doctor_name'] = self.reserved_doctor_name.to_alipay_dict()
            else:
                params['reserved_doctor_name'] = self.reserved_doctor_name
        if self.reserved_time:
            if hasattr(self.reserved_time, 'to_alipay_dict'):
                params['reserved_time'] = self.reserved_time.to_alipay_dict()
            else:
                params['reserved_time'] = self.reserved_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryEventInfo()
        if 'consult_summary_url' in d:
            o.consult_summary_url = d['consult_summary_url']
        if 'consult_time' in d:
            o.consult_time = d['consult_time']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'prescription_url' in d:
            o.prescription_url = d['prescription_url']
        if 'reserve_jump_url' in d:
            o.reserve_jump_url = d['reserve_jump_url']
        if 'reserved_doctor_name' in d:
            o.reserved_doctor_name = d['reserved_doctor_name']
        if 'reserved_time' in d:
            o.reserved_time = d['reserved_time']
        return o


