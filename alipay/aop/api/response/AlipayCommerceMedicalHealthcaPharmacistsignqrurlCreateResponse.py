#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHealthcaPharmacistsignqrurlCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthcaPharmacistsignqrurlCreateResponse, self).__init__()
        self._qr_url = None
        self._sign_flow_id = None

    @property
    def qr_url(self):
        return self._qr_url

    @qr_url.setter
    def qr_url(self, value):
        self._qr_url = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthcaPharmacistsignqrurlCreateResponse, self).parse_response_content(response_content)
        if 'qr_url' in response:
            self.qr_url = response['qr_url']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
