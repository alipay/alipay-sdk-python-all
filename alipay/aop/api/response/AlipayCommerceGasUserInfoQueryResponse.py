#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceGasUserInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGasUserInfoQueryResponse, self).__init__()
        self._encrypted_data = None

    @property
    def encrypted_data(self):
        return self._encrypted_data

    @encrypted_data.setter
    def encrypted_data(self, value):
        self._encrypted_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGasUserInfoQueryResponse, self).parse_response_content(response_content)
        if 'encrypted_data' in response:
            self.encrypted_data = response['encrypted_data']
