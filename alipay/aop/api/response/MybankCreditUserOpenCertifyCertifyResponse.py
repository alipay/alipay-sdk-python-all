#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditUserOpenCertifyCertifyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditUserOpenCertifyCertifyResponse, self).__init__()
        self._auth_url = None

    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditUserOpenCertifyCertifyResponse, self).parse_response_content(response_content)
        if 'auth_url' in response:
            self.auth_url = response['auth_url']
