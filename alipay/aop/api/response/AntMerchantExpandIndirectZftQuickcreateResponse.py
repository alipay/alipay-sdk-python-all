#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectZftQuickcreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectZftQuickcreateResponse, self).__init__()
        self._order_id = None
        self._sign_qr_code_url = None
        self._sign_short_chain_url = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def sign_qr_code_url(self):
        return self._sign_qr_code_url

    @sign_qr_code_url.setter
    def sign_qr_code_url(self, value):
        self._sign_qr_code_url = value
    @property
    def sign_short_chain_url(self):
        return self._sign_short_chain_url

    @sign_short_chain_url.setter
    def sign_short_chain_url(self, value):
        self._sign_short_chain_url = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectZftQuickcreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'sign_qr_code_url' in response:
            self.sign_qr_code_url = response['sign_qr_code_url']
        if 'sign_short_chain_url' in response:
            self.sign_short_chain_url = response['sign_short_chain_url']
