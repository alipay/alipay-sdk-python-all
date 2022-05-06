#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankMarketingMcaplatformConstractSignResponse(AlipayResponse):

    def __init__(self):
        super(MybankMarketingMcaplatformConstractSignResponse, self).__init__()
        self._sign_result = None

    @property
    def sign_result(self):
        return self._sign_result

    @sign_result.setter
    def sign_result(self, value):
        self._sign_result = value

    def parse_response_content(self, response_content):
        response = super(MybankMarketingMcaplatformConstractSignResponse, self).parse_response_content(response_content)
        if 'sign_result' in response:
            self.sign_result = response['sign_result']
