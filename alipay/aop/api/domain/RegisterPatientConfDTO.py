#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterPatientConfDTO(object):

    def __init__(self):
        self._add_patient_url = None
        self._need_query_patient = None
        self._patient_source = None

    @property
    def add_patient_url(self):
        return self._add_patient_url

    @add_patient_url.setter
    def add_patient_url(self, value):
        self._add_patient_url = value
    @property
    def need_query_patient(self):
        return self._need_query_patient

    @need_query_patient.setter
    def need_query_patient(self, value):
        self._need_query_patient = value
    @property
    def patient_source(self):
        return self._patient_source

    @patient_source.setter
    def patient_source(self, value):
        self._patient_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_patient_url:
            if hasattr(self.add_patient_url, 'to_alipay_dict'):
                params['add_patient_url'] = self.add_patient_url.to_alipay_dict()
            else:
                params['add_patient_url'] = self.add_patient_url
        if self.need_query_patient:
            if hasattr(self.need_query_patient, 'to_alipay_dict'):
                params['need_query_patient'] = self.need_query_patient.to_alipay_dict()
            else:
                params['need_query_patient'] = self.need_query_patient
        if self.patient_source:
            if hasattr(self.patient_source, 'to_alipay_dict'):
                params['patient_source'] = self.patient_source.to_alipay_dict()
            else:
                params['patient_source'] = self.patient_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterPatientConfDTO()
        if 'add_patient_url' in d:
            o.add_patient_url = d['add_patient_url']
        if 'need_query_patient' in d:
            o.need_query_patient = d['need_query_patient']
        if 'patient_source' in d:
            o.patient_source = d['patient_source']
        return o


