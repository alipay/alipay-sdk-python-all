#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfopenmqImSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfopenmqImSendResponse, self).__init__()
        self._message = None
        self._msgid = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def msgid(self):
        return self._msgid

    @msgid.setter
    def msgid(self, value):
        self._msgid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfopenmqImSendResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'msgid' in response:
            self.msgid = response['msgid']
