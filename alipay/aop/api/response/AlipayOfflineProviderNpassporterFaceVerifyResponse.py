#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpassporterFaceVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterFaceVerifyResponse, self).__init__()
        self._cert_type = None
        self._encrypt_cert_no = None

    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def encrypt_cert_no(self):
        return self._encrypt_cert_no

    @encrypt_cert_no.setter
    def encrypt_cert_no(self, value):
        self._encrypt_cert_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterFaceVerifyResponse, self).parse_response_content(response_content)
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'encrypt_cert_no' in response:
            self.encrypt_cert_no = response['encrypt_cert_no']
