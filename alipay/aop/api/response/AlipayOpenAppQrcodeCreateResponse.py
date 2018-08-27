#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppQrcodeCreateResponse, self).__init__()
        self._qr_code_url = None

    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
