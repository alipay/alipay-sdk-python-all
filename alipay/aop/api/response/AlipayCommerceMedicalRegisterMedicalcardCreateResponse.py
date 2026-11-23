#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterMedicalcardCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterMedicalcardCreateResponse, self).__init__()
        self._medical_card_prop = None
        self._patient_id = None

    @property
    def medical_card_prop(self):
        return self._medical_card_prop

    @medical_card_prop.setter
    def medical_card_prop(self, value):
        self._medical_card_prop = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterMedicalcardCreateResponse, self).parse_response_content(response_content)
        if 'medical_card_prop' in response:
            self.medical_card_prop = response['medical_card_prop']
        if 'patient_id' in response:
            self.patient_id = response['patient_id']
