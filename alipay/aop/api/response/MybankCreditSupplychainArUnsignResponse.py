#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainArUnsignResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainArUnsignResponse, self).__init__()
        self._invalid_result = None

    @property
    def invalid_result(self):
        return self._invalid_result

    @invalid_result.setter
    def invalid_result(self, value):
        self._invalid_result = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainArUnsignResponse, self).parse_response_content(response_content)
        if 'invalid_result' in response:
            self.invalid_result = response['invalid_result']
