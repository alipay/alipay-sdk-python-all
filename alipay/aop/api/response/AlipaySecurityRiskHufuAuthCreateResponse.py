#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskHufuAuthCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskHufuAuthCreateResponse, self).__init__()
        self._info = None
        self._serial = None
        self._token = None

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value
    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskHufuAuthCreateResponse, self).parse_response_content(response_content)
        if 'info' in response:
            self.info = response['info']
        if 'serial' in response:
            self.serial = response['serial']
        if 'token' in response:
            self.token = response['token']
