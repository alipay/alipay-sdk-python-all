#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankQrcodeCreateResponse, self).__init__()
        self._qrcode = None
        self._qrcode_id = None
        self._qrcode_out_id = None

    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value
    @property
    def qrcode_id(self):
        return self._qrcode_id

    @qrcode_id.setter
    def qrcode_id(self, value):
        self._qrcode_id = value
    @property
    def qrcode_out_id(self):
        return self._qrcode_out_id

    @qrcode_out_id.setter
    def qrcode_out_id(self, value):
        self._qrcode_out_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'qrcode' in response:
            self.qrcode = response['qrcode']
        if 'qrcode_id' in response:
            self.qrcode_id = response['qrcode_id']
        if 'qrcode_out_id' in response:
            self.qrcode_out_id = response['qrcode_out_id']
