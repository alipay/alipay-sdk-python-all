#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMallScanpurchasePreorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallScanpurchasePreorderCreateResponse, self).__init__()
        self._advance_order_id = None
        self._qr_code = None
        self._qr_code_url = None

    @property
    def advance_order_id(self):
        return self._advance_order_id

    @advance_order_id.setter
    def advance_order_id(self, value):
        self._advance_order_id = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMallScanpurchasePreorderCreateResponse, self).parse_response_content(response_content)
        if 'advance_order_id' in response:
            self.advance_order_id = response['advance_order_id']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
