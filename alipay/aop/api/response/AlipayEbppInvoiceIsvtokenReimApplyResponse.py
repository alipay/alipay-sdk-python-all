#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceIsvtokenReimApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceIsvtokenReimApplyResponse, self).__init__()
        self._isv_token = None
        self._serial_no = None

    @property
    def isv_token(self):
        return self._isv_token

    @isv_token.setter
    def isv_token(self, value):
        self._isv_token = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceIsvtokenReimApplyResponse, self).parse_response_content(response_content)
        if 'isv_token' in response:
            self.isv_token = response['isv_token']
        if 'serial_no' in response:
            self.serial_no = response['serial_no']
