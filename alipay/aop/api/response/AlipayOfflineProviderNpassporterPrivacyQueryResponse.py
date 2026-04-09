#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpassporterPrivacyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterPrivacyQueryResponse, self).__init__()
        self._cert_type = None
        self._encrypt_cert_no_list = None

    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def encrypt_cert_no_list(self):
        return self._encrypt_cert_no_list

    @encrypt_cert_no_list.setter
    def encrypt_cert_no_list(self, value):
        if isinstance(value, list):
            self._encrypt_cert_no_list = list()
            for i in value:
                self._encrypt_cert_no_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterPrivacyQueryResponse, self).parse_response_content(response_content)
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'encrypt_cert_no_list' in response:
            self.encrypt_cert_no_list = response['encrypt_cert_no_list']
