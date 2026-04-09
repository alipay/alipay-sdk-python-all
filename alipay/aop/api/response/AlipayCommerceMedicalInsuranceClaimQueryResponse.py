#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EncryptRequest import EncryptRequest


class AlipayCommerceMedicalInsuranceClaimQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceClaimQueryResponse, self).__init__()
        self._encrypt_response = None

    @property
    def encrypt_response(self):
        return self._encrypt_response

    @encrypt_response.setter
    def encrypt_response(self, value):
        if isinstance(value, EncryptRequest):
            self._encrypt_response = value
        else:
            self._encrypt_response = EncryptRequest.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceClaimQueryResponse, self).parse_response_content(response_content)
        if 'encrypt_response' in response:
            self.encrypt_response = response['encrypt_response']
