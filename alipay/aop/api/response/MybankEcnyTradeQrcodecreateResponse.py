#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyTradeQrcodecreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyTradeQrcodecreateResponse, self).__init__()
        self._merchant_id = None
        self._qr_code = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyTradeQrcodecreateResponse, self).parse_response_content(response_content)
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
