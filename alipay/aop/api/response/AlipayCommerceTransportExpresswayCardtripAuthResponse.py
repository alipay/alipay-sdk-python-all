#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportExpresswayCardtripAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportExpresswayCardtripAuthResponse, self).__init__()
        self._auth_biz_no = None
        self._biz_token = None

    @property
    def auth_biz_no(self):
        return self._auth_biz_no

    @auth_biz_no.setter
    def auth_biz_no(self, value):
        self._auth_biz_no = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportExpresswayCardtripAuthResponse, self).parse_response_content(response_content)
        if 'auth_biz_no' in response:
            self.auth_biz_no = response['auth_biz_no']
        if 'biz_token' in response:
            self.biz_token = response['biz_token']
