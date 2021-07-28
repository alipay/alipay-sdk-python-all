#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentCredential import PaymentCredential
from alipay.aop.api.domain.CredentialsResponseHeader import CredentialsResponseHeader


class AlipayPayCodecApplepayCredentialsGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayCodecApplepayCredentialsGetResponse, self).__init__()
        self._credentials = None
        self._response_header = None

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        if isinstance(value, list):
            self._credentials = list()
            for i in value:
                if isinstance(i, PaymentCredential):
                    self._credentials.append(i)
                else:
                    self._credentials.append(PaymentCredential.from_alipay_dict(i))
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, CredentialsResponseHeader):
            self._response_header = value
        else:
            self._response_header = CredentialsResponseHeader.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayPayCodecApplepayCredentialsGetResponse, self).parse_response_content(response_content)
        if 'credentials' in response:
            self.credentials = response['credentials']
        if 'response_header' in response:
            self.response_header = response['response_header']
