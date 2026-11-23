#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegisterPatientDetailInfo import RegisterPatientDetailInfo
from alipay.aop.api.domain.MedicalRegisterOrderInfo import MedicalRegisterOrderInfo


class AlipayCommerceMedicalRegisterOrderdetailinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterOrderdetailinfoQueryResponse, self).__init__()
        self._button_gray_tips = None
        self._button_status = None
        self._patient_info = None
        self._register_info = None
        self._scm_info = None

    @property
    def button_gray_tips(self):
        return self._button_gray_tips

    @button_gray_tips.setter
    def button_gray_tips(self, value):
        self._button_gray_tips = value
    @property
    def button_status(self):
        return self._button_status

    @button_status.setter
    def button_status(self, value):
        self._button_status = value
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, RegisterPatientDetailInfo):
            self._patient_info = value
        else:
            self._patient_info = RegisterPatientDetailInfo.from_alipay_dict(value)
    @property
    def register_info(self):
        return self._register_info

    @register_info.setter
    def register_info(self, value):
        if isinstance(value, MedicalRegisterOrderInfo):
            self._register_info = value
        else:
            self._register_info = MedicalRegisterOrderInfo.from_alipay_dict(value)
    @property
    def scm_info(self):
        return self._scm_info

    @scm_info.setter
    def scm_info(self, value):
        self._scm_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterOrderdetailinfoQueryResponse, self).parse_response_content(response_content)
        if 'button_gray_tips' in response:
            self.button_gray_tips = response['button_gray_tips']
        if 'button_status' in response:
            self.button_status = response['button_status']
        if 'patient_info' in response:
            self.patient_info = response['patient_info']
        if 'register_info' in response:
            self.register_info = response['register_info']
        if 'scm_info' in response:
            self.scm_info = response['scm_info']
