#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseVerificationcodeSendResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseVerificationcodeSendResponse, self).__init__()
        self._type = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseVerificationcodeSendResponse, self).parse_response_content(response_content)
        if 'type' in response:
            self.type = response['type']
