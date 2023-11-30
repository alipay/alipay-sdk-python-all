#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppQrcodeTemporaryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppQrcodeTemporaryCreateResponse, self).__init__()
        self._qr_code = None
        self._qr_code_url = None

    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppQrcodeTemporaryCreateResponse, self).parse_response_content(response_content)
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
