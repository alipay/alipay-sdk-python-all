#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthEcsignUserwhitelistSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignUserwhitelistSaveResponse, self).__init__()
        self._sign_order_no = None

    @property
    def sign_order_no(self):
        return self._sign_order_no

    @sign_order_no.setter
    def sign_order_no(self, value):
        self._sign_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignUserwhitelistSaveResponse, self).parse_response_content(response_content)
        if 'sign_order_no' in response:
            self.sign_order_no = response['sign_order_no']
