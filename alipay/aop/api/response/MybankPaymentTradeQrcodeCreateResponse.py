#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeQrcodeCreateResponse, self).__init__()
        self._encrypt_token = None
        self._url = None

    @property
    def encrypt_token(self):
        return self._encrypt_token

    @encrypt_token.setter
    def encrypt_token(self, value):
        self._encrypt_token = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'encrypt_token' in response:
            self.encrypt_token = response['encrypt_token']
        if 'url' in response:
            self.url = response['url']
