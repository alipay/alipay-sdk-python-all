#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyManagerAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyManagerAuthResponse, self).__init__()
        self._biz_token = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyManagerAuthResponse, self).parse_response_content(response_content)
        if 'biz_token' in response:
            self.biz_token = response['biz_token']
