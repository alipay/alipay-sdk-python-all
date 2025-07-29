#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsCbddoctorDiagnosisFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsCbddoctorDiagnosisFinishResponse, self).__init__()
        self._disposal_advice = None
        self._doctor_beneficial = None
        self._illness_desc = None
        self._patient_age = None
        self._patient_gender = None

    @property
    def disposal_advice(self):
        return self._disposal_advice

    @disposal_advice.setter
    def disposal_advice(self, value):
        self._disposal_advice = value
    @property
    def doctor_beneficial(self):
        return self._doctor_beneficial

    @doctor_beneficial.setter
    def doctor_beneficial(self, value):
        self._doctor_beneficial = value
    @property
    def illness_desc(self):
        return self._illness_desc

    @illness_desc.setter
    def illness_desc(self, value):
        self._illness_desc = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_gender(self):
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, value):
        self._patient_gender = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsCbddoctorDiagnosisFinishResponse, self).parse_response_content(response_content)
        if 'disposal_advice' in response:
            self.disposal_advice = response['disposal_advice']
        if 'doctor_beneficial' in response:
            self.doctor_beneficial = response['doctor_beneficial']
        if 'illness_desc' in response:
            self.illness_desc = response['illness_desc']
        if 'patient_age' in response:
            self.patient_age = response['patient_age']
        if 'patient_gender' in response:
            self.patient_gender = response['patient_gender']
