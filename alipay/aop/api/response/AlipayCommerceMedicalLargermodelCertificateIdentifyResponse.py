#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BirthCertificateDTO import BirthCertificateDTO
from alipay.aop.api.domain.HouseholdRegistrationDTO import HouseholdRegistrationDTO


class AlipayCommerceMedicalLargermodelCertificateIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelCertificateIdentifyResponse, self).__init__()
        self._birth_certificate = None
        self._household_registration = None

    @property
    def birth_certificate(self):
        return self._birth_certificate

    @birth_certificate.setter
    def birth_certificate(self, value):
        if isinstance(value, BirthCertificateDTO):
            self._birth_certificate = value
        else:
            self._birth_certificate = BirthCertificateDTO.from_alipay_dict(value)
    @property
    def household_registration(self):
        return self._household_registration

    @household_registration.setter
    def household_registration(self, value):
        if isinstance(value, HouseholdRegistrationDTO):
            self._household_registration = value
        else:
            self._household_registration = HouseholdRegistrationDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelCertificateIdentifyResponse, self).parse_response_content(response_content)
        if 'birth_certificate' in response:
            self.birth_certificate = response['birth_certificate']
        if 'household_registration' in response:
            self.household_registration = response['household_registration']
