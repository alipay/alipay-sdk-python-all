#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunStaticsiteDomaincertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteDomaincertQueryResponse, self).__init__()
        self._certificate = None
        self._enable_https = None

    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value
    @property
    def enable_https(self):
        return self._enable_https

    @enable_https.setter
    def enable_https(self, value):
        self._enable_https = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteDomaincertQueryResponse, self).parse_response_content(response_content)
        if 'certificate' in response:
            self.certificate = response['certificate']
        if 'enable_https' in response:
            self.enable_https = response['enable_https']
