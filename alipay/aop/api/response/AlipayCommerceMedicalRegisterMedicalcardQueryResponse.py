#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegisterMedicalCardVO import RegisterMedicalCardVO


class AlipayCommerceMedicalRegisterMedicalcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterMedicalcardQueryResponse, self).__init__()
        self._medicalcards = None

    @property
    def medicalcards(self):
        return self._medicalcards

    @medicalcards.setter
    def medicalcards(self, value):
        if isinstance(value, list):
            self._medicalcards = list()
            for i in value:
                if isinstance(i, RegisterMedicalCardVO):
                    self._medicalcards.append(i)
                else:
                    self._medicalcards.append(RegisterMedicalCardVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterMedicalcardQueryResponse, self).parse_response_content(response_content)
        if 'medicalcards' in response:
            self.medicalcards = response['medicalcards']
