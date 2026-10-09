#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpaydirectPurchaseCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpaydirectPurchaseCreateResponse, self).__init__()
        self._expire_time = None
        self._purchase_qr_code = None
        self._purchase_url = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def purchase_qr_code(self):
        return self._purchase_qr_code

    @purchase_qr_code.setter
    def purchase_qr_code(self, value):
        self._purchase_qr_code = value
    @property
    def purchase_url(self):
        return self._purchase_url

    @purchase_url.setter
    def purchase_url(self, value):
        self._purchase_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpaydirectPurchaseCreateResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'purchase_qr_code' in response:
            self.purchase_qr_code = response['purchase_qr_code']
        if 'purchase_url' in response:
            self.purchase_url = response['purchase_url']
