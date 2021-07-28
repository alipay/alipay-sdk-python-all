#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialForestSimplecertificateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialForestSimplecertificateQueryResponse, self).__init__()
        self._cert_id = None
        self._user_name = None

    @property
    def cert_id(self):
        return self._cert_id

    @cert_id.setter
    def cert_id(self, value):
        self._cert_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialForestSimplecertificateQueryResponse, self).parse_response_content(response_content)
        if 'cert_id' in response:
            self.cert_id = response['cert_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
