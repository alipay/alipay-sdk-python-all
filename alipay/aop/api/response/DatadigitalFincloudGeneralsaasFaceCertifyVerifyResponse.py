#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceCertifyVerifyResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceCertifyVerifyResponse, self).__init__()
        self._certify_url = None

    @property
    def certify_url(self):
        return self._certify_url

    @certify_url.setter
    def certify_url(self, value):
        self._certify_url = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceCertifyVerifyResponse, self).parse_response_content(response_content)
        if 'certify_url' in response:
            self.certify_url = response['certify_url']
