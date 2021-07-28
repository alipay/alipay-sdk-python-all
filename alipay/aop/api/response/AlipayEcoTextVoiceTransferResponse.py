#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoTextVoiceTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoTextVoiceTransferResponse, self).__init__()
        self._call_id = None
        self._code = None
        self._message = None

    @property
    def call_id(self):
        return self._call_id

    @call_id.setter
    def call_id(self, value):
        self._call_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoTextVoiceTransferResponse, self).parse_response_content(response_content)
        if 'call_id' in response:
            self.call_id = response['call_id']
        if 'code' in response:
            self.code = response['code']
        if 'message' in response:
            self.message = response['message']
