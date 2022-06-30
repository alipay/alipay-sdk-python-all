#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcApplyorderSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcApplyorderSignResponse, self).__init__()
        self._etc_deduct_sign_page_url = None
        self._etc_deduct_sign_token = None

    @property
    def etc_deduct_sign_page_url(self):
        return self._etc_deduct_sign_page_url

    @etc_deduct_sign_page_url.setter
    def etc_deduct_sign_page_url(self, value):
        self._etc_deduct_sign_page_url = value
    @property
    def etc_deduct_sign_token(self):
        return self._etc_deduct_sign_token

    @etc_deduct_sign_token.setter
    def etc_deduct_sign_token(self, value):
        self._etc_deduct_sign_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcApplyorderSignResponse, self).parse_response_content(response_content)
        if 'etc_deduct_sign_page_url' in response:
            self.etc_deduct_sign_page_url = response['etc_deduct_sign_page_url']
        if 'etc_deduct_sign_token' in response:
            self.etc_deduct_sign_token = response['etc_deduct_sign_token']
