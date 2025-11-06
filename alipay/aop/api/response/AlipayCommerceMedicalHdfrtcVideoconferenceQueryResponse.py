#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConferenceInfo import ConferenceInfo
from alipay.aop.api.domain.DoctorDetails import DoctorDetails
from alipay.aop.api.domain.PatientDetails import PatientDetails
from alipay.aop.api.domain.RtcBaseInfo import RtcBaseInfo


class AlipayCommerceMedicalHdfrtcVideoconferenceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferenceQueryResponse, self).__init__()
        self._conference_info = None
        self._doctor_info = None
        self._patient_info = None
        self._rtc_base_info = None

    @property
    def conference_info(self):
        return self._conference_info

    @conference_info.setter
    def conference_info(self, value):
        if isinstance(value, ConferenceInfo):
            self._conference_info = value
        else:
            self._conference_info = ConferenceInfo.from_alipay_dict(value)
    @property
    def doctor_info(self):
        return self._doctor_info

    @doctor_info.setter
    def doctor_info(self, value):
        if isinstance(value, DoctorDetails):
            self._doctor_info = value
        else:
            self._doctor_info = DoctorDetails.from_alipay_dict(value)
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, PatientDetails):
            self._patient_info = value
        else:
            self._patient_info = PatientDetails.from_alipay_dict(value)
    @property
    def rtc_base_info(self):
        return self._rtc_base_info

    @rtc_base_info.setter
    def rtc_base_info(self, value):
        if isinstance(value, RtcBaseInfo):
            self._rtc_base_info = value
        else:
            self._rtc_base_info = RtcBaseInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferenceQueryResponse, self).parse_response_content(response_content)
        if 'conference_info' in response:
            self.conference_info = response['conference_info']
        if 'doctor_info' in response:
            self.doctor_info = response['doctor_info']
        if 'patient_info' in response:
            self.patient_info = response['patient_info']
        if 'rtc_base_info' in response:
            self.rtc_base_info = response['rtc_base_info']
