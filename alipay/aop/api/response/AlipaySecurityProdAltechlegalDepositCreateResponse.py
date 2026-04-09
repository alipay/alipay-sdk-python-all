#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdAltechlegalDepositCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAltechlegalDepositCreateResponse, self).__init__()
        self._deposit_no = None

    @property
    def deposit_no(self):
        return self._deposit_no

    @deposit_no.setter
    def deposit_no(self, value):
        self._deposit_no = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAltechlegalDepositCreateResponse, self).parse_response_content(response_content)
        if 'deposit_no' in response:
            self.deposit_no = response['deposit_no']
