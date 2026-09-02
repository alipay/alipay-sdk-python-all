#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAuthcodeGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAuthcodeGenerateResponse, self).__init__()
        self._authcode = None
        self._expire_time = None

    @property
    def authcode(self):
        return self._authcode

    @authcode.setter
    def authcode(self, value):
        self._authcode = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAuthcodeGenerateResponse, self).parse_response_content(response_content)
        if 'authcode' in response:
            self.authcode = response['authcode']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
