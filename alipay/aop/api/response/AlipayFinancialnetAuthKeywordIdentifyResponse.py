#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthKeywordIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthKeywordIdentifyResponse, self).__init__()
        self._is_financial_account = None
        self._is_financial_inst = None

    @property
    def is_financial_account(self):
        return self._is_financial_account

    @is_financial_account.setter
    def is_financial_account(self, value):
        self._is_financial_account = value
    @property
    def is_financial_inst(self):
        return self._is_financial_inst

    @is_financial_inst.setter
    def is_financial_inst(self, value):
        self._is_financial_inst = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthKeywordIdentifyResponse, self).parse_response_content(response_content)
        if 'is_financial_account' in response:
            self.is_financial_account = response['is_financial_account']
        if 'is_financial_inst' in response:
            self.is_financial_inst = response['is_financial_inst']
