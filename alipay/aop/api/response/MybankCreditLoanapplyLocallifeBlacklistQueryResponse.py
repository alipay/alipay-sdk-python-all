#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyLocallifeBlacklistQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyLocallifeBlacklistQueryResponse, self).__init__()
        self._is_black = None

    @property
    def is_black(self):
        return self._is_black

    @is_black.setter
    def is_black(self, value):
        self._is_black = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyLocallifeBlacklistQueryResponse, self).parse_response_content(response_content)
        if 'is_black' in response:
            self.is_black = response['is_black']
