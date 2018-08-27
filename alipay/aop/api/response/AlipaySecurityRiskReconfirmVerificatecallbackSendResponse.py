#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskReconfirmVerificatecallbackSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskReconfirmVerificatecallbackSendResponse, self).__init__()
        self._extend_info = None

    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskReconfirmVerificatecallbackSendResponse, self).parse_response_content(response_content)
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
