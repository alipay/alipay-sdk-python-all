#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiagnosisInfoDTO import DiagnosisInfoDTO
from alipay.aop.api.domain.DoctorInfoDTO import DoctorInfoDTO
from alipay.aop.api.domain.PatientInfoDTO import PatientInfoDTO


class MedicalBasicInfoDTO(object):

    def __init__(self):
        self._diagnosis_info = None
        self._faculty_name = None
        self._medical_card_no = None
        self._open_order_doctor_info = None
        self._patient_info = None

    @property
    def diagnosis_info(self):
        return self._diagnosis_info

    @diagnosis_info.setter
    def diagnosis_info(self, value):
        if isinstance(value, DiagnosisInfoDTO):
            self._diagnosis_info = value
        else:
            self._diagnosis_info = DiagnosisInfoDTO.from_alipay_dict(value)
    @property
    def faculty_name(self):
        return self._faculty_name

    @faculty_name.setter
    def faculty_name(self, value):
        self._faculty_name = value
    @property
    def medical_card_no(self):
        return self._medical_card_no

    @medical_card_no.setter
    def medical_card_no(self, value):
        self._medical_card_no = value
    @property
    def open_order_doctor_info(self):
        return self._open_order_doctor_info

    @open_order_doctor_info.setter
    def open_order_doctor_info(self, value):
        if isinstance(value, DoctorInfoDTO):
            self._open_order_doctor_info = value
        else:
            self._open_order_doctor_info = DoctorInfoDTO.from_alipay_dict(value)
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, PatientInfoDTO):
            self._patient_info = value
        else:
            self._patient_info = PatientInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.diagnosis_info:
            if hasattr(self.diagnosis_info, 'to_alipay_dict'):
                params['diagnosis_info'] = self.diagnosis_info.to_alipay_dict()
            else:
                params['diagnosis_info'] = self.diagnosis_info
        if self.faculty_name:
            if hasattr(self.faculty_name, 'to_alipay_dict'):
                params['faculty_name'] = self.faculty_name.to_alipay_dict()
            else:
                params['faculty_name'] = self.faculty_name
        if self.medical_card_no:
            if hasattr(self.medical_card_no, 'to_alipay_dict'):
                params['medical_card_no'] = self.medical_card_no.to_alipay_dict()
            else:
                params['medical_card_no'] = self.medical_card_no
        if self.open_order_doctor_info:
            if hasattr(self.open_order_doctor_info, 'to_alipay_dict'):
                params['open_order_doctor_info'] = self.open_order_doctor_info.to_alipay_dict()
            else:
                params['open_order_doctor_info'] = self.open_order_doctor_info
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalBasicInfoDTO()
        if 'diagnosis_info' in d:
            o.diagnosis_info = d['diagnosis_info']
        if 'faculty_name' in d:
            o.faculty_name = d['faculty_name']
        if 'medical_card_no' in d:
            o.medical_card_no = d['medical_card_no']
        if 'open_order_doctor_info' in d:
            o.open_order_doctor_info = d['open_order_doctor_info']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        return o


