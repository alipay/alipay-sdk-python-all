#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeAcpCreditinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeAcpCreditinfoQueryResponse, self).__init__()
        self._auth = None
        self._credit_level_code = None

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def credit_level_code(self):
        return self._credit_level_code

    @credit_level_code.setter
    def credit_level_code(self, value):
        self._credit_level_code = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeAcpCreditinfoQueryResponse, self).parse_response_content(response_content)
        if 'auth' in response:
            self.auth = response['auth']
        if 'credit_level_code' in response:
            self.credit_level_code = response['credit_level_code']
