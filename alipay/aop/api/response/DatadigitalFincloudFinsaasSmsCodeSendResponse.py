#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasSmsCodeSendResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasSmsCodeSendResponse, self).__init__()
        self._expire_time = None
        self._sms_code = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasSmsCodeSendResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'sms_code' in response:
            self.sms_code = response['sms_code']
