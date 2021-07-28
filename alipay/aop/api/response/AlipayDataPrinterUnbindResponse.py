#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataPrinterUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataPrinterUnbindResponse, self).__init__()
        self._code = None
        self._message = None
        self._status = None

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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataPrinterUnbindResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'message' in response:
            self.message = response['message']
        if 'status' in response:
            self.status = response['status']
