#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataPrinterTaskSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataPrinterTaskSubmitResponse, self).__init__()
        self._code = None
        self._data = None
        self._message = None
        self._status = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
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
        response = super(AlipayDataPrinterTaskSubmitResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'data' in response:
            self.data = response['data']
        if 'message' in response:
            self.message = response['message']
        if 'status' in response:
            self.status = response['status']
